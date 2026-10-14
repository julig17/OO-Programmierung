import rennwagen as r

# Objekt A erzeugen vom Klassse Rennwagen
auto_a = r.Rennwagen()

# Methoden aufrufen
auto_a.setze_name("Lotus")
auto_a.setze_farbe("blau")

# Attribute ausgeben
print("Name:", auto_a._name)
print("Farbe:", auto_a._farbe)
