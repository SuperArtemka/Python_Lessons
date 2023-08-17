print('Введите число, факториал которого желаете найти:')
N = int(input())
i = 1
result = 1
while i <= N:
    result *= i
    i += 1
print(result)
