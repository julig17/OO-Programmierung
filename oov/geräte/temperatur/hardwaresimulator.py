import random

class HardwareSimulator:

    def __init__(self, temp):
            self.__temperatur = temp

    # Öffentlicher Setter
    def set_temperatur(self, temperatur):
        self.__temperatur = temperatur

    def temperatur_messen(self):
        # Simuliert einen Temperaturwert der Hardware
        self.set_temperatur(round(random.uniform(-60, 60), 1))
        return self.__temperatur