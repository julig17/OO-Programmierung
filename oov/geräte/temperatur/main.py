from hardwaresimulator import HardwareSimulator
from temperatursensor import Temperatursensor
import time

# Hauptprogramm
hardware = HardwareSimulator(0)
sensor = Temperatursensor()

while True:
    temperatur = hardware.temperatur_messen()
    sensor.set_temperatur(temperatur)
    sensor.temperatur_anzeigen()

    time.sleep(10)
