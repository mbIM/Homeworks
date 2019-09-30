import numpy as np
import random

n = int(input("Введите число n = "))

a = np.random.randint(1, n , 5)
b = [i**2 for i in a]

print(b)