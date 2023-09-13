# Дружественные числа
def my_func(n):
    sum_dif = 0
    for i in range(1, n//2 + 1):
        if n % i == 0:
            sum_dif += i
    return sum_dif

k = 300
for i in range(1, k):
        n_1 = my_func(i)
        n_2 = my_func(n_1)
        if n_2 == i and n_1 != n_2 and n_2 < n_1:
            print(n_2, n_1)


# def get_summ(n):
# count = 0
# for i in range(1, n):
# if n % i == 0:
# count += i
# return count


# k = 300
# for num_1 in range(1, k):
# num_2 = get_summ(num_1)
# sum_del_num_2 = get_summ(num_2)

# if (num_1 == sum_del_num_2) and (num_1 != num_2) and (num_1 < num_2):
# print(num_1, num_2)            