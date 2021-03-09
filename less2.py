import math
import random

"""
#1
a_list = [1, "сутл", 3.9, "cucumber", 32, 45.1, True]
for el in a_list:
    print(type(el))

#2
b_list = list(input("Введите список "))
print(b_list)
i = 0
for el in b_list:
    if i < len(b_list)-1:
        b_list[i], b_list[i+1] = b_list[i+1], b_list[i]
    i += 2
print(b_list)

#3.1
n_month = int(input("Введите номер месяца "))
month = ["Зима", "Весна", "Лето", "Осень"]
if 2 < n_month < 6:
     print(month[1])
elif 5 < n_month < 9:
     print(month[2])
elif 8 < n_month < 12:
     print(month[3])
else:
    print(month[0])

#3.2
n_month = int(input("Введите номер месяца "))
m_dict = {1: 'Зима', 2: 'Зима', 3: 'Весна', 4: 'Весна', 5: 'Весна',
          6: 'Лето', 7: 'Лето', 8: 'Лето', 9: 'Осень', 10: 'Осень',
          11: 'Осень', 12: 'Зима'}
keys = m_dict.keys()
for el in keys:
    if el == n_month:
        print(m_dict.get(el))

#4
string = input("Введите строку ").split()
for ind, el in enumerate(string, 1):
    print(f"{ind}: {el[:10]}")

#5.1
my_list = [7, 5, 3, 3, 2]
#new_list = my_list
reit = int(input("Введите элемент рейтинга "))
if reit > max(my_list):
    my_list.insert(0, reit)
elif reit < min(my_list) or reit == min(my_list):
    my_list.append(reit)
else:
    new_list = my_list[1:-1]
    if reit > max(new_list) or reit == max(new_list):
        my_list.insert(1, reit)
    elif reit < min(new_list) or reit == min(new_list):
        my_list.insert(-2, reit)
    else:
        new_list = my_list[2:-2]
        if reit > max(new_list) or reit == max(new_list):
            my_list.insert(2, reit)
        elif reit < min(new_list) or reit == min(new_list):
            my_list.insert(-3, reit)

print(my_list)

#5.2
my_list = [7, 5, 3, 3, 2]
reit = int(input("Введите элемент рейтинга "))
my_list.append(reit)
my_list.sort(reverse=True)
print(my_list)

#6
n = int(input("Сколько позиций товара хотите внести? "))
i = 1
product_list = []
name_list = []
cost_list = []
count_list = []
sht_list = []
while i <= n:
    my_dict = {"название": input("Название "), "цена": input("Цена "),
               "количество": input("Количество "), "ед": "шт"}
    product = (i, my_dict)
    product_list.append(product)
    i += 1
print(product_list)
for el in product_list:
    for d in el:
        if type(d) == dict:
            for key, value in d.items():
                if key == "название":
                    name_list.append(value)
                elif key == "цена":
                    cost_list.append(value)
                elif key == "количество":
                    count_list.append(value)
                elif key == "ед":
                    sht_list.append(value)
                    sht_list = list(set(sht_list))
sort_dict = {"название": name_list, "цена": cost_list,
             "количество": count_list, "ед": sht_list}
print(sort_dict)

#7.1
fruit_list = ["яблоки", "груши", "апельсины", "бананы"]
for ind, el in enumerate(fruit_list, 1):
    print(f"{ind}: {el:>10}")

#7.2
one_list = [3, 1, 5, 9, 12, 22, 24, 11]
two_list = [1, 3, 5, 4, 13, 22, 24, 9]
for el in two_list:
    for i in one_list:
        if el == i:
            one_list.remove(i)
print(one_list)

#7.3
my_list = [1, 4, 9, 11, 18, 24, 31, 32]
new_list = []
for el in my_list:
    if el % 2 == 0:
        i = el / 4
        new_list.append(i)
    else:
        i = el * 2
        new_list.append(i)
print(new_list)

#8.1
my_list = [2, -5, 9, -25, 25, 4, 6, 49, -27, 121]
new_list = []
for el in my_list:
    if el > 0 and math.sqrt(el) % 1 == 0:
        i = int(math.sqrt(el))
        new_list.append(i)
print(new_list)

#8.2
day_dict = {1: "первое", 2: "второе", 3: "третье", 4: "четвёртое",
            5: "пятое", 6: "шестое", 7: "седьмое", 8: "восьмое",
            9: "девятое", 10: "десятое", 11: "одиннадцатое",
            12: "двеннадцатое", 13: "триннадцатое",
            14: "черырнадцатое", 15: "пятнадцатое",
            16: "шестнадцатое", 17: "семнадцатое",
            18: "восемнадцатое", 19: "девятнадцатое",
            20: "двадцатое", 21: "двадцать первое",
            22: "двадцать второе", 23: "двадцать третье",
            24: "двадцать четвёртое", 25: "двадцать пятое",
            26: "двадцать шестое", 27: "двадцать седьмое",
            28: "двадцать восьмое", 29: "двадцать девятое",
            30: "тридцатое", 31: "тридцать первое"}
month_dict = {1: "января", 2: "февраля", 3: "марта", 4: "апреля",
              5: "мая", 6: "июня", 7: "июля", 8: "августа",
              9: "сентября", 10: "октября", 11: "ноября",
              12: "декабря"}
data = input("Введите дату в формате dd.mm.yyyy ").split(".")
day_str = ""
month_str = ""
day = int(data[0])
month = int(data[1])
year = data[2]
for key, value in day_dict.items():
    if day == key:
        day_str = value
for key, value in month_dict.items():
    if month == key:
        month_str = value
print(f"{day_str} {month_str} {year} года")

#8.3
n = int(input("Введите количество элементов в списке "))
my_list = []
i = 0
while i < n:
    el = random.randint(-100, 100)
    my_list.append(el)
    i += 1
print(my_list)

#8.4
my_list = [1, 2, 1, 2, 5, 4, 0, 9, 9, 9, 4, 7]
new_list = list(set(my_list))
print(new_list)

new_list2 = []
for el in my_list:
    if el not in new_list2:
        new_list2.append(el)
print(new_list2)

new_list3 = []
for el in my_list:
    if my_list.count(el) == 1:
        new_list3.append(el)
print(new_list3)

#9.1
equation = "y = -12x + 11111140.2121"
x = 2.5
equation_list = list(equation.split())
el = equation_list[2]
el = float(el[:3])
num = float(equation_list[4])
y = el*x + num
print(f"y = {y}")

#9.2
import sys
date = input("Введите дату в формате дд.мм.гггг: ")
if date.find('.') == 2 and date.find('.', 3) == 5 and len(date) == 10:
    print("Длина введённой даты соответствует правилам ввода.")
else:
    print("При вводе была допущена ошибка.")
    sys.exit()
numberDay = int(date[:2])
numberMonth = int(date[3:5])
numberYear = int(date[6:])

if 0 < numberDay <= 31 and 0 < numberMonth <= 12 and 0 < numberYear <= 9999:
    print("Параметры даты соблюдены.")
else:
    print("При вводе числовых параметров даты была допущена ошибка.")

#9.3
N = random.randint(1, 2000000000)
sum_room = 0
block_floor = 0
top_floor = 0
while N - sum_room > 0:
    block_floor += 1
    sum_room = sum_room + block_floor**2
    top_floor = top_floor + block_floor
r_end = abs(N-sum_room)
floor = top_floor - r_end//block_floor
room_left = block_floor - round((r_end/block_floor - r_end//block_floor)
 * block_floor)
print(f"Квартира {N} находится на {floor} этаже, {room_left} слева")
"""
