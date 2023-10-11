from .base import MyPhoneFactory
from factory_method import phone_models, consts


class RussiaFactory(MyPhoneFactory):
    def create_phone(self, phone_type: str):
        if phone_type == consts.MY_PHONE_MINI:
            return phone_models.RussiaMyPhoneMini()
        elif phone_type == consts.MY_PHONE_STANDARD:
            return phone_models.RussiaMyPhone()
        elif phone_type == consts.MY_PHONE_MAX:
            return phone_models.RussiaMyPhoneMax()
        else:
            raise NotImplementedError('Модель телефона не обработана')
