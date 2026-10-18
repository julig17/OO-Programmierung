class NetzwerkKonfiguration:

    def __init__(self):
        self.__ip = "192.168.1.100"
        self.__gateway = "192.168.1.1"

    def get_ip_adresse(self):
        return self.__ip

    def get_gateway(self):
        return self.__gateway