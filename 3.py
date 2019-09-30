import numpy as np
import random

n = int(input("Введите число n = "))

a = np.random.randint(1, 10, 5)

for i in range (0, 5):
    if n > a[i]:
        print ("Все числа меньше вводимого n: ", a[i] < n, a[i])
    else:
        print ("Таких чисел нет")