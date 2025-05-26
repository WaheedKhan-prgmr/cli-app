class Habit:
    def __init__(self, name, frequency):
        self.name = name
        self.frequency = frequency  # 'daily', 'weekly', etc.
        self.progress = 0

    def mark_done(self):
        self.progress += 1

    def display_status(self):
        print(f"Habit: {self.name} | Frequency: {self.frequency} | Progress: {self.progress}")
