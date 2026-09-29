class Mahsulot:
    def __init__(self, nomi, kategoriya, narx):
        self.nomi = nomi
        self._kategoriya = kategoriya
        self.__narx = narx

    @property
    def narx(self):
        return self.__narx

    @narx.setter
    def narx(self, yangi_narx):
        if yangi_narx >= 0:
            self.__narx = yangi_narx
        else:
            print("Narx manfiy bo'lishi mumkin emas")


mahsulot = Mahsulot("Olma", "Meva", 5000)

print(mahsulot.nomi)
print(mahsulot.narx)

mahsulot.nomi = "Banan"
mahsulot.narx = 7000

print(mahsulot.nomi)
print(mahsulot.narx)
