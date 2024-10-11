from decimal import Decimal

class Clothes:
    def __init__(self, id:int, marca:str, talla: str, cantidad_disponible: int, colores: str, descripcion: str, tipo_prenda: str, puntaje: Decimal, comentario: str):
        self.id = id,
        self.marca = marca,
        self.talla = talla,
        self.cantidad_disponible = cantidad_disponible,
        self.colores = colores,
        self.descripcion = descripcion,
        self.tipo_prenda = tipo_prenda,
        self.puntaje = puntaje,
        self.comentario = comentario