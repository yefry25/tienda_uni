from datetime import datetime;
from decimal import Decimal

class Order():
    def __init__(self, Id: int = None, UserId: int = None, CreationDate: datetime = None, statusId:int = None, total = Decimal):
        self.Id = Id
        self.UserId = UserId
        self.CreationDate = CreationDate
        self.statusId = statusId
        self.total = total