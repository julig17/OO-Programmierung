from drucker import Drucker

# Zwei Drucker-Objekte erstellen
drucker1 = Drucker("HP", "LaserJet", 80)
drucker2 = Drucker("Canon", "PIXMA", 50)
drucker1 =  Drucker("HP", "LaserJet", 70)
drucker3 = Drucker("HP", "", 70)

print("ZUerst")

# Drucken bei ausgeschaltetem Drucker
drucker1.drucken()
drucker1.setTonerstand(50)

drucker1.__tonerstand = 20
drucker1.setTonerstand(25)

print(drucker1.__tonerstand)

# Drucker einschalten
drucker1.einschalten()

# Dokument drucken
drucker1.drucken()
drucker1.drucken()


# Drucker ausschalten
drucker1.ausschalten()


hallo = "HAllo"
print(type(hallo))
print(type(drucker1))