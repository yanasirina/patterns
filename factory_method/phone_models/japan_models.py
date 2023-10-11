from .base import MyPhoneBase


class JapanMixin(MyPhoneBase):
    pass


class JapanMyPhoneMini(JapanMixin):
    def __init__(self):
        super().__init__()
        self.storage = 128
        self.camera = 'Japanese Super Camera 2023'
        self.display_size = (140, 70)


class JapanMyPhone(JapanMixin):
    def __init__(self):
        super().__init__()
        self.storage = 256
        self.camera = 'Japanese Super Camera 2023'
        self.display_size = (150, 75)


class JapanMyPhoneMax(JapanMixin):
    def __init__(self):
        super().__init__()
        self.storage = 512
        self.camera = 'Japanese Super Puper Camera 2023'
        self.display_size = (160, 80)

    def test(self):
        super().test()
        print('Тест для совместимости японской "супер-пупер камеры"')
