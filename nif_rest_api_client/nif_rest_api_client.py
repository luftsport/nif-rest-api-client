from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
import base64
from functools import wraps
import inspect
from datetime import datetime, timedelta
from dateutil import tz
from retry import retry
import requests
import json
import os.path

from .typings import PersonCompetences

LOCAL_TIMEZONE = 'Europe/Oslo'


def before(f):
    @wraps(f)
    def wrapper(self, *args, **kw):
        if hasattr(self, '_before') and inspect.ismethod(self._before):
            self._before()
        result = f(self, *args, **kw)
        return result

    return wrapper


class NifRestApiClient:

    def __init__(self, client_id, client_secret, token_file='nif.token', realm='PROD'):

        if realm == 'DST':
            self.TOKEN_URL = 'https://iddst.nif.no/connect/token'  # 'https://iddst.nif.no/connect/token' # 
            self.NIF_DATA_URL = 'https://datadst.nif.no/api/v1'  # 'https://data.nif.no/api/v1' #'https://datadst.nif.no/api/v1' #
            self.NIF_EDUCATION_URL = 'https://nif-education-api-prod-app.azurewebsites.net/api/v1'
        else:
            self.TOKEN_URL = 'https://id.nif.no/connect/token'
            self.NIF_DATA_URL = 'https://data.nif.no/api/v1'
            self.NIF_EDUCATION_URL = 'https://nif-education-api-prod-app.azurewebsites.net/api/v1'

        self.tz_local = tz.gettz(LOCAL_TIMEZONE)
        self.token = None
        self.token_file = token_file
        self.auth = requests.auth.HTTPBasicAuth(client_id, client_secret)
        self.client = BackendApplicationClient(client_id=client_id)
        self.oauth = OAuth2Session(client=self.client)
        # self._get_token()

    def _is_token_valid(self):
        try:
            if self.token is not None and datetime.now().timestamp() < self.token.get('expires_at', 0):
                return True
        except:
            pass

        return False

    def _load_token_file(self) -> dict or None:
        if os.path.isfile(self.token_file) is True:
            try:
                with open(self.token_file, 'r', encoding='utf-8') as f:
                    token = json.load(f)
                    if token:
                        return token
            except Exception as e:
                print('[ERR] loading file failed', e)
        return None

    def _save_token_file(self):
        with open(self.token_file, 'w+', encoding='utf-8') as f:
            if self.token is not None and self._is_token_valid() is True:
                json.dump(self.token, f)

    @retry((requests.exceptions.ConnectionError), tries=3, delay=0.1)
    def _fetch_token(self):
        self.token = self.oauth.fetch_token(token_url=self.TOKEN_URL, auth=self.auth)

    def _get_token(self, force=False):
        """
        Get token, try file first if not valid then fetch token from token resource

        :param force: force token fetch from token resource omitting validating checks
        :return:
        """
        self.token = self._load_token_file()

        if self.token is None or self._is_token_valid() is False or force is True:
            self._fetch_token()
            self.token = self.oauth.token  # ['expires_at'] = self.token['expires_at'] + int(round(datetime.now().timestamp() - datetime.now().replace(tzinfo=self.tz_local).timestamp(), 0))
            if self.token is not None:
                self._save_token_file()
        elif self.token is not None and self._is_token_valid() is True:
            self.oauth.token = self.token

    def _before(self):
        """Verify token"""

        try:
            if self._is_token_valid() is True:
                pass
            elif self.token is None or self._is_token_valid() is False:
                self._get_token()
            else:
                raise
        except Exception as e:
            raise Exception('Could not init token', e)

    @before
    @retry((requests.exceptions.ConnectionError, ConnectionError), tries=3, delay=0.1)
    def _get(self, base_url, resource_url, params=None):
        return self.oauth.get(f'{base_url}/{resource_url}', params=params)

    @before
    @retry((requests.exceptions.ConnectionError, ConnectionError), tries=3, delay=0.1)
    def _post(self, base_url, resource_url, payload=None, params=None):
        return self.oauth.post(f'{base_url}/{resource_url}', json=payload, params=params)

    def get_person(self, person_id):

        r = self._get(self.NIF_DATA_URL, '/person/personinfo', params={'personId': person_id})
        # self.oauth.get(f'{self.NIF_DATA_URL}/person/personinfo', params={'personId': person_id})

        if r.status_code == 200:
            return True, r.json()

        return False, None

    def get_person_ids(self, person_id=None, buypass_id=None):

        r = self._get(self.NIF_DATA_URL, '/person/PersonInfo/PersonIds',
                      {'personId': person_id, 'buypassId': buypass_id})

        if r.status_code == 200:
            return True, r.json()

        return False, None

    def get_person_merged(self, person_id):

        r = self._get(self.NIF_DATA_URL, '/person/PersonMergeCheck', {'personIds': [person_id]})

        if r.status_code == 200:
            return True, r.json()

        return False, None

    def get_person_relations(self, person_id=None, buypass_id=None):

        if person_id is not None:
            r = self._get(self.NIF_DATA_URL, f'/person/PersonRelation/{person_id}')
        elif buypass_id is not None:
            r = self._get(self.NIF_DATA_URL, f'/person/PersonRelation/bpid/{buypass_id}')
        else:
            return False, None

        if r.status_code == 200:
            return True, r.json()

        return False, None

    def get_person_police_certificate(self, person_id=None, buypass_id=None):

        r = self._get(self.NIF_DATA_URL, '/person/PoliceCertificate', {'personId': person_id, 'buypassId': buypass_id})

        if r.status_code == 200:
            return True, r.json()

        return False, None

    def get_person_licenses(self, person_id, buypass_id=None):
        r = self._get(self.NIF_DATA_URL, '/activity/license/person', {'personId': person_id, 'buypassId': buypass_id})

        if r.status_code == 200:
            return True, r.json()

        return False, None

    def get_person_licenses_check(self, person_id, buypass_id=None):
        r = self._get(self.NIF_DATA_URL, '/activity/LicenseCheck', {'personId': person_id, 'buypassId': buypass_id})

        if r.status_code == 200:
            return True, r.json()

        return False, None

    def get_org_licenses(self, org_id):
        r = self._get(self.NIF_DATA_URL, f'/activity/LicenseCheck/org/{org_id}')
        if r.status_code == 200:
            return True, r.json()

        return False, None

    def get_fed_licenses(self, fed_org_id=376):
        r = self._get(self.NIF_DATA_URL, f'/activity/license/products/{fed_org_id}')
        if r.status_code == 200:
            return True, r.json()

        return False, None

    """EDU API"""

    def get_person_competences(self, person_id):

        r = self._get(self.NIF_EDUCATION_URL, '/competences/competencesforperson', params={'personId': person_id})

        if r.status_code == 200:
            try:
                return True, PersonCompetences(r.json()).value
            except:
                pass

        return False, None

    def get_org_competences(self, org_id):

        r = self._get(self.NIF_EDUCATION_URL, f'/competences/competencefororg/{org_id}')

        if r.status_code == 200:
            return True, r.json()

        return False, None

    def get_competence_types(self, competence_id=None, activity_id=None, deactivated=False):

        r = self._get(self.NIF_EDUCATION_URL, '/competences/competencetypes',
                      params={'competenceId': competence_id,
                              'sportId': activity_id,
                              'showDeactivated': deactivated})

        if r.status_code == 200:
            return True, r.json()

        return False, None

    def get_competence_types_by_activity(self, activity_id):
        r = self._get(self.NIF_EDUCATION_URL, '/competences/competencetypes/sport/batch',
                      params={'sportIds': activity_id})

        if r.status_code == 200:
            return True, r.json()

        return False, None

    def search_competences(self, query):  # , org_id=None):

        """orgId has no effect
        {
          "competenceTitle": "string",
          "description": "string",
          "shortDescription": "string",
          "certificationDescription": "string",
          "owningOrgId": "string",
          "competenceId": "string",
          "sportId": 0
        }
        """
        r = self._post(self.NIF_EDUCATION_URL, '/competences/search', payload=query)  # , 'orgId': org_id})

        if r.status_code in [200, 201]:
            return True, r.json()

        return False, None

    """ORGS"""

    def get_clubs(self, org_id=376, logo=False):

        r = self._get(self.NIF_DATA_URL, '/org/AllClubs', {'orgId': org_id, 'logo': logo})

        if r.status_code == 200:
            return True, r.json()

        return False, None

    def get_club_structure(self, org_id=376, logo=False):
        r = self._get(self.NIF_DATA_URL, '/org/ClubStructure', {'orgId': 376, 'logo': False})

        if r.status_code == 200:
            return True, r.json()

        return False, None

    def get_clubs_by_activity(self, activity_id):

        r = self._get(self.NIF_DATA_URL, f'/org/ClubsBySport/{activity_id}', None)

        if r.status_code == 200:
            return True, r.json()

        return False, None

    def get_organization(self, org_id, logo=False):

        r = self._get(self.NIF_DATA_URL, '/org/Organisation', {'orgIds': 376, 'logo': False})

        if r.status_code == 200:
            return True, r.json()

        return False, None

    def get_organizations_by_org_type(self, org_type_id):

        r = self._get(self.NIF_DATA_URL, f'/org/Organisation/orgtype/{org_type_id}')

        if r.status_code == 200:
            return True, r.json()

        return False, None

    def get_organizations_by_org_type_in_federation(self, org_type_id):
        """Only org_type_id 6 works! Not 5 or 14 or 19"""

        r = self._get(self.NIF_DATA_URL, f'/org/Organisation/federation/376/{org_type_id}')

        if r.status_code == 200:
            return True, r.json()

        return False, None

    def get_organization_activities(self, org_id):
        """Only org_type_id 6 works! Not 5 or 14 or 19"""

        r = self._get(self.NIF_DATA_URL, f'/org/sport/{org_id}')

        if r.status_code == 200:
            return True, r.json()

        return False, None

    def get_organization_teams(self, org_id, activity_id=0):
        """Only org_type_id 6 works! Not 5 or 14 or 19"""

        r = self._get(self.NIF_DATA_URL, f'/org/Teams', params={'orgId': org_id, 'sportId': activity_id})

        if r.status_code == 200:
            return True, r.json()

        return False, None

    def search_organization(self, query, org_type_id):
        r = self._post(self.NIF_DATA_URL, '/org/Organisation/Search',
                       payload={'orgName': query, 'orgTypeId': org_type_id})

        if r.status_code in [200, 201]:
            return True, r.json()

        return False, None

    """
    Activities
    """

    def get_activities(self):
        r = self._get(self.NIF_DATA_URL, '/activity/Sport')

        if r.status_code == 200:
            return True, r.json()

        return False, None

    """
    Activities/Events
    """

    def get_events_for_org(self, org_id, start_date=datetime.now()):
        """Only org_type_id 5 or 376"""
        r = self._get(self.NIF_DATA_URL, f'/activity/EventsForOrg', params={'clubId': org_id, 'startDate': start_date})

        if r.status_code == 200:
            return True, r.json()

        return False, None

    def get_events_for_org_schedule(self, org_id, start_date=datetime.now(),
                                    end_date=datetime.now() + timedelta(days=14)):
        """Only 376"""
        r = self._get(self.NIF_DATA_URL, f'/activity/EventsForOrg/Schedule',
                      params={'orgId': org_id, 'startDate': start_date, 'endDate': end_date})

        if r.status_code == 200:
            return True, r.json()

        return False, None

    def get_event(self, event_id):
        r = self._get(self.NIF_DATA_URL, f'/activity/Events', params={'eventId': event_id})

        if r.status_code == 200:
            return True, r.json()

        return False, None

    def get_event_participants(self, event_id):
        r = self._get(self.NIF_DATA_URL, f'/activity/Participants', params={'eventId': event_id})

        if r.status_code == 200:
            return True, r.json()

        return False, None

    """
    Drone pilot
    """

    def register_drone_pilot(self, person_id):
        """GET???"""

        r = self._get(self.NIF_DATA_URL, f'/activity/FlyDrone/{person_id}')

        if r.status_code in [200, 201]:
            return r.status_code, r.json()

        return False, None
