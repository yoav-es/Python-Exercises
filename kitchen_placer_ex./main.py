import math
from collections import deque

# constants
WALL = 'W'
EMPLOYEE = 'E'
BLANK = ' '
NO_PATH = - 1
DIRECTIONS = 4
NO_PATH_MARK = 100
LOCATION_MESSAGE = "Optimal kitchen location is at"
MAP_FILE = 'map.txt'
# neighbour coordinates
rowNum = [-1, 0, 0, 1]
colNum = [0, -1, 1, 0]

"""
A class that represents a Point on the plan with x and y coordinates
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Board:
    """
    A class representing the floor plan matrix
    """

    def __init__(self, file):
        """
        Initialize a new Board object.
        """
        # implement your code here (and then delete the next line - 'pass')
        # self.rows = rows
        # self.cols = cols
        self.spaces = []
        self.employees = []
        self.mat = []
        with open(MAP_FILE, 'r') as f:
            self.mat = [[str(num) for num in line.split(',')] for line in f]
            f.close()
        self.cols = len(self.mat)
        self.rows = len(self.mat[0]) - 1
        for row in range(self.rows):
            for col in range(self.cols):
                data = self.mat[col][row]
                if data == EMPLOYEE:
                    self.employees.append(Point(row, col))
                elif data == ' ':
                    self.spaces.append(Point(row, col))
        f.close()

    def get(self, x, y):
        if x >= self.rows or y >= self.cols:
            return None
        if x <= 0 or y <= 0:
            return None
        return self.mat[y][x]


"""
A class that represents queue for the BFS algorithm
"""


class Qnode:
    def __init__(self, pt: Point, dist: int):
        self.pt = pt  # The coordinates of the cell
        self.dist = dist  # Cell's distance from the source


"""
A function to calculate the distance between two points
"""


def recDist(a, b):
    dist = math.sqrt((a.x - b.x) ^ 2 + (a.y - b.y) ^ 2)
    return dist


"""
A function to check that a point is not out of bounds or not a Wall
"""


def verify(p, board):
    if p.x >= board.rows or p.y >= board.cols:
        return False
    if p.x <= 0 or p.y <= 0:
        return False
    tmp = board.get(p.x, p.y)
    if tmp == WALL:
        return False
    elif tmp == EMPLOYEE or tmp == BLANK:
        return True


"""
Bfs algorithm implementation for getting the minimal distance from one point to another
src = open space, destination = employee
"""


def BFS(mat: Board, src: Point, dest: Point):
    if not verify(src, mat) or not verify(dest, mat):
        return NO_PATH
    if src.x == dest.x and src.y == dest.y:
        return None
    visited = [[False for i in range(mat.cols)] for j in range(mat.rows)]
    visited[src.x][src.y] = True
    q = deque()
    s = Qnode(src, 0)
    q.append(s)
    while q:
        curr = q.popleft()
        pt = curr.pt
        if pt.x == dest.x and pt.y == dest.y:
            return curr.dist
        for i in range(DIRECTIONS):
            row = pt.x + rowNum[i]
            col = pt.y + colNum[i]
            if verify(Point(row, col), mat) and not visited[row][col]:
                visited[row][col] = True
                adjCell = Qnode(Point(row, col), curr.dist + 1)
                q.append(adjCell)
    return NO_PATH


"""
A bfs that finds paths from a space to every employee and returns the sum of the distances. if the bfs cant find
a path, it adds a constant number to insure that this point could not be the minimal path
"""


def findPaths(mat: Board, space: Point):
    minSum = 0
    tmpSum = 0
    prevMin = 0
    for employee in mat.employees:
        prevMin = BFS(mat,space, employee)
        if prevMin > NO_PATH:
            minSum = prevMin
            tmpSum += minSum
        else:
            tmpSum += NO_PATH_MARK
    return tmpSum


"""
a function that finds the space with the minimal paths to all the users on the floors
and returns the coordinate that represents the optimal location to place the kitchen
"""


def findMin(mat: Board):
    results = {}
    for space in mat.spaces:
        results[(space.x, space.y)] = findPaths(mat, space)
    minVal = min(results.values())
    minSpace = [k for k, v in results.items() if v == minVal]
    print(LOCATION_MESSAGE, minSpace[0])

    return minSpace[0]


def main():
    mat = Board(MAP_FILE)
    print(findMin(mat))
    # mat = [['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
    #        ['W', ' ', 'E', ' ', ' ', ' ', 'W', ' ', 'E', ' ', ' ', ' ', 'W'],
    #        ['W', ' ', '1', ' ', ' ', ' ', 'W', ' ', '1', ' ', ' ', ' ', 'W'],
    #        ['W', ' ', '2', '3', '4', '5', '4', '3', '2', ' ', ' ', ' ', 'W'],
    #        ['W', ' ', ' ', ' ', ' ', ' ', 'W', ' ', ' ', ' ', ' ', ' ', 'W'],
    #        ['W', ' ', 'E', ' ', ' ', ' ', 'W', ' ', 'E', ' ', ' ', ' ', 'W'],
    #        ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W']]
main()
