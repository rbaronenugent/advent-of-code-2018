with open("input.csv") as input_file:
    lines = input_file.readlines()
lines = [i.split('\n')[0] for i in lines]

coords = []
sizes = []
claim_nos = []
for entry in lines:
    coord = entry.split(' @ ')[1].split(': ')[0]
    size = entry.split(': ')[1]
    claim_no = entry.split(' @ ')[0]
    coords.append((int(coord.split(',')[0]), int(coord.split(',')[1])))
    sizes.append((int(size.split('x')[0]), int(size.split('x')[1])))
    claim_nos.append(claim_no)

# part 1
occupied_coords = {}
for coord, size in zip(coords, sizes):
    for x in xrange(size[0]):
        for y in xrange(size[1]):
            c = (coord[0] + x + 1, coord[1] + y + 1)
            if c not in occupied_coords:
                occupied_coords[c] = 1
            else:
                occupied_coords[c] += 1

multiple_claims = 0
for i in occupied_coords.values():
    if i > 1:
        multiple_claims += 1
print multiple_claims


# part 2
for coord, size, claim_no in zip(coords, sizes, claim_nos):
    b = False
    for x in xrange(size[0]):
        for y in xrange(size[1]):
            c = (coord[0] + x + 1, coord[1] + y + 1)
            if occupied_coords[c] > 1:
                b = True
                break
        if b:
            break
    if not b:
        print claim_no
