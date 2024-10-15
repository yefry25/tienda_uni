from datetime import datetime
from decimal import Decimal

class Bill:
    def __init__(self, Id:int, IdOrden: int, MontoToTal: Decimal, FechaEmision: datetime):
        self.Id = Id,
        self.IdOrden = IdOrden,
        self.MontoTotal = MontoToTal,
        self.FechaEmision = FechaEmision