
from day01 import solver
from day02 import solver
from day03 import solver
from day04 import solver
from day05 import solver

if __name__ == '__main__':
    with open('day05/day05.txt') as f:
        lines = [l.strip() for l in f]

    result = solver.solve(lines, True)
    print(result)