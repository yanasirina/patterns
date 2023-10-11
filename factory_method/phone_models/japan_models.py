from base import MyPhoneBase


class JapanMixin(MyPhoneBase):
    pass


class JapanMyPhoneMini(JapanMixin):
    storage = 128
    camera = 'Japanese Super Camera 2023'
    display_size = (140, 70)


class JapanMyPhone(JapanMixin):
    storage = 256
    camera = 'Japanese Super Camera 2023'
    display_size = (150, 75)


class JapanMyPhoneMax(JapanMixin):
    storage = 512
    camera = 'Japanese Super Puper Camera 2023'
    display_size = (160, 80)

    def test(self):
        super().test()
        print('Тест для совместимости японской "супер-пупер камеры"')
