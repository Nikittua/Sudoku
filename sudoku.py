from itertools import product
from random import randint


def solve_sudoku(puzzle):
    for (col, row) in product(range(9), repeat=2):
        if puzzle[row][col] == 0:
            for num in range(1, 10):
                allowed = next(
                    (
                        False
                        for (i, j) in product(range(3), repeat=2)
                        if puzzle[row - row % 3 + i][col - col % 3 + j] == num
                    ),
                    not any(
                        puzzle[i][col] == num or puzzle[row][i] == num
                        for i in range(9)
                    ),
                )
                if allowed:
                    puzzle[row][col] = num
                    if trial := solve_sudoku(puzzle):
                        return trial
                    else:
                        puzzle[row][col] = 0
            return False
    return puzzle


M = 9


def print_sudoku(a):
    for i in range(M):
        for j in range(M):
            print(a[i][j], end=" ")
        print()


if __name__ == '__main__':
    pazl = [[2, 5, 0, 0, 3, 0, 9, 0, 1],
            [0, 1, 0, 0, 0, 4, 0, 0, 0],
            [4, 0, 7, 0, 0, 0, 2, 0, 8],
            [0, 0, 5, 2, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 9, 8, 1, 0, 0],
            [0, 4, 0, 0, 0, 3, 0, 0, 0],
            [0, 0, 0, 3, 6, 0, 0, 7, 2],
            [0, 7, 0, 0, 0, 0, 0, 0, 3],
            [9, 0, 3, 0, 0, 0, 6, 0, 4]]

print_sudoku(solve_sudoku(pazl))
