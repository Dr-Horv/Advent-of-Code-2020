


def solve(data, part_two=False):
    max_found = -1
    seat_ids = []
    for l in data:
        row_max = 127
        row_min = 0
        seat_max = 7
        seat_min = 0
        for c in l:
            if c == 'F':
                row_max = ((row_max-row_min) // 2) + row_min
            elif c == 'B':
                row_min = ((row_max-row_min) // 2) + 1 + row_min
            elif c == 'L':
                seat_max = ((seat_max-seat_min) // 2) + seat_min
            elif c == 'R':
                seat_min = ((seat_max-seat_min) // 2) + 1 + seat_min
        seat_id = row_max * 8 + seat_max
        seat_ids.append(seat_id)
        if seat_id > max_found:
            max_found = seat_id

    if not part_two:
        return max_found
    else:
        sorted_seat_ids = sorted(seat_ids)
        set_seat_ids = set(seat_ids)
        for potential_seat_id in range(sorted_seat_ids[0], sorted_seat_ids[-1]):
            if potential_seat_id not in set_seat_ids:
                return potential_seat_id
