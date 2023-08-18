print('Введтите число')
a = int(input())

digit_1 = 0
digit_2 = 1
count = 2

while digit_2 < a:
    digit_1, digit_2 = digit_2, digit_1 + digit_2
    count += 1
if digit_2 == a:
    print(count)
else:
    print(-1)        