import tkinter as tk
from linie import Linie
from rechteck import Rechteck
from kreis import Kreis

class Anzeige:
    def __init__(self):
        self.__fenster = tk.Tk()
        self.__fenster.title('Geometrische Grundformen')
        self.__zeichenflaeche = tk.Canvas(
            self.__fenster, width=620, height=420, bg='white'
        )
        self.__zeichenflaeche.pack(padx=12, pady=12)

    def zeichneLinie(self, linie: Linie) -> None:
        p1, p2 = linie.getPunkte()
        self.__zeichenflaeche.create_line(
            p1.getX(), p1.getY(), p2.getX(), p2.getY(),
            fill='black', width=3
        )

    def zeichneKreis(self, kreis: Kreis) -> None:
        p = kreis.getMittelpunkt()
        r = kreis.getRadius()
        self.__zeichenflaeche.create_oval(
            p.getX() - r, p.getY() - r,
            p.getX() + r, p.getY() + r,
            outline='black', width=3
        )

    def zeichneRechteck(self, rechteck: Rechteck) -> None:
        koordinaten = []
        for punkt in rechteck.getPunkte():
            koordinaten.extend((punkt.getX(), punkt.getY()))
        self.__zeichenflaeche.create_polygon(
            *koordinaten, outline='black', fill='', width=3
        )

    def flaeche(self, objekt) -> float:
        """Entspricht Flaeche(Kreis) bzw. Flaeche(Rechteck) aus UML."""
        if not isinstance(objekt, (Kreis, Rechteck)):
            raise TypeError('Erwartet wird ein Kreis oder Rechteck.')
        return objekt.flaecheBerechnen()

    def laenge(self, linie: Linie) -> float:
        return linie.laengeBerechnen()

    def anzeigen(self) -> None:
        self.__fenster.mainloop()
