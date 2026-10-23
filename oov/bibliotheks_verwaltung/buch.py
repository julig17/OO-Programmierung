class Buch:
    def __init__(self, titel, autor, isbn):
        self.titel = titel
        self.autor = autor
        self.isbn = isbn
        self.erscheinungsjahr = self.erscheinungsjahr
        self.auflage = auflage
        self.verfuegbar = True

    def ausleihen(self):
        if self.verfuegbar:
            self.verfuegbar = False
            print(f"'{self.titel}' wurde ausgeliehen.")
            return True
        print(f"'{self.titel}' ist bereits ausgeliehen.")
        return False

    def zurueckgeben(self):
        if not self.verfuegbar:
            self.verfuegbar = True
            print(f"'{self.titel}' wurde zurückgegeben.")
        else:
            print(f"'{self.titel}' ist bereits verfügbar.")
