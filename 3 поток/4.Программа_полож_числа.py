# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

def my_func(x,y):
    i1 = x ** y
    i2 = 1
    i = 1
    while i <= abs(y):
        i2 *= x
        i += 1
    return i1,1 / i2 

print(my_func(int(input("Возведение в степень: ")), int(input("Возведение в степень без оператора: "))))