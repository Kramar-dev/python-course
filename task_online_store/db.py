from data_classes import *


class Goods:
    def __init__(self):
        self.__baseId: int = 0
        self.db: dict[int, Good] = {
            self.next_id(): Good('Smartphone', 1500, 10),
            self.next_id(): Good('Smartwatch', 500, 20),
            self.next_id(): Good('Monitor', 2300, 30),
            self.next_id(): Good('Mouse', 50, 40),
            self.next_id(): Good('Keyboard', 100, 50),
            self.next_id(): Good('Book', 25, 60),
            self.next_id(): Good('Bed', 5000, 70),
            self.next_id(): Good('Headphones', 350, 80),
            self.next_id(): Good('Car', 50000, 90)
        }

    def next_id(self) -> int:
        self.__baseId += 11
        return self.__baseId


class Users:
    def __init__(self):
        self.db: dict[str, User] = {
            'admin@mail.com': User('admin@mail.com', 'admin', True, False, {}, 0, []),
            'slave@mail.com': User('slave@mail.com', 'slave', False, False, {}, 0, []),
            'john@mail.com': User('john@mail.com', 'john', False, False, {}, 0, []),
            'mia@mail.com': User('mia@mail.com', 'mia', False, False, {}, 0, []),
            'tony@mail.com': User('tony@mail.com', 'tony', False, False, {}, 0, [])
        }

    @staticmethod
    def login_correct(login: str) -> bool:
        # TODO mail regex
        if len(login) < 5:
            return False
        if '@' not in login:
            return False
        return True

    @staticmethod
    def password_correct(password: str) -> bool:
        # TODO check special condition for entered password
        if len(password) < 8:
            return False
        return True



