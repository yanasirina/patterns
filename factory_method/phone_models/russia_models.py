from .base import MyPhoneBase


class RussiaMixin(MyPhoneBase):
    def download_apps(self):
        self.apps.append('гос. услуги')
        super().download_apps()


class RussiaMyPhoneMini(RussiaMixin):
    def __init__(self):
        super().__init__()
        self.storage = 512
        self.camera = 'Some camera'
        self.display_size = (140, 70)


class RussiaMyPhone(RussiaMixin):
    def __init__(self):
        super().__init__()
        self.storage = 1024
        self.camera = 'Some camera'
        self.display_size = (150, 75)

    def box(self):
        print('Упаковка в коробку цвета флага России')


class RussiaMyPhoneMax(RussiaMixin):
    def __init__(self):
        super().__init__()
        self.storage = 2048
        self.camera = 'Some camera'
        self.display_size = (160, 80)

    def download_apps(self):
        super().download_apps()
        print('Установка премиум версии гос.услуг')
