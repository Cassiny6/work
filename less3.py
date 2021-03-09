"""
def new_func(a, b):
    return a + b


print(new_func(2, 6))

my_func = lambda p_1, p_2: p_1 + p_2
print(my_func(2, 5))

seasons = lambda **kwargs: kwargs
print(seasons(el1="зима", el2="весна", el3="лето", el4="осень"))

print(ord("*"))
print(chr(945))
print(divmod(3, 4))


del_func = lambda a_1, a_2: divmod(a_1, a_2)
#def del_func(a_1, a_2):
#    return divmod(a_1, a_2)


a_1 = int(input("Введите числитель "))
a_2 = int(input("Введите знаменатель "))
print(f"{del_func(a_1, a_2)[0]} {del_func(a_1, a_2)[1]}/{a_2}")

iter_obj = "яzаdоlиyа"
print(max(iter_obj), min(iter_obj))

print(list(range(5, 0, -1)))
print(list(range(0, 5)))
"""

# 1
'''
def cha(n_1=1, n_2=1):
    """Деление двух чисел

    n_1 и n_2 - делимое и делитель, задаются пользователем
    если n_2 = 0, обрабатывается исключение и выводится сообщение

    """
    try:
        n_1 = float(input("Введите делимое "))
        n_2 = float(input("Введите делитель "))
        n = n_1 / n_2
    except ZeroDivisionError:
        return "Деление на ноль"
    return n


print(cha())

#2
def user_data(data):
    name = input("Ваше имя ")
    surname = input("Ваша фамилия ")
    born = input("Дата рождения ")
    city = input("Город проживания ")
    email = input("E-mail адрес ")
    phone = input("Номер телефора ")
    data = f"{name} {surname} {born} {city} {email} {phone}"
    return data


print(f"Данные пользователя: {user_data('data')}")

#3
def my_func(a=10, b=22, c=11):
    s = 0
    arg = (a, b, c)
    for el in arg:
        if el > min(arg):
            s = s + el
    return s


print(my_func())

#4
def my_func(x, y):
    up = x ** y
    return up


def power(x, y):
    up = 1
    for i in range(0, abs(y)):
        up *= x
    if y < 0:
        up = 1 / up
    return up


print(my_func(2.1, 2))
print(power(2.1, 2))

#5
def str_numbers(*args):
    numbers = input("Введите числа ").split()
    sum_num = 0
    for el in numbers:
        if el == 'q':
            break
        else:
            sum_num += int(el)
    return sum_num


sum_num = str_numbers()
answer = ''
print(sum_num)
while answer != 'q':
    answer = input("Продолжить ввод чисел? ")
    if answer == 'y':
        sum_num += str_numbers()
        print(sum_num)
print(f"Сумма чисел: {sum_num}")

#6
def int_func():
    word = input("Введите слово ")
    return word.title()


print(int_func())

# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    if number[ndigits+2] < 0.4:
        number = number[ndigits+1]
    return number
    #return round(number, ndigits)


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))
print(my_round(2.2548153, 5))

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    first_sum = 0
    second_sum = 0
    first_number = str(ticket_number)[:3]
    second_number = str(ticket_number)[3:]
    for i in first_number:
        first_sum = first_sum + int(i)
    for i in second_number:
        second_sum = second_sum + int(i)
    if first_sum == second_sum:
        return "счастливый билет"
    else:
        return "не счастливый билет"


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
'''
'''
# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    pass
'''
'''
# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    sort_list = []
    n = 0
    while n <= len(origin_list):
        n = 0
        for el in origin_list:
            if el == min(origin_list):
                sort_list.append(el)
                origin_list.remove(el)
        n += 1
    return sort_list

sort_list = sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])
print(sort_list)

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def my_filter(content, flag):
    filter_list = []
    for el in content:
        if el == flag:
            filter_list.append(el)
    return filter_list

a = "Курица лапой буквы писала".split()
b = "лапой"
c = my_filter(a, b)
print(c)

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
import math

def parallelogramm(A1, A2, A3, A4):
    A1A2 = math.sqrt(pow(abs(A2[0] - A1[0]), 2) + pow(abs(A2[1] - A1[1]), 2))
    A3A4 = math.sqrt(pow(abs(A4[0] - A3[0]), 2) + pow(abs(A4[1] - A3[1]), 2))
    A1A3 = math.sqrt(pow(abs(A3[0] - A1[0]), 2) + pow(abs(A3[1] - A1[1]), 2))
    A2A4 = math.sqrt(pow(abs(A4[0] - A2[0]), 2) + pow(abs(A4[1] - A2[1]), 2))
    if A1A2 == A3A4 and A1A3 == A2A4:
        return f"Точки с координатами {A1}, {A2}, {A3}, {A4}" \
               f" - вершины параллелограмма"
    else:
        return f"Точки с координатами {A1}, {A2}, {A3}, {A4}" \
               f" не являются вершинами параллелограмма"

A1 = (1, 4)
A2 = (5, 4)
A3 = (2, 1)
A4 = (6, 1)
print(parallelogramm(A1, A2, A3, A4))
'''
