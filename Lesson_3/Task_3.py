all_dicts = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, \
{"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]

all_vals = []

for small_dict in all_dicts:
    for val in small_dict.values():
        if val not in all_vals:
            all_vals.append(val)

print(all_vals)