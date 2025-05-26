from models.habit import Habit
from models.notifier import ConsoleNotifier
from models.premium_user import PremiumUser
from models.sphere import Sphere
from services.cli import display_menu

def main():
    notifier = ConsoleNotifier()
    user = PremiumUser("Waheed", "waheedkhan0fficial786@gmail.com", notifier)

    sphere = Sphere("Wellness Warriors")
    sphere.add_member(user)

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Habit name: ")
            freq = input("Frequency (daily/weekly): ")
            user.add_habit(Habit(name, freq))

        elif choice == "2":
            for i, habit in enumerate(user.habits):
                print(f"{i + 1}. {habit.name}")
            idx = int(input("Select habit to mark done: ")) - 1
            user.habits[idx].mark_done()

        elif choice == "3":
            sphere.share_progress()

        elif choice == "4":
            msg = input("Reminder message: ")
            user.send_reminder(msg)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
credits