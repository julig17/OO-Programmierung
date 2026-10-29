class Laptop:
    def __init__(self, marke, modell):
        self.__marke = marke
        self.__modell = modell

    def einschalten(self):
        print("Laptop wird eingeschaltet")

    def setzteMarke(self, marke):
        if (marke == "Lenovo" or marke == "HP"):
            self.__marke = marke


