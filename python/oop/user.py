class User:
    active_users = 0

    @classmethod
    def display_active_users(cls):
        return f'There are currently {cls.active_users} users active'

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1
    
    def logout(self):
        User.active_users -= 1
        return f'{self.first} has logged out'
    
    def full_name(self):
        return f'{self.first} {self.last}'
    
    def initials(self):
        return f'{self.first[0]} {self.last[0]}'

user_1 = User(first='Larry', last='James', age=34)

print(User.display_active_users())