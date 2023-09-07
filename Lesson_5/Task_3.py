# Поиск простого числа

def func(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return 'целое'
        return 'простое'

n = int(input())
print(func(n))