from base import MyPhoneBase


class UAEMixin(MyPhoneBase):
    def download_apps(self):
        self.apps = self.apps.remove('face_time')
        super().download_apps()


class UAEMyPhoneMini(UAEMixin):
    storage = 128
    camera = 'Camera 2021'
    display_size = (140, 70)


class UAEMyPhone(UAEMixin):
    storage = 256
    camera = 'Camera 2022'
    display_size = (150, 75)


class UAEMyPhoneMax(UAEMixin):
    storage = 512
    camera = 'Camera 2023'
    display_size = (160, 80)
