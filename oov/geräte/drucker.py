
class Drucker:
    def __init__(self, hersteller, modell, tonerstand):
        self.hersteller = hersteller
        self.modell = modell
        self.tonerstand = tonerstand
        self.status = False  # Drucker ist ausgeschaltet

    def einschalten(self):
        self.status = True
        print(f"{self.modell} wurde eingeschaltet.")

    def ausschalten(self):
        self.status = False
        print(f"{self.modell} wurde ausgeschaltet.")

    def drucken(self):
        if not self.status:
            print("Drucker ist ausgeschaltet!")
        else:
            print("Dokument wird gedruckt.")
            print(f"Tonerstand: {self.tonerstand}%")


