#6. Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

a = int(input("Введите сколько хочешь киллометров?: "))
b = int(input("Введите сколько хочешь бы пробежать?: "))

day = 1

while a < b:
    a *= 1.1
    day += 1

print(f"Нужно потребуется {day}-й день, чтобы пробежать спортсмен результат не менее {b} км")