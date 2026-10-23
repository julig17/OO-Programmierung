class Temperatursensor:

    # Konstanten
    UNTERGRENZE = -89
    OBERGRENZE = 57

    def __init__(self):
        self.__temperatur = 20.0

    # Öffentlicher Getter
    def get_temperatur(self):
        return self.__temperatur

    # Öffentlicher Setter
    def set_temperatur(self, temperatur):
        if self.__ist_gueltig(temperatur):
            self.__temperatur = temperatur
        else:
            print("Ungültiger Temperaturwert:", temperatur)

    # Private Hilfsmethode
    def __ist_gueltig(self, temperatur):
        return self.UNTERGRENZE <= temperatur <= self.OBERGRENZE

    # Öffentliche Methode zur Ausgabe
    def temperatur_anzeigen(self):
        print(f"Aktuelle Temperatur: {self.__temperatur:.1f} °C")
