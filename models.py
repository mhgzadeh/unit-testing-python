class Supervisor:

    def __init__(self, username, password, phone_number=None):
        self.username = username
        self.password = password
        self.phone_number = phone_number
        self.__is_logged_in = False

    @property
    def logged_in(self):
        return self.__is_logged_in

    @classmethod
    def sample(cls):
        return cls('ali', '123', '12234')

    @classmethod
    def login(cls, username, password, phone_number=None):
        supervisor = cls(username, password, phone_number)
        supervisor.__is_logged_in = True
        return supervisor

    def protected(self):
        if self.__is_logged_in:
            return [1, 2, 3]
        return None
