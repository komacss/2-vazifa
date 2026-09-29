class Xodim:
    def __init__(self, ism, maosh, xodim_id):
        self.ism = ism
        self._maosh = maosh
        self.__xodim_id = xodim_id

    @property
    def maosh(self):
        return self._maosh

    @maosh.setter
    def maosh(self, yangi_maosh):
        if yangi_maosh > 0:
            self._maosh = yangi_maosh
            print("Maosh muvaffaqiyatli o'zgartirildi")
        else:
            print("Xato: maosh 0 dan katta bo'lishi kerak")

    def __str__(self):
        return f"ID: {self.__xodim_id}, Ism: {self.ism}"


xodim_1 = Xodim(ism="Sobir", maosh=5000, xodim_id=1)

print(xodim_1.maosh)

yangi_maosh = int(input("Yangi maosh: "))
xodim_1.maosh = yangi_maosh

print(xodim_1)
