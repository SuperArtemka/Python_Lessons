# Все четные умножить на 3, все нечетные разделить на 5

print(list(map(lambda x: x / 5 if (x % 2) else x * 3, [1, 5, 8, 3, 6, 10])))