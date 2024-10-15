from decimal import Decimal 

class payment_type:
    def __init__(self, id: int, tipo_pago: str, monto_pagado: Decimal, usuario_id: int, prenda_id: int):
        self.id = id,
        self.tipo_pago = tipo_pago,
        self.monto_pagado = monto_pagado,
        self.usuario_id = usuario_id,
        self.prenda_id = prenda_id