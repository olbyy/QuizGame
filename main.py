class User:
    def __init__(self):
        self.name = "Tony"

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

user_1 = User()
print(user_1.get_name())
user_1.set_name("Mike")
print(user_1.get_name())
