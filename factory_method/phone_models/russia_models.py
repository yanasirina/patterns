from base import MyPhoneBase


class RussiaMixin(MyPhoneBase):
    def download_apps(self):
        self.apps = self.apps.append('гос. услуги')
        super().download_apps()


class RussiaMyPhoneMini(RussiaMixin):
    storage = 512
    camera = 'Some camera'
    display_size = (140, 70)


class RussiaMyPhone(RussiaMixin):
    storage = 1024
    camera = 'Some camera'
    display_size = (150, 75)

    def box(self):
        print('Упаковка в коробку цвета флага России')


class RussiaMyPhoneMax(RussiaMixin):
    storage = 2048
    camera = 'Some camera'
    display_size = (160, 80)

    def download_apps(self):
        super().download_apps()
        print('Установка премиум версии гос.услуг')
