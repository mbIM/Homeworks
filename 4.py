import numpy as np
import random


a = np.random.randint(1, 10, 5)

b = np.random.randint(1, 10, 5)

for i in range (0, 5):
    if a[i] == b[i]:
        print ("Числа общие для двух массивов: ", a[i] == b[i], a[i])