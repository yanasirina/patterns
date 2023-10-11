from .base import MyPhoneBase


class UAEMixin(MyPhoneBase):
    def download_apps(self):
        self.apps.remove('face time')
        super().download_apps()


class UAEMyPhoneMini(UAEMixin):
    def __init__(self):
        super().__init__()
        self.storage = 128
        self.camera = 'Camera 2021'
        self.display_size = (140, 70)


class UAEMyPhone(UAEMixin):
    def __init__(self):
        super().__init__()
        self.storage = 256
        self.camera = 'Camera 2022'
        self.display_size = (150, 75)


class UAEMyPhoneMax(UAEMixin):
    def __init__(self):
        super().__init__()
        self.storage = 512
        self.camera = 'Camera 2023'
        self.display_size = (160, 80)
