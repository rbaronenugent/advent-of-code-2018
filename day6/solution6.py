# define functions
def manhattan_distance(coord1, coord2):
    return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])


# load data
with open("input.txt") as input_file:
    lines = input_file.readlines()
lines = [i.split('\n')[0] for i in lines]
coords = [(int(i.split(', ')[0]), int(i.split(', ')[1])) for i in lines]


# part 1
min_x = min(zip(*coords)[0])
max_x = max(zip(*coords)[0])
min_y = min(zip(*coords)[1])
max_y = max(zip(*coords)[1])

# determine "infinite coords" by running around the perimeter of the coordinates
infinite_coords = []
for x in [min_x - 1, max_x + 1]:
    for y in xrange(min_y - 1, max_y + 2):
        min_dist = 1000
        for coord in coords:
            md = manhattan_distance(coord, (x, y))
            if md < min_dist:
                closest_coord = coord
                min_dist = md
            elif md == min_dist:
                closest_coord = None
            else:
                pass
        if closest_coord not in infinite_coords and closest_coord is not None:
            infinite_coords.append(closest_coord)

for y in [min_y - 1, max_y + 1]:
    for x in xrange(min_x - 1, max_x + 2):
        min_dist = 1000
        for coord in coords:
            md = manhattan_distance(coord, (x, y))
            if md < min_dist:
                closest_coord = coord
                min_dist = md
            elif md == min_dist:
                closest_coord = None
            else:
                pass
        if closest_coord not in infinite_coords and closest_coord is not None:
            infinite_coords.append(closest_coord)

# and calculate the closest point
area_dict = {}
for x in xrange(max_x):
    for y in xrange(max_y):
        min_dist = 1000
        for coord in coords:
            md = manhattan_distance(coord, (x, y))
            if md < min_dist:
                closest_coord = coord
                min_dist = md
            elif md == min_dist:
                closest_coord = None
            else:
                pass
        if closest_coord is None or closest_coord in infinite_coords:
            continue
        else:
            if closest_coord in area_dict:
                area_dict[closest_coord] += 1
            else:
                area_dict[closest_coord] = 1
sorted_coords = sorted(area_dict.items(), key=lambda x: x[1], reverse=True)
print sorted_coords[0][1]

# part 2
tdict = {}
for x in xrange(max_x):
    for y in xrange(max_y):
        total_md = 0
        for coord in coords:
            md = manhattan_distance(coord, (x, y))
            total_md += md
        tdict[(x, y)] = total_md
print sum([1 if val < 32 else 0 for val in tdict.values()])
