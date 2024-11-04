from datetime import datetime

class Bill:
    def __init__(self, Id:int, UserId: int, IssuedDate: datetime):
        self.Id = Id
        self.UserId = UserId
        self.IssuedDate = IssuedDate