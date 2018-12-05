import numpy as np

# party 1
with open("input.csv") as input_file:
    lines = input_file.readlines()
sum_ = sum([int(i.split('\n')[0]) for i in lines])
print sum_


# part 2
value_list = [float(i.split('\n')[0]) for i in lines]
cum_values = np.cumsum(value_list)

starting_value = 0
c = {0: 1}
while max(c.values()) <= 1:
    sum_list = (cum_values + starting_value).astype('int')

    for entry in sum_list:
        if entry in c:
            c[entry] += 1
            print entry
            break
        else:
            c[entry] = 1

    starting_value = sum_list[-1]
