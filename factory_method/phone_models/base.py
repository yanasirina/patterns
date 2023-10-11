class MyPhoneException(Exception):
    pass


class MyPhoneBase:
    """Класс с базовой реализацией основных методов"""
    def __init__(self):
        self.storage = None
        self.camera = None
        self.display_size = None
        self.apps = ['calculator', 'face time', 'camera']

    def prepare(self):
        if self.storage and self.camera and self.display_size:
            print(f'Память {self.storage} гб готова')
            print(f'Камера {self.camera} готова')
            print(f'Экран {self.display_size} готов')
        else:
            raise MyPhoneException('Запчасти не были предоставлены')

    def build(self):
        print('Сборка MyPhone')

    def download_apps(self):
        for app in self.apps:
            print(f'Установка приложения {app}')

    def test(self):
        print('Тестирование MyPhone')

    def box(self):
        print('Упаковка MyPhone')
