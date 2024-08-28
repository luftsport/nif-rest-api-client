from .competence import Competence


class Competences:
    def __init__(self, competences):

        self.value = competences

        self._map()

    def _map(self):
        new_value = []
        for item in self.value:
            new_value.append(Competence(dict(item)).value)

        self.value = new_value
