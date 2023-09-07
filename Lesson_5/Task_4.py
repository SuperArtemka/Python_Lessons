# Поменять числа местами не используя списков
def revers_(n):
    number = input()
    if n != 1:
        revers_(n - 1)
    print(number, end=' ')

n = int(input())

revers_(n)

#  def revers_(n):
# number = input()
# if n == 1:
# return number
# return revers_(n - 1) + ' ' + number

# n = int(input())

# print(revers_(n))