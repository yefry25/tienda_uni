from datetime import datetime;

class Order():
    def __init__(self, Id: int = None, IdUsuario: int = None, IdPrenda:int = None, FechaCreacion: datetime = None):
        self.Id = Id
        self.IdUsuario = IdUsuario
        self.IdPrenda = IdPrenda
        self.FechaCreacion = FechaCreacion