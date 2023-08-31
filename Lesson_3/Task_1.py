# Список
list_1 = [1, 2, 6, 2, 5, 2,] 
count = 0
for i in range(len(list_1)):
    if list_1[i] not in list_1[:i]:
        count += 1
print(count)

# list_1 = set(list_1)
# print(len(list_1))