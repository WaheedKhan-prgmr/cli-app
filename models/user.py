class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.habits = []

    def add_habit(self, habit):
        self.habits.append(habit)

    def show_progress(self):
        for habit in self.habits:
            habit.display_status()
