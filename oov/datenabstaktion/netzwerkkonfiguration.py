import ipaddress
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


    def pruefe_netzwerkkonfiguration(self):

        try:
            # 1. IP-Adresse prüfen
            ip = ipaddress.IPv4Address(
                self.__konfiguration["ip"]
            )

            # 2. Subnetzmaske prüfen
            netzwerk = ipaddress.IPv4Network(
                (
                    self.__konfiguration["ip"],
                    self.__konfiguration["subnetzmaske"]
                ),
                strict=False
            )

            # 3. Gateway prüfen
            gateway = ipaddress.IPv4Address(
                self.__konfiguration["gateway"]
            )

            # 4. DNS-Server prüfen
            ipaddress.IPv4Address(
                self.__konfiguration["dns"]
            )

            # 5. Prüfen, ob Gateway im Subnetz liegt
            if gateway not in netzwerk:
                return False

            # 6. Prüfen, ob IP und Gateway
            # gültige Hostadressen im Netz sind
            if ip not in netzwerk.hosts():
                return False

            if gateway not in netzwerk.hosts():
                return False

            if ip == gateway:
                return False

            return True

        except (ValueError, KeyError):
            return False


# Objekt erzeugen
netzwerk = NetzwerkKonfiguration()

# Öffentliche Methoden aufrufen
print(netzwerk.get_ip_adresse())
print(netzwerk.get_gateway())
print(netzwerk.get_dns_server())
print(netzwerk.pruefe_netzwerkkonfiguration())
