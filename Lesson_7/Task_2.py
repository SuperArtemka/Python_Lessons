# Поиск максимальной орбиты
def max_orbit(my_list):
    maxx = [(i[0] * i[1]) if (i[0] != i[1]) else 0 for i in my_list]
    return my_list[maxx.index(max(maxx))]

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(max_orbit(orbits))

# def max_orbit(my_list):
# # (1, 3)
#     s_orbits = [(x_1*x_2 if x_1 != x_2 else 0) for x_1, x_2 in my_list]
#     return my_list[s_orbits.index(max(s_orbits))]

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(max_orbit(orbits))