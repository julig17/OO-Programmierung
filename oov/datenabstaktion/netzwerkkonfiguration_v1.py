class NetzwerkKonfiguration:

    def __init__(self):
        self.__konfiguration = [
                    "192.168.1.100",
                     "255.255.255.0",
                    "192.168.1.1",
                    "8.8.8.8"
        ]

    def get_ip_adresse(self):
        return self.__konfiguration[1]

    def get_gateway(self):
        return self.__gateway[2]