from .base import RemoteBase


class MobileApp(RemoteBase):
    """Класс Мобильное Приложение"""
    def restart(self):
        # предполагается, что перезагружать устройство можно только через мобильное приложение,
        # поэтому метод не определен в базовом классе
        self.device.restart()
