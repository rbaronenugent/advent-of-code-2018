# define functions
def cumsum(list_):
    sum_ = 0
    clist = []
    for i in list_:
        clist.append(i + sum_)
        sum_ += i
    return clist


# load data
with open("input.txt") as input_file:
    lines = input_file.readlines()
lines = [int(i.split('\n')[0]) for i in lines]

# part 1
sum_ = sum(lines)
print sum_


# part 2
cum_values = cumsum(lines)

starting_value = 0
c = {0: 1}
while max(c.values()) <= 1:
    sum_list = [i + starting_value for i in cum_values]

    for entry in sum_list:
        if entry in c:
            c[entry] += 1
            print entry
            break
        else:
            c[entry] = 1

    starting_value = sum_list[-1]
