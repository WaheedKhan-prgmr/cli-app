from abc import ABC, abstractmethod

class Notifier(ABC):
    @abstractmethod
    def notify(self, user, message):
        pass

class EmailNotifier(Notifier):
    def notify(self, user, message):
        print(f"Sending email to {user.email}: {message}")

class ConsoleNotifier(Notifier):
    def notify(self, user, message):
        print(f"[NOTIFY] {user.username}: {message}")
