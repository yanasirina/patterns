from factory_method.phone_models import MyPhoneBase


class MyPhoneFactory:
    def order_phone(self, phone_type: str) -> MyPhoneBase:
        phone = self.create_phone(phone_type=phone_type)

        phone.prepare()
        phone.build()
        phone.test()
        phone.download_apps()
        phone.box()

        return phone

    def create_phone(self, phone_type: str):
        raise NotImplementedError('Метод create_phone не переопределен')
