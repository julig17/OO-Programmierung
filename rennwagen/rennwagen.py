#Klasse Rennwagen als Bauplan
class Rennwagen:
    def __init__(self):
        self._name = ""
        self._farbe = ""
        self._kw = 0
        self._hubraum = 0.0

    def setze_name(self, name):
        if isinstance(name, str) and name.strip():
            self._name = name

    def setze_farbe(self, farbe):
        if isinstance(farbe, str) and farbe.strip():
            self._farbe = farbe


