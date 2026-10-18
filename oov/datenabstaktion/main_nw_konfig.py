from netzwerkkonfiguration import NetzwerkKonfiguration as NK
from netzwerkkonfiguration_v1 import NetzwerkKonfiguration as NK1
# Objekt erzeugen
netzwerk = NK()
# Objekt er zweiten Version erstellen
netzwerk1 = NK1()

# Öffentliche Methoden aufrufen
print(netzwerk.get_ip_adresse())
print(netzwerk.get_gateway())
print(netzwerk.get_dns_server())

print("Geänderte Datenstruktur, gleiche Schnittstelle")
# Öffentliche Methoden aufrufen
print(netzwerk1.get_ip_adresse())