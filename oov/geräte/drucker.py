
class Drucker:
    def __init__(self, hersteller, modell, tonerstand):
        self.__hersteller = hersteller
        self.__modell = modell
        self.__tonerstand = tonerstand
        self.__status = False  # Drucker ist ausgeschaltet

    def setTonerstand(self, tonerstand):
        self.__tonerstand = tonerstand

    def reduziereTonerstand(self, wert):
            self.__tonerstand = self.__tonerstand - wert


    def einschalten(self):
        self.__status = True
        print(f"{self.__modell} wurde eingeschaltet.")

    def ausschalten(self):
        self.__status = False
        print(f"{self.__modell} wurde ausgeschaltet.")
        print("Ende")

    def drucken(self):
        if not self.__status:
            print("Drucker ist ausgeschaltet!")
        elif self.__tonerstand <= 0 :
            print("Kann nicht drucken!")
            print(f"Tonerstand leer: {self.__tonerstand}%")
        else:
            print("Dokument wird gedruckt.")
            self.reduziereTonerstand(10)
            print(f"Tonerstand: {self.__tonerstand}%")


