from .user import User

class PremiumUser(User):
    def __init__(self, username, email, notifier):
        super().__init__(username, email)
        self.notifier = notifier

    def send_reminder(self, message):
        self.notifier.notify(self, message)
