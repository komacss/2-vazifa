class User:
    def __init__(self, name, age, password):
        self.name = name
        self.age = age
        self.password = password

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, qiymat):
        if qiymat < 0:
            raise ValueError("Yosh 0 dan kichik bo'lmasligi kerak!")
        self._age = qiymat

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, qiymat):
        if len(qiymat) < 6:
            raise ValueError("Parol kamida 6 ta belgidan iborat bo'lishi kerak!")
        self.__password = qiymat

    def __str__(self):
        return f"Foydalanuvchi: {self.name}, yoshi: {self._age}"

    def __repr__(self):
        return f"User(name='{self.name}', age={self._age})"


user1 = User("Ali", 20, "ali12345")
user2 = User("Vali", 25, "vali7890")

print(user1)
print(user2)
print(repr(user1))

user1.name = "Aliyev"
print(user1.name)

user2.age = 30
print(user2.age)
try:
    user2.age = -5
except ValueError as xato:
    print("Xato:", xato)

user1.password = "yangi_parol"
print(user1.password)
try:
    user1.password = "123"
except ValueError as xato:
    print("Xato:", xato)