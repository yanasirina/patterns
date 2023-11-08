from handlers import ErrorHandler, EmailHandler, PhoneHandler, UsernameHandler
from utils import categorize_value


if __name__ == "__main__":
    error_handler = ErrorHandler()
    email_handler = EmailHandler(error_handler)
    phone_handler = PhoneHandler(email_handler)
    username_handler = UsernameHandler(phone_handler)

    values = ["john@example.com", "+79999999999", "@telegram_user", "123456"]

    for value in values:
        category = categorize_value(value)
        username_handler.handle_request(value, category)

    """Результат выполнения"""
    # Обработка электронной почты: john@example.com
    # Обработка телефона: +79999999999
    # Обработка username: @telegram_user
    # Ошибка: Неизвестная категория (unknown): 123456
