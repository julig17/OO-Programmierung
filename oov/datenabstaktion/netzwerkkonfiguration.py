
class NetzwerkKonfiguration:

    def __init__(self):
        # Beispielhafte Interne Datenstruktur
        self.__konfiguration = {
            "ip": "192.168.1.100",
            "subnetzmaske": "255.255.255.0",
            "gateway": "192.168.1.1",
            "dns": "8.8.8.8"
        }

    def get_ip_adresse(self):
        return self.__konfiguration["ip"]

    def get_gateway(self):
        return self.__konfiguration["gateway"]

    def get_dns_server(self):
        return self.__konfiguration["dns"]


# Objekt erzeugen
netzwerk = NetzwerkKonfiguration()

# Öffentliche Methoden aufrufen
print(netzwerk.get_ip_adresse())
print(netzwerk.get_gateway())
print(netzwerk.get_dns_server())
