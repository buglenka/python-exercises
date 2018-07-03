#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""MineSweeper Game

"""
import datetime

from random import randint
from collections import deque

BEGINNER = 1
INTERMEDIATE = 2
EXPERT = 3

SETTINGS = {
    BEGINNER: {'size': 8, 'mines': 10 },
    INTERMEDIATE: {'size': 16, 'mines': 40 },
    EXPERT: {'size': 32, 'mines': 99 },
}

NEIGHB_DIFF = [ (-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1) ]

# Marks for the fields value
FV_EMPTY = 0
FV_MINE = 9
FV_EXPLODED = 10

# Marks for print field
FP_EMPTY = ' '
FP_MINE = 'х'
FP_HIDDEN = '-'
FP_EXPLODED = 'ж'
FP_MARKED = 'M'

# Marks for cells
FC_UNCHECKED = 0
FC_CHECKED = 1
FC_MARKED = 2


class Game(object):
    """Game

    """
    def __init__(self, gameLevel):
        self._startTimestamp = datetime.datetime.now()
        self._endTimestamp = None
        self._finished = False
  
        size = SETTINGS[gameLevel]['size']
        mines = SETTINGS[gameLevel]['mines']

        self._field = Field(size, mines)

    def isFinished(self):
        return self._finished

    def action(self, x, y, mark = False):
        if mark:
            self._field.mark(x, y)
        else:
            self._field.check(x, y)

        if self._field.isMineExploded() or self._field.isAllDone():
            self._finished = True
            self._endTimestamp = datetime.datetime.now()

        self._field.status()


    def result(self):
        """Print the result of the game
        """

        if (not self.isFinished()):
            print('Game is in progress.')
            return

        if self._field.isMineExploded():
            print('One of the mines exploded!')
        else:
            print('You win!')

        print('Game duration: {}'.format(self._endTimestamp - self._startTimestamp))

class Field(object):
    """Field

    Represents field with mines.

    Levels:
      - Beginner: 8x8, 10 mines
      - Intermediate: 16x16, 40 mines
      - Expert: 32x32, 99 mines
    """

    def __init__(self, size, mines):
        self._size = size
        self._mineCount = mines
        self._mineMarked = 0
        self._mineList = []
        self._mineExploded = False
        self._cellsChecked = 0

        # Create empty map
        self._initMap()
        
        # Set the mines randomly
        self._placeMines()

        # Set the numbers around mines
        self._placeNumbers()

        # Print True for debug
        self.status(False)

    def _initMap(self):
        size = self._size

        self._mineMap = [[FV_EMPTY for col in range(size)] for row in range(size)]
        self._checked = [[FC_UNCHECKED for col in range(size)] for row in range(size)]

    def _placeMines(self):
        maxIdx = self._size - 1

        minePlaced = 0
        while(minePlaced != self._mineCount):
            x = randint(0, maxIdx)
            y = randint(0, maxIdx)

            if (self._mineMap[x][y] == FV_MINE): continue

            self._mineMap[x][y] = FV_MINE
            self._mineList.append((x, y))        

            minePlaced += 1

    def _adjustNumber(self, x, y):
        if (not self._checkIdxs(x, y)) or (self._mineMap[x][y] == FV_MINE): return

        self._mineMap[x][y] += 1

    def _placeNumbers(self):
        for x, y in self._mineList:
            for dx, dy in NEIGHB_DIFF:
                self._adjustNumber(x+dx, y+dy)

    def status(self, showUnchecked = False):
        """Print all cells, mines left, game duration"""

        print('Field:')

        # Show the initial field values if mine exploded
        if (self.isMineExploded()):
            showUnchecked = True

        for y in range(self._size):
            xs = []

            for x in range(self._size):
                if (not showUnchecked) and (self._checked[x][y] == FC_UNCHECKED):
                    xs.append(FP_HIDDEN)
                    continue

                # Show the initial field values if mine exploded
                if (self._checked[x][y] == FC_MARKED) and (not self.isMineExploded()):
                    xs.append(FP_MARKED)
                elif (self._mineMap[x][y] == FV_MINE):
                    xs.append(FP_MINE)
                elif(self._mineMap[x][y] == FV_EMPTY):
                    xs.append(FP_EMPTY)
                elif(self._mineMap[x][y] == FV_EXPLODED):
                    xs.append(FP_EXPLODED)
                else:
                    xs.append(str(self._mineMap[x][y]))

            print(" ".join(xs))

        print('Mines left: {}'.format(self._mineCount - self._mineMarked))

    def check(self, x, y):
        """Check the specified cell
        """
        if not self._checkIdxs(x, y):
            print('At least one index is out of the boundaries!')
            return
    
        if (self._checked[x][y] == FC_CHECKED):
            print('This cell is already checked!')
            return

        if (self._checked[x][y] == FC_MARKED):
            print('This cell is marked as mine!')
            return

        self._checked[x][y] = True

        if (self._mineMap[x][y] == FV_MINE):
            self._mineExploded = True
            self._mineMap[x][y] = FV_EXPLODED
            return

        if (self._mineMap[x][y] == FV_EMPTY):
            self._checkNeighbours(x, y)

    def _checkNeighbours(self, x, y):
        queue = deque()
        queue.append((x, y))

        while queue:
           _x, _y = queue.popleft()

           for dx, dy in NEIGHB_DIFF:
                X, Y = _x+dx, _y+dy

                if (not self._checkIdxs(X, Y)): continue

                if (self._checked[X][Y] != FC_UNCHECKED): continue
 
                if (self._mineMap[X][Y] == FV_EMPTY):
                    self._checked[X][Y] = FC_CHECKED
                    queue.append((X, Y))

                elif (self._mineMap[X][Y] < FV_MINE): # Number
                    self._checked[X][Y] = FC_CHECKED                

    def isMineExploded(self):
        return self._mineExploded

    def isAllDone(self):
        if (self._cellsChecked == self._size*self._size) and \
           (self._mineCount == self._mineMarked):
            return True

        return False

    def _checkIdxs(self, x, y):
        """Check the values of indexes

        If values are out of the boundaries returns False.
        """

        minIdx = 0
        maxIdx = self._size - 1

        if (x < minIdx) or (x > maxIdx) or \
           (y < minIdx) or (y > maxIdx):
            return False

        return True

    def mark(self, x, y):
        """Mark or unmark cell with mine
        """

        if not self._checkIdxs(x, y): 
            print('At least one index is out of the boundaries!')
            return

        if (self._checked[x][y] == FC_CHECKED):
            print('The cell is already checked and can\'t be markded as Mine.')
            return

        if (self._checked[x][y] == FC_UNCHECKED):
            self._mineMarked += 1
            self._checked[x][y] = FC_MARKED
        else:
            self._mineMarked -= 1
            self._checked[x][y] = FC_UNCHECKED

# Print ptions to start game and read the input
level = None
while(True):
    try:
        level = int(input('Enter the level (1 - Beginner, 2 - Entermediate, 3 - Expert): '))
    except ValueError:
        print("Not a valid number.")

    if (level > 0) and (level < 4):
        break
    print("Invalid number.")

game = Game(level)

while not game.isFinished():
    answer = input('Do you want to mark/unmark the cell as mine? (y/n): ')

    mark = False
    message = 'Enter the coordinates to check (x y): '
     
    if (answer not in ['y', 'n']):
        print('Enter the valid answer!')
        continue
    elif (answer is 'y'):
        mark = True
        message = 'Enter the coordinates to mark/ummark mine (x y): '

    try:
        x, y = map(int, input(message).split())
    except ValueError:
        print("Not a valid numbers.")

    game.action(x, y, mark)

# Result of the Game
game.result()

