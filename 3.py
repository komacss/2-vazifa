class BankAccount:
    def __init__(self, owner, balance, card_number):
        self.owner = owner
        self.balance = balance
        self.__card_number = card_number

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, qiymat):
        if qiymat < 0:
            raise ValueError("Balans manfiy bo'lmasligi kerak!")
        self._balance = qiymat

    def __str__(self):
        return f"Hisob egasi: {self.owner}, balans: {self._balance}"

    def __repr__(self):
        return f"BankAccount(owner='{self.owner}', balance={self._balance}, card_number='{self.__card_number}')"


hisob1 = BankAccount("Ali", 1000, "8600123412341234")
hisob2 = BankAccount("Vali", 2500, "8600987698769876")

print(hisob1)
print(hisob2)
print(repr(hisob1))
print(repr(hisob2))

hisob1.balance = 1500
print(hisob1.balance)

hisob2.balance = 0
print(hisob2.balance)

try:
    hisob1.balance = -200
except ValueError as xato:
    print("Xato:", xato)

print(hisob1)

try:
    print(hisob2.__card_number)
except AttributeError as xato:
    print("Xato:", xato)