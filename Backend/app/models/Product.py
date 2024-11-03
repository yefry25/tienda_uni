from decimal import Decimal

class Product:
    def __init__(self, id:int, name: str , categoryId: int ,brandId: int , price: Decimal ,stock: int, description:str, active: bool):
        self.id = id
        self.name = name
        self.categoryId = categoryId
        self.brandId = brandId
        self.price = price
        self.stock = stock
        self.description = description
        self.active = active