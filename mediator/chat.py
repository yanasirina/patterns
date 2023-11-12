class ChatMediator:
    """Посредник"""
    def __init__(self, name):
        self.name = name
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def send_message(self, message, sender):
        for user in self.users:
            # Посредник рассылает сообщения всем пользователям, кроме отправителя
            if user != sender:
                user.receive(message)
