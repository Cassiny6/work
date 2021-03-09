# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной
# платы сотрудника. В расчете необходимо использовать формулу: (выработка в часах*ставка в
# час) + премия. Для выполнения расчета для конкретных значений необходимо запускать
# скрипт с параметрами.
'''
from sys import argv

name, virab, stavka, prem = argv


def zp():
    income = int(virab)*int(stavka) + int(prem)
    return income


print(f"Название {name}")
print(f"Выработка {virab}")
print(f"Ставка {stavka}")
print(f"Премия {prem}")
print(f"Зарплата сотрудника {zp()}")
'''
# 2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения
# которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для
# формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].
'''
in_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [j for i, j in zip(in_list, in_list[1:]) if j > i]
print(new_list)
'''
# 3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
# Необходимо решить задание в одну строку.
# Подсказка: использовать функцию range() и генератор.
'''
crat = [el for el in range(20, 120) if el % 20 == 0 or el % 21 == 0]
print(crat)
'''
# 4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке.
# Для выполнения задания обязательно использовать генератор.
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]
'''
ish_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
set_list = [el for el in ish_list if ish_list.count(el) == 1]
print(set_list)
'''
# 5. Реализовать формирование списка, используя функцию range() и возможности
# генератора. В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().
'''
from functools import reduce

def chet():
    chet_list = [el for el in range(100, 1001) if el % 2 == 0]
    return chet_list

def my_func(prev_el, el):
    return prev_el * el


print(reduce(my_func, chet()))
'''
# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении
# числа 10 завершаем цикл. Во втором также необходимо предусмотреть условие,
# при котором повторение элементов списка будет прекращено.
'''
from sys import argv
from itertools import cycle, count, repeat, chain

name, min_el, max_el, stop = argv

for el in count(int(min_el)):
    if el > int(max_el):
        break
    else:
        print(el)

some_list = [1, 5, 'f', 'd', 10, 9, 'qw']
c = 1
for el in cycle(some_list):
    if c > int(stop):
        break
    some_list.append(el)
    c += 1
print(some_list)

some_list = [1, 5, 'f', 'd', 10, 9, 'qw']
res = list(chain.from_iterable(repeat(i, int(stop)) for i in some_list))
print(res)
'''
# 7. Реализовать генератор с помощью функции с ключевым словом yield,
# создающим очередное значение. При вызове функции должен создаваться
# объект-генератор. Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить
# только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n.
# Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
'''
from functools import reduce
from itertools import count


def mult(prev_el, el):
    return prev_el * el

def fact(n):
    for el in count(1):
        if el > n:
            break
        else:
            nums = [el for el in range(1, el + 1)]
            yield reduce(mult, nums)


for el in fact(5):
    print(el)
'''
# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]
'''
my_list = [1, 2, 4, 0, -4, -2, 5]
new_list = [el**2 for el in my_list]
print(new_list)
'''
# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.
'''
fruit_list1 = ["яблоко", "апельсин", "банан", "помело"]
fruit_list2 = ["грейпфрут", "груша", "банан", "гранат", "персик", "яблоко", "помело"]
fruit_list_s = fruit_list1 + fruit_list2
fruit_list = [el for el in fruit_list_s if fruit_list_s.count(el) == 2]
print(set(fruit_list))
'''
# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4
'''
base_list = [1, 24, 11, 0, 64, 27, 81, -45, -12, 9, -6, 14, -3, 3]
new_list = [el for el in base_list if el % 3 == 0 and el > 0 and el % 4 != 0]
print(new_list)
'''
'''
import re

string = "This is a simple text message for text"
pattern_1 = "text"
print(re.match(pattern_1, string) is None)
print(re.search(pattern_1, string) is None)
found = re.findall('text', string)
print(found)

string = "If 300 spartans were so 10k siple 15k"
string_2 = "If 300 spartans were so 10-16C siple 4 - 9C"
pattern = '\d+k'
pattern_2 = '\d+ *- *\d+'
print(re.findall(pattern, string))
print(re.findall(pattern_2, string_2))

string = "1926-1234"
pattern = "926\D123"
print(re.findall(pattern, string))
'''
# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.

import re

line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNO'\
       'GIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzK'\
       'TUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqn'\
       'LxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIVjXa'\
       'pzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnWete'\
       'kUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfCvzQ'\
       'WrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXb'\
       'JrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCC'\
       'EUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfB'\
       'tQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuT'\
       'SkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCfKCu'\
       'UJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWHuXB'\
       'qHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFa'\
       'XiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQ'\
       'zTYwZAiRwycdlHfyHNGmkNqSwXUrxGc'

print(re.findall('[a-z]+', line))

# Задание-2:
# Вывести символы в верхнем регистре, слева от которых находятся
# два символа в нижнем регистре, а справа - два символа в верхнем регистре.
# Т.е. из строки
# "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
# нужно получить список строк: ['AY', 'NOGI', 'P']
# Решить задачу двумя способами: с помощью re и без.

print(re.findall('[a-z]{2}[A-Z]+[A-Z]{2}', line))