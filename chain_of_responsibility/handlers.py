class Handler:
    def __init__(self, successor=None):
        self.successor = successor

    def handle_request(self, value, category):
        if self.successor:
            self.successor.handle_request(value, category)


class EmailHandler(Handler):
    def handle_request(self, value, category):
        if category == "email":
            print(f"Обработка электронной почты: {value}")
        else:
            super().handle_request(value, category)


class PhoneHandler(Handler):
    def handle_request(self, value, category):
        if category == "phone":
            print(f"Обработка телефона: {value}")
        else:
            super().handle_request(value, category)


class UsernameHandler(Handler):
    def handle_request(self, value, category):
        if category == "username":
            print(f"Обработка username: {value}")
        else:
            super().handle_request(value, category)


class ErrorHandler(Handler):
    def handle_request(self, value, category):
        print(f"Ошибка: Неизвестная категория ({category}): {value}")
