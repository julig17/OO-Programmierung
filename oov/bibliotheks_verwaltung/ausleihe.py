class Ausleihe:
    def __init__(self, buch, mitglied):
        self.buch = buch
        self.mitglied = mitglied
        self.aktiv = False

    def ausleihen(self):
        if self.aktiv:
            print("Diese Ausleihe ist bereits aktiv.")
        elif self.buch.ausleihen():
            self.aktiv = True
            print(f"Ausgeliehen von: {self.mitglied.name}")

    def zurueckgeben(self):
        if self.aktiv:
            self.buch.zurueckgeben()
            self.aktiv = False
            print(f"Rückgabe durch: {self.mitglied.name}")
        else:
            print("Diese Ausleihe ist nicht aktiv.")
