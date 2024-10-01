from datetime import datetime
from decimal import Decimal

class User:
    def __init__(self, id: int, nombres: str, apellidos: str, usuario: str, fecha_nacimiento: datetime, total_compras: Decimal, direccion: str, numero_telefonico: str, password: str, estado: bool):
        self.id = id
        self.nombres = nombres
        self.apellidos = apellidos
        self.usuario = usuario
        self.fecha_nacimiento = fecha_nacimiento
        self.total_compras = total_compras
        self.direccion = direccion
        self.numero_telefonico = numero_telefonico
        self.password = password
        self.estado = estado
