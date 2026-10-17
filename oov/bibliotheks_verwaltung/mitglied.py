class Mitglied:
    def __init__(self, name, mitgliedsnummer):
        self.name = name
        self.mitgliedsnummer = mitgliedsnummer

    def info_anzeigen(self):
        print(f"Mitglied: {self.name}")
        print(f"Mitgliedsnummer: {self.mitgliedsnummer}")
