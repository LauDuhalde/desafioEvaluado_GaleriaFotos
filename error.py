class DimensionError(Exception):
    def __init__(self, mensaje, dimension=None, maximo=None):
        self.mensaje = mensaje
        self.dimension = dimension
        self.maximo = maximo
    def __str__(self):
        if(self.dimension is None and self.maximo is None):
            return super.__str__(self.mensaje)
        else:
            mensaje_retorno = f"Mensaje: {self.mensaje}"
            if self.dimension is not None:
                mensaje_retorno += f", Dimension: {self.dimension}"
            if self.maximo is not None:
                mensaje_retorno += f", Maximo: {self.maximo}"
            return mensaje_retorno 