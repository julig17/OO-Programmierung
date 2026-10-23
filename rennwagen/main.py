import rennwagen as r

# Objekt A erzeugen vom Klassse Rennwagen
auto_a = r.Rennwagen()
auto_b = r.Rennwagen()
auto_c = auto_a

# Methoden aufrufen
auto_a.setze_name("Lotus")
auto_a.setze_farbe("blau")

auto_b.setze_name("Opel")
auto_b.setze_farbe("rot")

# Attribute ausgeben
print("Name:", auto_a._name)
print("Farbe:", auto_a._farbe)
