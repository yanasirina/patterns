from .base import MyPhoneFactory
from factory_method import phone_models, consts


class UAEFactory(MyPhoneFactory):
    def create_phone(self, phone_type: str):
        if phone_type == consts.MY_PHONE_MINI:
            return phone_models.UAEMyPhoneMini()
        elif phone_type == consts.MY_PHONE_STANDARD:
            return phone_models.UAEMyPhone()
        elif phone_type == consts.MY_PHONE_MAX:
            return phone_models.UAEMyPhoneMax()
        else:
            raise NotImplementedError('Модель телефона не обработана')
