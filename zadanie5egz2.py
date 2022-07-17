from exam_lib import User

class VIPUser(User):
    def __init__(self, name, surname, mail, card_number):
        super().__init__(name=name, surname=surname, mail=mail)
        self._card_number = card_number if self._checked_card_number(card_number) else None

    @staticmethod
    def _checked_card_number(card_number):
        return card_number > 999 and card_number % 2 == 0

    @staticmethod
    def use_vip_card():
        return None

    @property
    def card_number(self):
        return self._card_number

    @card_number.setter
    def card_number(self, card_number):
        self._card_number = card_number if self._checked_card_number(card_number) else None
