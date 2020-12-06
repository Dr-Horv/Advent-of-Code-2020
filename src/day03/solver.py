from functools import reduce


def test_slope(x_diff, y_diff, map, max_x, max_y):
    x = 0
    y = 0
    trees = 0
    while y < max_y:
        x = (x + x_diff) % max_x
        y = y + y_diff
        if map.get((x, y), False):
            trees += 1

    return trees


def solve(data, part_two=False):
    map = dict()
    max_y = len(data)
    max_x = len(data[0])
    for y, l in enumerate(data):
        for x, c in enumerate(l):
            if c == '#':
                map[(x, y)] = True

    if not part_two:
        return test_slope(3, 1, map, max_x, max_y)
    else:
        trees_data = [test_slope(x_diff, y_diff, map, max_x, max_y) for (x_diff, y_diff) in
                      [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]]
        return reduce(lambda x, y: x * y, trees_data)
