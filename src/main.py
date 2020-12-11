
from day01 import solver
from day02 import solver
from day03 import solver
from day04 import solver
from day05 import solver
from day06 import solver
from day07 import solver
from day11 import solver

if __name__ == '__main__':
    with open('day11/day11.txt') as f:
        lines = [l.strip() for l in f]

    result = solver.solve(lines, True)
    print(result)