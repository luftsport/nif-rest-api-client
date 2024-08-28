from . import snake_case, rename_keys, Competences

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