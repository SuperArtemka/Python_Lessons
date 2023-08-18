n = int(input())
arbuz = int(input('Вес первого арбуза'))
max = arbuz
min = arbuz
for _ in range(n-1):
    arbuz = int(input('Вес арбуза'))
if arbuz > max:
    max = arbuz
if arbuz < min:
    min = arbuz
print (F'{max} {min}')