from .base import DeviceBase


class TV(DeviceBase):
    def turn_on(self):
        print('Телевизор включен')

    def turn_off(self):
        print('Телевизор выключен')

    def set_channel(self, channel):
        print(f'Выбран канал {channel} на телевизоре')

    def restart(self):
        print('Перезагрузка телевизора')
