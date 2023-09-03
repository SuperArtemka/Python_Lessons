# Подсчет букв словаря с выводом количества
start_str = 'a a a b c a a d c d d'.split()
print(start_str)

char_dict = {}
result_str = ''

for char in start_str:
    if char not in char_dict:
        char_dict[char] = 1
        result_str += f'{char} '
    else:
        result_str += f'{char}_{char_dict[char]} '
        char_dict[char] += 1

print(result_str)