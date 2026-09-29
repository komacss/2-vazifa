class Product:
    def __init__(self, name, category, price):
        self.name = name
        self._category = category
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, qiymat):
        if qiymat <= 0:
            raise ValueError("Narx 0 dan katta bo'lishi kerak!")
        self.__price = qiymat

    def __str__(self):
        return f"Mahsulot: {self.name}, turkumi: {self._category}, narxi: {self.__price}"

    def __repr__(self):
        return f"Product(name='{self.name}', category='{self._category}', price={self.__price})"


mahsulot1 = Product("Olma", "Meva", 12000)
mahsulot2 = Product("Sut", "Ichimlik", 9000)
mahsulot3 = Product("Non", "Un mahsuloti", 4000)

print(mahsulot1)
print(mahsulot2)
print(mahsulot3)

print(repr(mahsulot1))
print(repr(mahsulot2))
print(repr(mahsulot3))

mahsulot1.name = "Qizil olma"
print(mahsulot1.name)

mahsulot2.price = 10000
print(mahsulot2.price)

try:
    mahsulot3.price = 0
except ValueError as xato:
    print("Xato:", xato)

try:
    mahsulot3.price = -500
except ValueError as xato:
    print("Xato:", xato)

print(mahsulot3)

try:
    print(mahsulot1.__price)
except AttributeError as xato:
    print("Xato:", xato)