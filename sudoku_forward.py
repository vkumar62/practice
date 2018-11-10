#!/usr/bin/python3
import pdb
from pprint import pprint
from sortedcontainers import SortedSet

''' Incomplete/very slow '''

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

def populate_next_value(grid, choices, i, j, choice_index):
    valid = False

    while not valid:
        if len(choices[i][j]) <= choice_index:
            return False, 0

        if i == 0 and j == 3:
            pdb.set_trace()
        next_val = choices[i][j][choice_index]
        grid[i][j] = next_val
        valid = checker(grid, i, j)
        choice_index += 1
    return True, choice_index

def _solve(grid, choices, i, j):
    i, j = get_next_free(grid, i, j)
    if i == None and j == None:
        return True

    cur_valid = False
    down_valid = False
    choice_index = 0

    while not down_valid:
        cur_valid, choice_index = populate_next_value(grid, choices, i, j, choice_index)

        if not cur_valid:
            grid[i][j] = 0 
            break
        remove_choices(choices, i, j, grid[i][j])
        choice_index -= 1
        down_valid = _solve(grid, choices, i, j+1)
        if not down_valid:
            add_choices(choices, i, j, grid[i][j])
            choice_index += 1

    
    return cur_valid

def add_choices(choices, i, j, val):
    r = i
    for c in range(0, 9):
        choices[r][c].add(val)

    c = j
    for r in range(0, 9):
        choices[r][c].add(val)

    for r in range(3*int(i/3), 3+3*int(i/3)):
        for c in range(3*int(j/3), 3+3*int(j/3)):
            choices[r][c].add(val)
    
def remove_choices(choices, i, j, val):
    r = i
    for c in range(0, 9):
        choices[r][c].discard(val)

    c = j
    for r in range(0, 9):
        choices[r][c].discard(val)

    for r in range(3*int(i/3), 3+3*int(i/3)):
        for c in range(3*int(j/3), 3+3*int(j/3)):
            choices[r][c].discard(val)
    
def prepare(grid, choices):
    for r in range(0, 9):
        for c in range(0, 9):
            if grid[r][c]:
                remove_choices(choices, r, c, grid[r][c])


def solve(grid):
    choices = [[SortedSet(range(1,10)) for _ in range(9)] for _ in range(9)]
    prepare(grid, choices)
    pdb.set_trace()
    valid_solution = _solve(grid, choices, 0, 0)
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

grid = [
 [8, 1, 2, 7, 5, 3, 0, 0, 0],
 [9, 4, 3, 6, 8, 2, 0, 0, 0],
 [6, 7, 5, 4, 9, 1, 0, 0, 0],
 [1, 5, 4, 2, 3, 7, 0, 0, 0],
 [3, 6, 9, 8, 4, 5, 0, 0, 0],
 [2, 8, 7, 1, 6, 9, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0]]
solve(grid)
