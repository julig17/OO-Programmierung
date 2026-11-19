class Punkt:
    def __init__(self, x: float, y: float):
        self.__x = float(x)
        self.__y = float(y)

    def getX(self) -> float:
        return self.__x

    def getY(self) -> float:
        return self.__y

    def setX(self, wert: float) -> None:
        self.__x = float(wert)

    def setY(self, wert: float) -> None:
        self.__y = float(wert)