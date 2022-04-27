import datetime
import time

# задание 1 Ввод, вывод данных
a = 12
b = 10
print(a)
print(b)
value1 = int(input("Введите число >>>"))
print(value1)
username = input("Введите Ваше имя >>>")
useryear = int(input("Введите год Вашего рождения >>>"))
now = datetime.datetime.now()
nowyear = now.year
userage = nowyear - useryear
print("Привет, {}! Тебе уже {} лет! и число, которое Вы ввели {}".format(username, userage, value1))

# задание 2 Перевод секунд в часы, минуты и секунды
sec = int(input("Введите количество секунд >>>"))
ty_res = time.gmtime(sec)
res = time.strftime("%H:%M:%S", ty_res)
print(res)

# задание 3 Преобразование числа
freevalue = int(input("Введите число для умножения и сложения >>>"))
resulttack = freevalue + (freevalue * 10 + freevalue) + (freevalue * 100 + freevalue * 10 + freevalue)
print(resulttack)

# задание 4 Найти самую большую цифру в числе
maxvalue = int(input("Введите число, что бы найти самую большую цифру в числе >>>"))
string = str(maxvalue)
ls = list(map(int, string))
mavval = max(ls)
print("Самая большая цифра в числе {}".format(mavval))

# задание 5 Прибыль и рентабельность организации
revenue = int(input("Введите выручку >>>"))
costs = int(input("Введите издержки >>>"))
if revenue > costs:
    print("Ваша организация работает с прибылью")
elif revenue == costs:
    print("Ваша организация работает без прибыли")
else:
    print("Ваша организация работает в убыток")

if revenue > costs:
    employees = int(input("Введите количество сотрудников >>>"))
    rent = round(float(revenue / costs), 2)
    procrent = round(rent * 100, 2)
    rentemployees = round(float(revenue / employees), 2)
    print(
        "Коэффициент рентабельности Вашей организации равен {} или {} процентов, "
        "а прибыль на одного сотрудника равна {}".format(rent, procrent, rentemployees))
else:
    print("Ваша организация работает в убыток или без прибыли")

# задание 6 День достижения желаемого результата спортсменом
numberofday = 1
startresult = 2
waitresult = 3

while True:
    if waitresult > startresult:
        numberofday = numberofday + 1
        startresult = startresult + startresult * 0.1
        continue
    print("День достижения результата {}". format(numberofday))
    break
