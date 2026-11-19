from punkt import Punkt
import math

class Kreis:
    def __init__(self, p1: Punkt, radius: float):
        if radius <= 0:
            raise ValueError('Der Radius muss positiv sein.')
        self.__p1 = p1
        self.__radius = float(radius)
        self.__anz = None

    def getMittelpunkt(self) -> Punkt:
        return self.__p1

    def getRadius(self) -> float:
        return self.__radius

    def flaecheBerechnen(self) -> float:
        return math.pi * self.__radius ** 2

    def rufeAnzeige(self, anzeige: 'Anzeige') -> None:
        self.__anz = anzeige
        anzeige.zeichneKreis(self)
