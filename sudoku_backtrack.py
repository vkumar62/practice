#!/usr/bin/python3

from pprint import pprint

def checker(grid, i, j):
    if grid[i][j] == 0:
        return True

    val = grid[i][j]

    r = i
    for c in range(0, 9):
        if (r != i or c != j) and grid[r][c] == val:
            return False

    c = j
    for r in range(0, 9):
        if (r != i or c != j) and grid[r][c] == val:
            return False

    for r in range(3*int(i/3), 3+3*int(i/3)):
        for c in range(3*int(j/3), 3+3*int(j/3)):
            if (r != i or c != j) and grid[r][c] == val:
                return False
    return True


def get_next_free(grid, i, j):
    r = i
    for c in range(j, 9):
        if grid[r][c] == 0:
            return r, c

    for r in range(i+1, 9):
        for c in range(0, 9):
            if grid[r][c] == 0:
                return r, c
    return None, None

def populate_next_value(grid, i, j):
    valid = False

    while not valid:
        next_val = grid[i][j] + 1
        if next_val > 9:
            return False

        grid[i][j] = next_val
        valid = checker(grid, i, j)
    return True

def _solve(grid, i, j):
    i, j = get_next_free(grid, i, j)
    if i == None and j == None:
        return True

    old_val = grid[i][j]
    cur_valid = False
    down_valid = False

    while not down_valid:
        cur_valid = populate_next_value(grid, i, j)
        if not cur_valid:
            grid[i][j] = old_val 
            break
        down_valid = _solve(grid, i, j+1)
    
    return cur_valid
    

def solve(grid):
    valid_solution = _solve(grid, 0, 0)
    if valid_solution:
        pprint(grid)
    else:
        print("valid solution not found")

grid = [
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 6, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 9, 0, 2, 0, 0],
        [0, 5, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 4, 5, 7, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 3, 0],
        [0, 0, 1, 0, 0, 0, 0, 6, 8],
        [0, 0, 8, 5, 0, 0, 0, 1, 0],
        [0, 9, 0, 0, 0, 0, 4, 0, 0]
        ]
solve(grid)
