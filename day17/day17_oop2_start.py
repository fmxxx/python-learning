class User:
    def __init__(self, user_id, user_name) -> None:
        self.id = user_id
        self.user_name = user_name
        self.followers = 0
        self.following = 0

    def follow(self, user_to_follow):
        user_to_follow.followers += 1
        self.following += 1


user_1 = User("000.000.000.001", "Jeff")
user_2 = User("000.000.000.002", "Bob")


user_1.follow(user_2)

print(f"{user_1.id} - {user_1.user_name} - {user_1.followers} followers")
print(f"{user_2.id} - {user_2.user_name} - {user_2.followers} followers")
