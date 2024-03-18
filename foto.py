from error import DimensionError
class Foto():
    MAX = 2500

    def __init__(self, ancho: int, alto: int, ruta: str) -> None:
        self.__ancho = ancho
        self.__alto = alto
        ruta = ruta

    @property
    def ancho(self) -> int:
        return self.__ancho

    @ancho.setter
    def ancho(self, ancho) -> None:
        if ancho < 1 or ancho > self.MAX:
            #raise DimensionError(mensaje="El nuevo ancho está fuera de rango.")
            raise DimensionError(mensaje="El nuevo ancho está fuera de rango.",dimension=ancho,maximo=self.MAX)
        else:
            self.__ancho = ancho

    @property
    def alto(self) -> int:
        return self.__alto

    @alto.setter
    def alto(self, alto) -> None:
        if alto < 1 or alto > self.MAX:
            #raise DimensionError(mensaje="El nuevo alto está fuera de rango.",dimension=alto)
            raise DimensionError(mensaje="El nuevo alto está fuera de rango.",dimension=alto,maximo=self.MAX)
        else:
            self.__alto = alto
            
            
if __name__ == "__main__":
    f = Foto(200,200,"ruta")
    #f.alto=0
    f.ancho = 2501