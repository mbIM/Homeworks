def fibo(n = int(input("Введите число n = "))):

    if n == 1 or n == 2:
        return 1

    else:
        return fibo(n - 1) + fibo(n - 2)

print("Число Фибоначчи n =", fibo())