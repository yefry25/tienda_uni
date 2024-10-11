from datetime import datetime
from decimal import Decimal

class Bill:
    def __init__(self, id:int, fecha_compra: datetime, prenda_id: int, precio: Decimal, referencia: str, talla: str, iva : Decimal, descuento: Decimal, total: Decimal):
        self.id = id,
        self.fecha_compra = fecha_compra,
        self.prenda_id = prenda_id,
        self.precio = precio,
        self.referencia = referencia,
        self.talla = talla,
        self.iva = iva,
        self.descuento = descuento,
        self.total = total