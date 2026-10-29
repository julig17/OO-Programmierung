from buch import Buch
from mitglied import Mitglied
from ausleihe import Ausleihe



buch1 = Buch("Python lernen", "Max Müller", "12345")
buch2 = Buch("Java Grundlagen", "Anna Schmidt", "67890")
mitglied1 = Mitglied("Lisa Weber", 1001)

mitglied1.info_anzeigen()
print("\n--- Ausleihe ---")
ausleihe1 = Ausleihe(buch1, mitglied1)
ausleihe1.ausleihen()
ausleihe1.ausleihen()
print("\n--- Rückgabe ---")
ausleihe1.zurueckgeben()
print("\n--- Erneute Ausleihe ---")
ausleihe1.ausleihen()
