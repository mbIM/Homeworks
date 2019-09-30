def factorial(n = int(input("Введите число n = "))):
    if n == 0:
        return 1

    return factorial(n-1) * n

print("Факториал от n =", factorial())