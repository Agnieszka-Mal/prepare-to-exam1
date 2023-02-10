class User:
    def __init__(self, mail, name, surname):
        self.mail = mail
        self.name = name
        self.surname = surname

    def say_hello(self):
        return "User %(name)s %(surname)s says hello." % {
            "name": self.name,
            "surname": self.surname
        }

class VIPUser(User):

    def __init__(self, mail, name, surname, vip_card_number):
        super().__init__(mail, name, surname)
        self._vip_card_number = vip_card_number if self._check_card_number(vip_card_number) else None

    @property
    def vip_card_number(self):
        return self._vip_card_number

    @vip_card_number.setter
    def vip_card_number(self, vip_card_number):
        self._vip_card_number = vip_card_number if self._check_card_number(vip_card_number) else None


    @staticmethod
    def _check_card_number(vip_card_number):
        return vip_card_number > 999 and vip_card_number % 2 == 0

    @staticmethod
    def use_vip_card():
        pass

if __name__ == '__main__':
    user = VIPUser("Brajanusz", "Kowalski", "Kowalski@mail.pl", 1999)
    print(user.vip_card_number)
    user.vip_card_number = 9998
    print(user.vip_card_number)