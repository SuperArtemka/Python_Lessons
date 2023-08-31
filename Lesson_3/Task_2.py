my_list = [1, 2, 3, 4, 5]
print(my_list)

k = int(input('На сколько позиций сдвигать числа  -> '))

for _ in range(k):
    last_item = my_list.pop()
    my_list.insert(0, last_item)


# my_list = [1, 2, 3, 4, 5]

# k = int(input('-> '))
# k %= len(my_list)

# print(my_list[-k:] + [-k:])