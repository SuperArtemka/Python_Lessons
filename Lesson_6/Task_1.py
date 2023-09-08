# Пересекающиеся элементы списков

# def func(my_list, yours_list):
#     answer = list()
#     for value in my_list:
#         if value not in yours_list:
#             answer.append(value)
#     return answer


# first = int(input("Введите количество элементов первого множества: "))
# my_list = list()

# for i in range(first):
#     value = int(input("Введите элемент первого множества: "))
#     my_list.append(value)

# second = int(input("Введите количество элементов второго множества: "))
# yours_list = list()

# for i in range(second):
#     value = int(input("Введите элемент второго множества: "))
#     yours_list.append(value)

# print(func(my_list, yours_list))

def func(my_list, yours_list):
    answer = list()
    for value in my_list:
        if value not in yours_list:
            answer.append(value)
        return answer

def generation(m):
    my_list = list()
    for i in range(m):
        value = int(input("Введите элемент первого множества: "))
        my_list.append(value)
    return my_list


m = int(input("Введите количество элементов первого множества: "))
my_list = generation(m)

k = int(input("Введите количество элементов второго множества: "))
yours_list = generation(k)