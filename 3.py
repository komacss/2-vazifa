class BankHisobi:
    def __init__(self, egasi, balans, karta_raqami):
        self.egasi = egasi
        self._balans = balans
        self.__karta_raqami = karta_raqami

    @property
    def balans(self):
        return self._balans

    @balans.setter
    def balans(self, yangi_balans):
        if yangi_balans >= 0:
            self._balans = yangi_balans
        else:
            print("Balans manfiy bo'lishi mumkin emas")

    def __str__(self):
        return f"Egasi: {self.egasi}\nBalans: {self._balans}"

    def __repr__(self):
        return f"BankHisobi('{self.egasi}', {self._balans})"


hisob_1 = BankHisobi("Muhiddin Solijonov", 5000000, "1234 5678 5424 7985")
hisob_2 = BankHisobi("Sobirov Sobir", 440000, "7866 6744 7968 4586")

print(hisob_1.balans)

yangi_balans = int(input("Yangi balans: "))
hisob_1.balans = yangi_balans

print(hisob_1)
print(repr(hisob_1))
