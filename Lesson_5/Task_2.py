# Замена чисел минимальных на максимальные

m = list(map(int, input().split()))
# n = [1, 3, 3, 3, 4]
# print(n)

def func(n):
    maxx = max(m)
    minn = min(m)
    for i in range(len(m)):
        if n[i] == maxx:
            n[i] = minn
    return n
print(func(m))
 
#def grade(n=[]):
# max_1 = max(n)
# min_1 = min(n)

# for i in range(len(n)):
# if n[i] == max_1:
# n[i] = min_1
# return (n)

# print(grade(n=[1,3,3,3,4])) 