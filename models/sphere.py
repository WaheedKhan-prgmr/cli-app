class Sphere:
    def __init__(self, name):
        self.name = name
        self.members = []

    def add_member(self, user):
        self.members.append(user)

    def share_progress(self):
        print(f"=== Sphere: {self.name} ===")
        for user in self.members:
            print(f"\n{user.username}'s Progress:")
            user.show_progress()
