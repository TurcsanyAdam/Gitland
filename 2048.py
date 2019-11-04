# Implementation of the 2048 rage game (yes, I call it rage game)

import sys
import random

# matrix = [[2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2]]
# matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]


# Starts game with resetting the matrix and creating 2 new tiles
def InitNewGame():
    matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for _ in range(2):
        SpawnNewTile()
    PrintMatrix()


# Spawns one 2-tile randomly at an empty position
def SpawnNewTile():
    i = random.randint(0, 3)
    j = random.randint(0, 3)
    if matrix[i][j] == 0:
        matrix[i][j] = 2
    elif CheckPossibilities():
        return
    else:
        SpawnNewTile(matrix)


# Method called when there are no 0 cells left. Checks if neighbour cells can be merged.
def CheckPossibilities():
    for i in range(4):
        for j in range(4):
            if (matrix[i][j] == matrix[i + 1][j] or matrix[i][j] == matrix[i - 1][j] or
                    matrix[i][j] == matrix[i][j + 1] or matrix[i][j] == matrix[i][j - 1]):
                print("you can still do it!")
                return True
            else:
                PrintMatrix()
                print("game over")
                sys.exit()


def PrintMatrix():
    print('\n'.join([' '.join(['{:4}'.format(item) for item in row])
                     for row in matrix]))


def MoveUp():
    print("move up")


def MoveRight():
    for i in range(0, 4):
        for j in range(0,3):
            if matrix[i][j + 1] == 0:
                matrix[i][j+1] = matrix[i][j]
                matrix[i][j] = 0
            if matrix[i][j+1] == matrix[i][j]:
                matrix[i][j+1] += matrix[i][j]
                matrix[i][j] = 0
    PrintMatrix()
    print("move right")


def MoveDown():
    for i in range(0,3):
        for j in range(0,4):
            if matrix[i + 1][j] == 0:
                matrix[i + 1][j] = matrix[i][j]
                matrix[i][j] = 0
            if matrix[i + 1][j] == matrix[i][j]:
                matrix[i + 1][j] += matrix[i][j]
                matrix[i][j] = 0
    PrintMatrix()
    print("move down")


def MoveLeft():
    for i in range(3, -1, -1):
        for j in range(3, 0, -1):
            if matrix[i][j - 1] == 0:
                matrix[i][j - 1] = matrix[i][j]
                matrix[i][j] = 0
            if matrix[i][j - 1] == matrix[i][j]:
                matrix[i][j - 1] += matrix[i][j]
                matrix[i][j] = 0
    PrintMatrix()
    print("move left")


InitNewGame()

while True:
    cmd = input("Next input please (w, a, s, d, new, exit): ")
    if cmd == 'w':
        MoveUp()
    elif cmd == 'd':
        MoveRight()
    elif cmd == 's':
        MoveDown()
    elif cmd == 'a':
        MoveLeft()
    elif cmd == "new":
        InitNewGame()
    elif cmd == "exit":
        sys.exit()
    else:
        input("Invalid input, try again: ")

# SpawnNewTile()
# CheckPossibilities()
PrintMatrix()
