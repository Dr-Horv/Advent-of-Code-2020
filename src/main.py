
from day01 import solver
from day02 import solver

if __name__ == '__main__':
    with open('day02/day02.txt') as f:
        lines = [l.strip() for l in f]

    result = solver.solve(lines, True)
    print(result)