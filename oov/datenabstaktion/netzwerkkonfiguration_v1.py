class NetzwerkKonfiguration:

    def __init__(self):
        """self.__konfiguration = [
                    "192.168.1.100",
                    "255.255.255.0",
                    "192.168.1.1",
                    "8.8.8.8"
        ]"""
        self.__ip_adress = "192.168.1.100"

    def get_ip_adressen(self):
        #return self.__konfiguration[0]
        return self.__ip_adress;

    def get_gateway(self):
        return self.__gateway[2]