
# Задание 1 : Сумма ряда 0-100

from numpy import array, mean
x = sum(array(range(100)))
print (x)

# Задание 2 : Сумма ряда 0-input()

from numpy import array, mean
y = input("Введите число, до которого надо посчитать сумму ряда с 0:")
x = sum(array(range(int(y))))
print (x)

# Задание 3 : Среднее среди 100 случайных чисел

from numpy import mean
import numpy as np
x= np.random.random_integers(0, 10, 100)
y = mean(x)
print (y)