


def solve(data, part_two=False):
    numbers = [int(i) for i in data]
    if not part_two:
        for i,n1 in enumerate(numbers):
            for j,n2 in enumerate(numbers[i+1:], i):
                if (n1 + n2) == 2020:
                    return n1*n2
    else:
        for i,n1 in enumerate(numbers):
            for j,n2 in enumerate(numbers[i+1:], i):
                for k,n3 in enumerate(numbers[j+1:], j):
                    if (n1 + n2 + n3) == 2020:
                        return n1*n2*n3

    return -1