class ChatUser:
    """Пользователь"""
    def __init__(self, name):
        self.name = name

    def join_chat(self, mediator):
        # Пользователь присоединяется к чату
        mediator.add_user(self)

    def send(self, message, target_chat):
        # Пользователь отправляет сообщение в указанный чат
        print(f"{self.name} sent message ({message}) to {target_chat.name}")
        target_chat.send_message(f"{self.name}: {message}", self)

    def receive(self, message):
        # Пользователь принимает сообщение
        print(f"{self.name} received message ({message})")


class Teacher(ChatUser):
    """Учитель"""


class Student(ChatUser):
    """Студент"""
