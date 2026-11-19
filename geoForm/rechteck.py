from punkt import Punkt

class Rechteck:
    def __init__(self, p1: Punkt, p2: Punkt, p3: Punkt, p4: Punkt):
        self.__punkte = (p1, p2, p3, p4)
        self.__anz = None

    def getPunkte(self):
        return self.__punkte

    def flaecheBerechnen(self) -> float:
        # Gaußsche Trapezformel für die vier umlaufend angegebenen Ecken.
        punkte = self.__punkte
        doppelte_flaeche = sum(
            punkte[i].getX() * punkte[(i + 1) % 4].getY()
            - punkte[(i + 1) % 4].getX() * punkte[i].getY()
            for i in range(4)
        )
        return abs(doppelte_flaeche) / 2

    def rufeAnzeige(self, anzeige: 'Anzeige') -> None:
        self.__anz = anzeige
        anzeige.zeichneRechteck(self)
