def occupied(c, seat_map, part_two, max_dimension):
    nbr = 0
    (x,y) = c
    if not part_two:
        if seat_map.get((x+1,y), '.') == '#':
            nbr += 1
        if seat_map.get((x-1,y), '.') == '#':
            nbr += 1
        if seat_map.get((x+1,y+1), '.') == '#':
            nbr += 1
        if seat_map.get((x+1,y-1), '.') == '#':
            nbr += 1
        if seat_map.get((x-1,y+1), '.') == '#':
            nbr += 1
        if seat_map.get((x-1,y-1), '.') == '#':
            nbr += 1
        if seat_map.get((x,y+1), '.') == '#':
            nbr += 1
        if seat_map.get((x,y-1), '.') == '#':
            nbr += 1
    else:
        (max_x, max_y) = max_dimension
        for (x_diff,y_diff) in [(-1,0),(1,0),(0,1),(0,-1),(-1,-1),(-1,1),(1,1),(1,-1), ]:
            (x, y) = c
            (x,y) = (x+x_diff, y+y_diff)
            while max_x >= x >= 0 and max_y >= y >= 0:
                if seat_map.get((x,y)) == "L":
                    break
                elif seat_map.get((x,y)) == "#":
                    nbr += 1
                    break
                (x, y) = (x + x_diff, y + y_diff)

    return nbr


def apply_rules(seat_map, part_two, max_dimension):
    new_seat_map = dict()
    for (c,v) in seat_map.items():
        #print("{}{}".format(key,value))
        if v == 'L':
           if occupied(c, seat_map, part_two, max_dimension) == 0:
               new_seat_map[c] = '#'
           else:
               new_seat_map[c] = v
        if v == '#':
            nbr_occupied = occupied(c, seat_map, part_two, max_dimension)
            if (not part_two and nbr_occupied >= 4) or (part_two and nbr_occupied >= 5):
                new_seat_map[c] = 'L'
            else:
                new_seat_map[c] = v
        if v == '.':
            new_seat_map[c] = '.'

    return new_seat_map

def print_map(seat_map, max_dimension):
    (max_x, max_y) = max_dimension
    y = 0
    x = 0
    str = ""
    while y <= max_y:
        while x <= max_x:
            v = seat_map.get((x,y))
            str += v
            x += 1
        str += "\n"
        y += 1
        x = 0
    print(str + "\n\n")

def solve(data, part_two=False):
    seat_map = dict()
    max_x = 0
    max_y = 0
    for y, l in enumerate(data):
        if y > max_y:
            max_y = y
        for x, c in enumerate(l):
            if x > max_x:
                max_x = x
            seat_map[(x, y)] = c

    new_map = apply_rules(seat_map, part_two,  (max_x, max_y))
    #print_map(new_map, (max_x, max_y))
    while seat_map != new_map:
        seat_map = new_map
        new_map = apply_rules(seat_map, part_two, (max_x, max_y))
        #print_map(new_map, (max_x, max_y))

    count = 0
    for (c, v) in seat_map.items():
        if v == '#':
            count += 1

    return count