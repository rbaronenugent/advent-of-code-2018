def bincount(string):
    d = {}
    for letter in string:
        if letter in d:
            d[letter] += 1
        else:
            d[letter] = 1
    return d


def product(tup):
    p = 1
    for i in tup:
        p *= i
    return p


def character_diff(str1, str2):
    diff = 0
    common_letters = ''
    for c1, c2 in zip(str1, str2):
        if c1 != c2:
            diff += 1
        else:
            common_letters += c1
    return diff, common_letters


# part 1
with open("input.csv") as input_file:
    lines = input_file.readlines()
lines = [i.split('\n')[0] for i in lines]

multiple_dict = {}
for entry in lines:
    d_ = bincount(entry)
    already_added_vals = []
    for key, val in d_.items():
        if val in multiple_dict and val not in already_added_vals:
            multiple_dict[val] += 1
            already_added_vals.append(val)
        elif val not in already_added_vals:
            multiple_dict[val] = 1
            already_added_vals.append(val)

checksum = 1
for key, val in multiple_dict.items():
    if key != 1:
        checksum *= val
print checksum


# part 2
min_diff = len(lines[0])
min_common_letters = ''
first_id = ''
second_id = ''
for i, entry1 in enumerate(lines):
    for entry2 in lines[i + 1:]:
        diff, common_letters = character_diff(entry1, entry2)
        if diff == 1:
            min_diff = diff
            min_common_letters = common_letters
            first_id = entry1
            second_id = entry2
            print min_diff, min_common_letters, first_id, second_id
