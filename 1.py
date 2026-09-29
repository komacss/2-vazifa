class Foydalanuvchi:
    def __init__(self, ism, yosh, parol):
        self.ism = ism
        self._yosh = yosh
        self.__parol = parol

    @property
    def yosh(self):
        return self._yosh

    @yosh.setter
    def yosh(self, yangi_yosh):
        if yangi_yosh >= 0:
            self._yosh = yangi_yosh
            print("Yosh o'zgartirildi")
        else:
            print("Yosh 0 dan kichik bo'lishi mumkin emas")

    @property
    def parol(self):
        return self.__parol

    @parol.setter
    def parol(self, parollar):
        eski_parol, yangi_parol = parollar

        if len(yangi_parol) >= 6 and self.__parol == eski_parol:
            self.__parol = yangi_parol
            print("Parol almashtirildi")
        else:
            print("Xatolik")

    def __str__(self):
        return f"Ism: {self.ism}, Yosh: {self.yosh}"

    def __repr__(self):
        return f"Foydalanuvchi('{self.ism}', {self.yosh})"


foydalanuvchi_1 = Foydalanuvchi("Sobir", 19, "12345678")
foydalanuvchi_2 = Foydalanuvchi("Ali", 20, "5432105")

print(foydalanuvchi_1)
print(repr(foydalanuvchi_1))
print(foydalanuvchi_1.yosh)

yangi_yosh = int(input("Yangi yoshni kiriting: "))
foydalanuvchi_1.yosh = yangi_yosh

eski_parol = input("Eski parolni kiriting: ")
yangi_parol = input("Yangi parolni kiriting: ")

foydalanuvchi_1.parol = eski_parol, yangi_parol
