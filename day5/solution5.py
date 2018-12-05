with open("input.txt") as input_file:
    lines = input_file.readlines()
code = [i.split('\n')[0] for i in lines][0]


def reduce_polymer(polymer):
    i = 1
    while i < len(polymer):
        current_letter = polymer[i]
        previous_letter = polymer[i - 1]
        if current_letter != previous_letter and current_letter.lower() == previous_letter.lower():
            polymer = polymer[:i - 1] + polymer[i + 1:]
            i -= 1
            i = max(i, 1)
        else:
            i += 1
    return polymer, len(polymer)


# part 1
new_code, new_length = reduce_polymer(code)
print new_length


# part 2
reduce_list = []
for letter in 'abcdefghijklmnopqrstuvwyxz':
    reduced_polymer = ''.join([i for i in code if i.lower() != letter])
    reduce_list.append((reduce_polymer(reduced_polymer)[1], letter))
reduce_list = sorted(reduce_list)
print reduce_list[0][0]
