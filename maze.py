#!/usr/bin/python3
import pdb

def get_all_neighbors(maze, cur):
    neighbors = []
    x,y = cur

    for xo in range(-1, 2):
        for yo in range(-1, 2):
            xi = x+xo
            yi = y+yo
            if xi < 0 or xi >= len(maze):
                continue
            if yi < 0 or yi >= len(maze[0]):
                continue
            if maze[xi][yi] == 0:
                neighbors.append((xi, yi))
    return neighbors

def solve_maze_helper(maze, cur, e, path):
    if (cur == e):
        return True

    x,y = cur
    if maze[x][y] == 1:
        return False

    maze[x][y] = 1
    path.append(cur)

    for neighbor in get_all_neighbors(maze, cur):
        solved = solve_maze_helper(maze, neighbor, e, path)
        if solved:
            return True
    path = path[-1]
    return False

def solve_maze(maze, s, e):
    path = []
    solved = solve_maze_helper(maze, s, e, path)
    return solved, path
   
maze = [
        [ 0, 0, 1, 0, 1, 0, 0 ],
        [ 0, 0, 0, 1, 0, 0, 0 ],

        ]

solved, path = solve_maze(maze, (0,0), (1, 6))
if solved:
    print(path)
else:
    print("No solution")
#pdb.set_trace()
