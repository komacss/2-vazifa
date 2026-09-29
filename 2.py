class Employee:
    def __init__(self, name, salary, employee_id):
        self.name = name
        self.salary = salary
        self.__employee_id = employee_id

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, qiymat):
        if qiymat < 0:
            raise ValueError("Maosh 0 dan kichik bo'lmasligi kerak!")
        self._salary = qiymat

    def __str__(self):
        return f"Xodim: {self.name}, maosh: {self._salary}"

    def __repr__(self):
        return f"Employee(name='{self.name}', salary={self._salary}, employee_id={self.__employee_id})"


xodim1 = Employee("Ali", 5000, 101)
xodim2 = Employee("Vali", 7000, 102)
xodim3 = Employee("Sardor", 6000, 103)

print(xodim1)
print(xodim2)
print(xodim3)

print(repr(xodim1))
print(repr(xodim2))
print(repr(xodim3))

xodim1.name = "Aliyev"
print(xodim1.name)

xodim2.salary = 8000
print(xodim2.salary)
try:
    xodim2.salary = -100
except ValueError as xato:
    print("Xato:", xato)

try:
    print(xodim3.__employee_id)
except AttributeError as xato:
    print("Xato:", xato)

print(xodim3._Employee__employee_id)