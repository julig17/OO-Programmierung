from linie import Linie
from rechteck import Rechteck
from kreis import Kreis
from anzeige import Anzeige
from punkt import Punkt


def main() -> None:
    linie = Linie(Punkt(40, 60), Punkt(180, 160))
    kreis = Kreis(Punkt(330, 125), 65)
    rechteck = Rechteck(
        Punkt(80, 230), Punkt(260, 230),
        Punkt(260, 350), Punkt(80, 350)
    )

    anzeige = Anzeige()
    linie.rufeAnzeige(anzeige)
    kreis.rufeAnzeige(anzeige)
    rechteck.rufeAnzeige(anzeige)

    print(f'Linienlänge: {anzeige.laenge(linie):.2f}')
    print(f'Kreisfläche: {anzeige.flaeche(kreis):.2f}')
    print(f'Rechteckfläche: {anzeige.flaeche(rechteck):.2f}')
    anzeige.anzeigen()


if __name__ == '__main__':
    main()