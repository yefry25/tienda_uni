from datetime import datetime

class Shipping:
    def __init__(self, id:int, fecha_registro: datetime, prenda_id : int, usuario_id: int, direccion: str, fecha_despacho: datetime, fecha_estimada_llegada: datetime):
        self.id = id,
        self.fecha_registro = fecha_registro,
        self.prenda_id = prenda_id,
        self.usuario_id = usuario_id,
        self.direccion = direccion,
        self.fecha_despacho = fecha_despacho,
        self.fecha_estimada_llegada = fecha_estimada_llegada