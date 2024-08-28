from . import snake_case, rename_keys, Competences
"""
{
    'personId': 301041,
    'firstName': 'Einar',
    'lastName': 'Huseby',
    'hasCompetences': [33225, 33224],
 'hasCompetencesCount': 2,
    'hasOptionalCompetences': [33225, 33224],
    'competences': [
    {'name': 'F-ITE - INSTRUCTOR EX TAN', 'passed': 50, 'isPassed': False, 'expires': None, 'competenceId': '66667606',
     'competenceType': 'Kompetansedefinisjon', 'joined': '2023-09-18T12:20:28.047', 'id': 17107588, 'orgId': '376',
     'sportId': '109', 'childrenCompetenceIds': [], 'parentCompetenceIds': []},
    {'name': 'Fallskjermfornyelse instruktør tandem', 'passed': 50, 'isPassed': False, 'expires': None,
     'competenceId': '66669569', 'competenceType': 'E-kurs', 'joined': '2023-09-18T12:00:47.08', 'id': 17107416,
     'orgId': '376', 'sportId': '109', 'childrenCompetenceIds': [], 'parentCompetenceIds': [66667606, 66667615]},
    {'name': 'F-TD - TANDEM DEMO', 'passed': 50, 'isPassed': False, 'expires': None, 'competenceId': '66667616',
     'competenceType': 'Kompetansedefinisjon', 'joined': '2021-01-27T08:45:42.7', 'id': 10534201, 'orgId': '376',
     'sportId': '109', 'childrenCompetenceIds': [], 'parentCompetenceIds': []},
    {'name': 'Aktivitetsleder - Norges studentidrettsforbund', 'passed': 25, 'isPassed': False, 'expires': None,
     'competenceId': '66669416', 'competenceType': 'Kompetansedefinisjon', 'joined': '2019-03-22T13:42:58.753',
     'id': 7814840, 'orgId': None, 'sportId': '0', 'childrenCompetenceIds': [65852, 66668115],
     'parentCompetenceIds': []},
    {'name': 'Bryting - Trener 2', 'passed': 7, 'isPassed': False, 'expires': None, 'competenceId': '66669250',
     'competenceType': 'Kompetansedefinisjon', 'joined': '2019-03-22T13:42:58.57', 'id': 7814838, 'orgId': '358',
     'sportId': '0', 'childrenCompetenceIds': [66668069, 66668115, 66668142, 66669245, 66669246, 66669247, 66669249],
     'parentCompetenceIds': []},
    {'name': 'Ren Utøver (Antidoping Norge - NIF e-kurs)', 'passed': 50, 'isPassed': False, 'expires': None,
     'competenceId': '66668115', 'competenceType': 'E-kurs', 'joined': '2019-03-22T13:17:32.917', 'id': 7814796,
     'orgId': '1', 'sportId': '0', 'childrenCompetenceIds': [],
     'parentCompetenceIds': [41617, 41647, 42293, 66667614, 66668565, 66669161, 66669250, 66669375, 66669416, 66669562,
                             66669563, 66676473, 66676602, 66677025, 66678384, 66678914, 66679813]},
    {'name': 'REN Utøver -Seiling', 'passed': 25, 'isPassed': False, 'expires': None, 'competenceId': '66669375',
     'competenceType': 'Kompetansedefinisjon', 'joined': '2019-03-22T13:42:58.667', 'id': 7814839, 'orgId': '380',
     'sportId': '31', 'childrenCompetenceIds': [66668115, 66678628], 'parentCompetenceIds': []},
    {'name': 'Skiskyting - Trener 1', 'passed': 6, 'isPassed': False, 'expires': None, 'competenceId': '66676473',
     'competenceType': 'Kompetansedefinisjon', 'joined': '2021-03-04T06:32:08.887', 'id': 10801221, 'orgId': '388',
     'sportId': '39',
     'childrenCompetenceIds': [66666997, 66667018, 66667277, 66668076, 66668115, 66669190, 66669616, 66671924, 66671946,
                               66676948], 'parentCompetenceIds': []},
    {'name': 'Testdefinisjon - Trener 1 - svømming (SKAL SLETTES)', 'passed': 6, 'isPassed': False, 'expires': None,
     'competenceId': '66669126', 'competenceType': 'Kompetansedefinisjon', 'joined': '2019-03-22T13:42:58.387',
     'id': 7814836, 'orgId': None, 'sportId': '35', 'childrenCompetenceIds': [], 'parentCompetenceIds': []},
    {'name': 'Trener 1 - Amerikansk fotball', 'passed': 5, 'isPassed': False, 'expires': None,
     'competenceId': '66669161', 'competenceType': 'Kompetansedefinisjon', 'joined': '2019-03-22T13:42:58.483',
     'id': 7814837, 'orgId': '395', 'sportId': '173',
     'childrenCompetenceIds': [66666997, 66667018, 66667277, 66667946, 66668069, 66668076, 66668115, 66668142, 66669158,
                               66669159, 66669160], 'parentCompetenceIds': []},
    {'name': 'Trener 1 - Basketball (T140TR1 v2021)', 'passed': 6, 'isPassed': False, 'expires': None,
     'competenceId': '66678384', 'competenceType': 'Kompetansedefinisjon', 'joined': '2022-01-13T11:04:08.397',
     'id': 12401430, 'orgId': None, 'sportId': '5',
     'childrenCompetenceIds': [66667277, 66668115, 66668142, 66669251, 66678381, 66678382, 66678383],
     'parentCompetenceIds': [66677024]},
    {'name': 'Trener 1 - Cheer', 'passed': 5, 'isPassed': False, 'expires': None, 'competenceId': '66669077',
     'competenceType': 'Kompetansedefinisjon', 'joined': '2019-03-22T13:42:58.32', 'id': 7814835, 'orgId': '395',
     'sportId': '258', 'childrenCompetenceIds': [66668190, 66668191, 66669056], 'parentCompetenceIds': []},
    {'name': 'Trener 1 - Disksport', 'passed': 5, 'isPassed': False, 'expires': None, 'competenceId': '66669562',
     'competenceType': 'Kompetansedefinisjon', 'joined': '2019-03-22T13:42:58.84', 'id': 7814841, 'orgId': '395',
     'sportId': '368',
     'childrenCompetenceIds': [66666997, 66667018, 66667277, 66667946, 66668069, 66668076, 66668115, 66668142, 66669554,
                               66669557, 66669560], 'parentCompetenceIds': []},
    {'name': 'Trener 1 - Lacrosse', 'passed': 5, 'isPassed': False, 'expires': None, 'competenceId': '66669563',
     'competenceType': 'Kompetansedefinisjon', 'joined': '2019-03-22T13:42:58.92', 'id': 7814842, 'orgId': '395',
     'sportId': '365',
     'childrenCompetenceIds': [66666997, 66667018, 66667277, 66667946, 66668069, 66668076, 66668115, 66668142, 66669555,
                               66669559, 66669561], 'parentCompetenceIds': []},
    {'name': 'Trener 1 - Roing', 'passed': 6, 'isPassed': False, 'expires': None, 'competenceId': '66676602',
     'competenceType': 'Kompetansedefinisjon', 'joined': '2021-03-04T06:32:09.107', 'id': 10801222, 'orgId': '378',
     'sportId': '0',
     'childrenCompetenceIds': [39265, 66666997, 66667018, 66667277, 66668076, 66668115, 66668142, 66676203],
     'parentCompetenceIds': []},
    {'name': 'Trener 2 - Kampsport', 'passed': 6, 'isPassed': False, 'expires': None, 'competenceId': '41617',
     'competenceType': 'Kompetansedefinisjon', 'joined': '2019-03-22T13:42:58.06', 'id': 7814832, 'orgId': '391',
     'sportId': '42',
     'childrenCompetenceIds': [66942, 67748, 67750, 66668115, 66668142, 66668143, 66670076, 66670077, 66678375],
     'parentCompetenceIds': [66677069]},
    {'name': 'F-T - TANDEM INSTRUCTOR', 'passed': 50, 'isPassed': False, 'expires': None, 'competenceId': '66667615',
     'competenceType': 'Kompetansedefinisjon', 'joined': '2019-02-21T08:10:55.19', 'id': 7580166, 'orgId': '376',
     'sportId': '109', 'childrenCompetenceIds': [], 'parentCompetenceIds': [66667616]},
    {'name': 'F-SPO - FAI SPORTING LICENCE', 'passed': 25, 'isPassed': False, 'expires': None,
     'competenceId': '66667614', 'competenceType': 'Kompetansedefinisjon', 'joined': '2019-02-12T14:37:00.05',
     'id': 7437961, 'orgId': '376', 'sportId': '109', 'childrenCompetenceIds': [], 'parentCompetenceIds': []},
    {'name': 'Instruktør, klasse 2 - fallskjerm, del 2', 'passed': 100, 'isPassed': True, 'expires': None,
     'competenceId': '33225', 'competenceType': 'Kurs', 'joined': '2008-01-30T18:43:21.03', 'id': 2677160,
     'orgId': '376', 'sportId': '27', 'childrenCompetenceIds': [], 'parentCompetenceIds': []},
    {'name': 'Instruktør, klasse 2 - fallskjerm, del 1', 'passed': 100, 'isPassed': True, 'expires': None,
     'competenceId': '33224', 'competenceType': 'Kurs', 'joined': '2008-01-30T18:57:55.43', 'id': 2681678,
     'orgId': '376', 'sportId': '27', 'childrenCompetenceIds': [], 'parentCompetenceIds': []}]
}
]
"""
class PersonCompetences:
    def __init__(self, person_competences):

        if type(person_competences) == list and len(person_competences) == 1:
            self.value = person_competences[0]
        else:
            self.value = person_competences

        self._map()

    def _map(self):

        competences = Competences([x for x in self.value['competences'] if x['competenceType'] == 'Kompetansedefinisjon']).value


        self.value.pop('competences', None)
        self.value = snake_case(self.value)

        self.value['competences'] = competences

        #self.value = del_by_value(self.value, None)
        #self.value = del_by_value(self.value, '')
        #