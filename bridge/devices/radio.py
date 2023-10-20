from .base import DeviceBase


class Radio(DeviceBase):
    def turn_on(self):
        print('Радио включено')

    def turn_off(self):
        print('Радио выключено')

    def set_channel(self, channel):
        print(f'Выбран канал {channel} на радио')

    def restart(self):
        print('Перезагрузка радио')
