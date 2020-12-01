
from day01 import solver

if __name__ == '__main__':
    lines = []
    with open('day01/day01.txt') as f:
        lines = [l.strip() for l in f]

    result = solver.solve(lines, True)
    print(result)