with open("input.csv") as input_file:
    lines = input_file.readlines()
lines = [i.split('\n')[0] for i in lines]


# part 1
dates = [line.split('[')[1].split(']')[0] for line in lines]
sorted_dates = [i[0] for i in sorted(zip(lines, dates), key=lambda x: x[1])]

guard_sleep_dict = {}
for entry in sorted_dates:
    if 'Guard' in entry:
        current_guard = int(entry.split(' begins shift')[0].split('Guard #')[1])
        if current_guard not in guard_sleep_dict:
            guard_sleep_dict[current_guard] = [0 for i in xrange(60)]
    elif 'asleep' in entry:
        sleep_start = int(entry.split(']')[0].split(' ')[1].split(':')[1])
    elif 'wakes' in entry:
        sleep_end = int(entry.split(']')[0].split(' ')[1].split(':')[1])
        for ind in xrange(sleep_start, sleep_end):
            guard_sleep_dict[current_guard][ind] += 1

max_sleep_mins = 0
for guard, sleep_list in guard_sleep_dict.items():
    total_sleep_mins = sum(sleep_list)
    if total_sleep_mins > max_sleep_mins:
        sleepiest_guard = guard
        sleep_minutes = total_sleep_mins
        sleepiest_minute = max([ind if entry == max(sleep_list) else None for ind, entry in enumerate(sleep_list)])
        max_sleep_mins = total_sleep_mins
print sleepiest_guard * sleepiest_minute


# part 2
max_specific_min = 0
for guard, sleep_list in guard_sleep_dict.items():
    most_common_min = max(sleep_list)
    if most_common_min > max_specific_min:
        most_consistent_guard = guard
        sleepiest_minute = max([ind if entry == max(sleep_list) else None for ind, entry in enumerate(sleep_list)])
        max_specific_min = most_common_min
print most_consistent_guard * sleepiest_minute
