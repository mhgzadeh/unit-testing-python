from abc import abstractmethod


class User:
    counter = 0

    def __init__(self, username, password, fullname, email):
        self.username = username
        self.password = password
        self.fullname = fullname
        self.email = email
        User.counter += 1

    @classmethod
    def create(cls, username, password, fullname, email):
        if len(password) < 4:
            print('Not acceptable password.')
            return None
        return cls(username, password, fullname, email)

    @staticmethod
    def _password_validation(password):
        if len(password) < 4:
            print('Not acceptable password.')
            return True
        return False

    @abstractmethod
    def __introduce_your_self(self):
        print('Intro yourself')


class Reseller(User):
    def __init__(self, brand, logo, *args, **kwargs):
        self.brand = brand
        self.logo = logo
        super().__init__(*args, **kwargs)

    def __introduce_your_self(self):
        print(f'My name is {self.fullname} form {self.brand}')


class Customer(User):
    def __init__(self, username, password, fullname, email, nickname):
        super().__init__(username, password, fullname, email)
        self.nickname = nickname
        self.wallet = 0

    @property
    def off_15_percent(self):
        if self.wallet > 10000:
            self.wallet += 100

    def __introduce_your_self(self):
        print(f'My name is {self.nickname} '
              f'and my email address is {self.email}')


class Product:
    def __init__(self, name, price, description, reseller=None):
        self.name = name
        self.price = price
        self.description = description
        self.reseller = reseller
