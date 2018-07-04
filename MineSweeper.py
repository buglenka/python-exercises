#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""MineSweeper Game

"""
import datetime

from enum import Enum
from random import randint
from collections import deque

BEGINNER = 1
INTERMEDIATE = 2
EXPERT = 3

SETTINGS = {
    BEGINNER: {'size': 8, 'count': 10 },
    INTERMEDIATE: {'size': 16, 'count': 40 },
    EXPERT: {'size': 32, 'count': 99 },
}

class AlreadyOpened(Exception):
    def __init__(self):
        super().__init__()

class AlreadyMarked(Exception):
    def __init__(self):
        super().__init__()

class Status(Enum):
    CLOSED = 0
    OPENED = 1
    MARKED = 2

class Cell(object):
    """Cell

    Base cell which doesn't have any value.

    It can be marked as:
      '-': closed cell
      'M': marked as a mine
      ' ': opened cell
    """

    _VIEWS = {
        Status.CLOSED: '-',
        Status.OPENED: ' ',
        Status.MARKED: 'M',
    }

    def __init__(self):
        self._status = Status.CLOSED

    def isOpened(self):
        return (self._status is Status.OPENED)

    def isMarked(self):
        return (self._status is Status.MARKED)

    def show(self):
        if self.isOpened(): return

        self._status = Status.OPENED # show

    def open(self):
        """Open cell

        Incapsulates the internal method _open().

        Exceptions:
          - AlreadyOpened: Try to open already opened cell 
          - AlreadyMarked: Try to open cell marked as a mine
        """
        if self.isOpened():
            raise AlreadyOpened()

        if self.isMarked():
            raise AlreadyMarked()

        self._status = Status.OPENED

    def mark(self):
        """Mark/Unmark the cell

        Exceptions:
          - AlreadyOpened: Try to mark already opened cell
        """
        if self.isOpened():
            raise AlreadyOpened()

        if self._status is Status.CLOSED:
            self._status = Status.MARKED
        else:
            self._status = Status.CLOSED

    def __str__(self):
        return Cell._VIEWS[self._status]

class Number(Cell):
    """Number cell

    Cell which indicated a number neightbouring cells
    with mines.

    Neighbouring cells marked as 1:
      1 1 1
      1 * 1
      1 1 1 

    Numbers can be [0, 8]. 
    These cells will be initialized with proper numbers
    after the mines installed.

    It can be marked as 'N', where N - is a number.
    """

    # Differences to calculate neighbours of cell
    DXDY = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]

    def __init__(self):
        super().__init__()

        self._value = 0

    def adjust(self):
        """Adjust the number

        This method is called during initialization of number cells
        around mines.
        """

        self._value += 1

    def __str__(self):
        # Rewrite view if cell is opened
        if self.isOpened():
            return str(self._value)

        return super().__str__()

class MineStatus(Enum):
    INSTALLED = 0
    EXPLODED = 1
    FOUND = 2

class Mine(Cell):
    """Mine cell

    It can be printed as:
      - 'x': installed and marked mine
      - 'X': installed and not marked mine
      - 'Ж': exploded mine
      - views from base class
    """

    _MINE_VIEWS = {
        MineStatus.INSTALLED: 'X',
        MineStatus.EXPLODED: 'Ж',
        MineStatus.FOUND: 'x',
    }

    def __init__(self):
        super().__init__()
     
        self._mineStatus = MineStatus.INSTALLED

    def open(self):
        """Open mine cell

        Rewrites the base class method.

        Changes mine status.
        """
        super().open()

        self._mineStatus = MineStatus.EXPLODED

    def mark(self):
        """Mark cell as mine

        Rewrites the base class method.

        Changes mine status.
        """
        super().mark()

        if self.isMarked():
            self._mineStatus = MineStatus.FOUND
        else:
            self._mineStatus = MineStatus.INSTALLED

    def __str__(self):
        # Rewrites view if mine is opened
        if self.isOpened():  
            return Mine._MINE_VIEWS[self._mineStatus]

        return super().__str__()


class IndexOutOfBounds(Exception):
    def __init__(self):
        pass

class MineExploded(Exception):
    def __init__(self):
        pass

class Field(object):
    """Mine field 'size' x 'size' with 'count' mines

    Represents field with mines, methods to install, open
    and mark the cells.
    """

    def __init__(self, mode):
        size = SETTINGS[mode]['size']
        count = SETTINGS[mode]['count']

        self._size = size
        self._mineCount = count
        self._mineMarked = 0
        self._mineCoords = [] # for quicker search of mines
        self._openedCount = 0

        # Initialize with empty cells for now
        self._cells = [[ Cell() for col in range(size)] for row in range(size) ]

        # Set the mines randomly
        self._placeMines()

        # Set the numbers around mines
        self._placeNumbers()

    def _placeMines(self):
        maxIdx = self._size - 1

        minePlaced = 0
        while(minePlaced != self._mineCount):
            x = randint(0, maxIdx)
            y = randint(0, maxIdx)

            if (type(self._cells[x][y]) is Mine): continue

            self._cells[x][y] = Mine()

            self._mineCoords.append((x, y))

            minePlaced += 1

    def _checkIdxs(self, x, y):
        """Check the values of indeces

        If values are out of the boundaries returns False.
        """

        minIdx = 0
        maxIdx = self._size - 1

        if (x < minIdx) or (x > maxIdx) or \
           (y < minIdx) or (y > maxIdx):
            return False

        return True

    def _placeNumbers(self):
        for x, y in self._mineCoords: # Set the number around each mine
            for dx, dy in Number.DXDY:
                X, Y = x+dx, y+dy

                # Calculated indeces can be out of the boundaries
                # for example for x = 0 or y = size - 1
                if not self._checkIdxs(X, Y): continue

                if (type(self._cells[X][Y]) is Mine): continue
 
                if (type(self._cells[X][Y]) is Cell):
                    self._cells[X][Y] = Number()

                self._cells[X][Y].adjust()

    def isCompleted(self):
        """All field is opened
     
        Returns True if all field is opened and all mines are
        correctly marked.
        """
        if (self._mineCount == self._mineMarked) and \
           (self._openedCount == (self._size*self._size - self._mineCount)):
            return True

        return False

    def mark(self, x, y):
        """Mark/Unmark cell as mine

        Exceptions:
          - IndexOutOfBounds: specified index is out of the boundaries.
          - AlreadyOpened: Try to mark already opened cell.
        """
        if not self._checkIdxs(x, y):
            raise IndexOutOfBounds()

        self._cells[x][y].mark()

        # Count
        if self._cells[x][y].isMarked():
            self._mineMarked += 1
        else:
            self._mineMarked -= 1

    def open(self, x, y):
        """Open cell with coordinates 'x' and 'y'

        Exceptions:
          - IndexOutOfBounds: specified index is out of the boundaries.
          - MineExploded: Raised when mine exploded.
          - AlreadyOpened: Try to open already opened cell.
          - AlreadyMarked: Try to open cell marked as a mine.
        """
        if not self._checkIdxs(x, y):
            raise IndexOutOfBounds()

        self._cells[x][y].open()

        # Store the number of opened cells
        self._openedCount += 1

        # If specified cell was a mine, it exploded
        if (type(self._cells[x][y]) is Mine):
            raise MineExploded()

        # If specified cell is empty, need to open 
        # neighbouring cells
        if (type(self._cells[x][y]) is Cell):
            self._openNeighbours(x, y)

    def _openNeighbours(self, x, y):
        queue = deque()
        queue.append((x, y))

        while queue:
           _x, _y = queue.popleft()

           for dx, dy in Number.DXDY:
                X, Y = _x+dx, _y+dy

                if (not self._checkIdxs(X, Y)): continue

                if (self._cells[X][Y].isOpened() or self._cells[X][Y].isMarked()): continue

                if type(self._cells[X][Y]) is Mine: continue

                # Store the number of opened cells
                self._openedCount += 1

                if (type(self._cells[X][Y]) is Cell):
                    queue.append((X, Y))

                self._cells[X][Y].open()

    def show(self):
        for x in range(self._size):
            for y in range(self._size):
                self._cells[x][y].show()

        self.status()

    def status(self):
        """Status of cells

        """
        COLSIZE = 3

        print('Field:')

        # First row is column numbers
        xs = [''.rjust(COLSIZE)]
        for y in range(self._size):
            xs.append(str(y).rjust(COLSIZE))
        print(''.join(xs))

        # Underline the field heading
        xs = [''.rjust(COLSIZE)]
        xs.extend(['-'] * COLSIZE * self._size)
        print(''.join(xs))

        # Print values
        for y in range(self._size):
            xs = [ '{}|'.format(y).rjust(COLSIZE) ] # First value is the number of row

            for x in range(self._size):
                xs.append(str(self._cells[x][y]).rjust(COLSIZE))

            print(''.join(xs))

        print('Mines left: {}'.format(self._mineCount - self._mineMarked))

# Store the time of start to mesure the duration of the game
StartTimestamp = datetime.datetime.now()

# Print ptions to start game and read the input
level = None
while(True):
    try:
        level = int(input('Enter the level (1 - Beginner, 2 - Entermediate, 3 - Expert): '))
    except ValueError:
        print("Not a valid number.")

    if (level < 1) or (level > 3):
        print("Invalid number.")
        continue

    break

# Create game field and print the initial status
field = Field(level)
field.status()

# Opening cells
while not field.isCompleted():
    command = input('Print command like \'m x y\' (mark cell as mine) or \'o x y\' (open cell): ')

    s = command.split()

    if len(s) != 3:
        print('Enter a valid command!')
        continue

    if s[0].lower().strip() not in ['m','o']:
        print('The first letter should be \'O\'(open cell) or \'M\'(mark cell as mine.)')
        continue

    markCell = False
    if (s[0].lower().strip() == 'm'):
        markCell = True

    x = y = 0    
    try:
        x = int(s[1])
        y = int(s[2])
    except ValueError:
        print('Enter a valid numbers!')
        continue

    try:
        if markCell:
            field.mark(x, y)
        else:
            field.open(x, y)

        field.status()
    except IndexOutOfBounds:
        print('At least one index is out of the boundaries.')
        continue
    except AlreadyOpened:
        print('This cell is already opened.')
        continue
    except AlreadyMarked:
        print('This cell is already marked.')
        continue
    except MineExploded:
        print('Mine EXPLODED!!!')
        field.show()
        break

# Result of the Game
print('Game duration: {}'.format(datetime.datetime.now() - StartTimestamp))

