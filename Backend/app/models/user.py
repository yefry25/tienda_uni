from datetime import datetime

class User:
    def __init__(self, id: int, firstName: str, lastName: str, nickName: str, password: str, email: str, address: str, phoneNumber: str, creationDate: datetime, active: bool):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.nickName = nickName
        self.password = password
        self.email = email
        self.address = address
        self.phoneNumber = phoneNumber
        self.creationDate = creationDate
        self.active = active
