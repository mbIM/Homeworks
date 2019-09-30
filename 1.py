n = int(input("Введите число n = "))

def factorial():
    if n == 0:
        return 1

    return (n-1) * n

print("Факториал от n =2", factorial())