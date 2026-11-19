from punkt import Punkt
import math

class Linie:
    def __init__(self, p1: Punkt, p2: Punkt):
        self.__p1 = p1
        self.__p2 = p2
        self.__anz = None

    def getPunkte(self):
        return self.__p1, self.__p2

    def laengeBerechnen(self) -> float:
        dx = self.__p2.getX() - self.__p1.getX()
        dy = self.__p2.getY() - self.__p1.getY()
        return math.hypot(dx, dy)

    def rufeAnzeige(self, anzeige: 'Anzeige') -> None:
        self.__anz = anzeige
        anzeige.zeichneLinie(self)