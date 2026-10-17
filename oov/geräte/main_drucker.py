from drucker import Drucker
# Zwei Drucker-Objekte erstellen
drucker1 = Drucker("HP", "LaserJet", 80)
drucker2 = Drucker("Canon", "PIXMA", 50)

# Drucken bei ausgeschaltetem Drucker
drucker1.drucken()

# Drucker einschalten
drucker1.einschalten()

# Dokument drucken
drucker1.drucken()
drucker1.drucken()

# Drucker ausschalten
drucker1.ausschalten()