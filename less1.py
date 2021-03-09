# 1

a = 2
b = 5
c = 15

print(a + b)
print(b - c)
print(c / b**a)

d = int(input("Введите число от 0 до 9: "))
e = input("Введите ваше имя: ")
print("Ваше число", "-", d)
print("Ваше имя", "-", e)

# 2
sec_inp = int(input("Введите время в секундах: "))
hour = sec_inp // 3600
min = sec_inp//60 - hour*60
sec = sec_inp % 60

print(f"time: {hour:2d}:{min:2d}:{sec:2d}")

# 3
n = input("Введите число: ")
nn = n + n
nnn = n + n + n
sum = int(n) + int(nn) + int(nnn)
print(n)
print(nn)
print(nnn)
print(sum)

# 4.1 
a = int(input("Введите число: "))
m = 0
b = a
if a > 0:
    while b % 10 != 0:
        b -= 1
    n1 = a - b
    while b % 100 != 0:
        b -= 10
    n2 = (a-b) // 10
    while b % 1000 != 0:
        b -= 100
    n3 = (a-b) // 100
    n4 = (a - int(str(n3)+str(n2)+str(n1))) // 1000
    m = n1
    if n2 > m:
        m = n2
    if n3 > m:
        m = n3
    if n4 > m:
        m = n4
    print("Максимальная цифра в числе -", m)

#4.2
a = input("Введите число: ")
a_list = list(a)
print(f"Максимальная цифра в числе - {max(a_list)}")

# 5
vir = float(input("Введите выручку фирмы: "))
izd = float(input("Введите издежки фирмы: "))
if vir > izd:
    print(f"Фирма работает в прибыль, доход составляет {vir - izd:.2f}")
    print(f"Рентабельность выручки сосотавила {(vir-izd) / vir:.2f}")
    staf = int(input("Введите число сотрудников фирмы: "))
    print(f"Прибыль фирмы в расчёте на одного сотрудника составила"
          f" {(vir-izd) / staf:.2f}")
else:
    print(f"Фирма работает в убыток, расход составляет {vir - izd:.2f}")

# 6.1
print("Результаты тренировок")
dist_original = float(input("Дистанция пробежки в первый день"
                            "тренировок: "))
day_fin = int(input("День последней тренировки: "))
day = 1
dist_now = dist_original  # Дистанция в первый день
while day < day_fin:
    dist_now = dist_now * 1.1
    day += 1
print(f"Финальная дистаниция пробежки составила {dist_now:.2f} м")

# 6.2
print("Результаты тренировок")
dist_original = float(input("Дистанция пробежки в первый день"
                            "тренировок: "))
dist_fin = float(input("Дистанция пробежки: "))
dist_now = dist_original  # Дистанция в первый день
day = 1
while dist_now < dist_fin:
    dist_now = dist_now * 1.1
    day += 1
print(f"Заданная дистанция пробежки будет выполнена через {day} дней")
