"""
Stores the state of the drawing board.
"""


class Board(object):
    ROWS = COLS = 90

    def __init__(self):
        """
        init the board by creating empty board (all white pixels)
        """
        self.data = self._create_empty_board()

    def update(self, x, y, color):
        """
        updates a singular pixel of the board
        :param x: int
        :param y: int
        :param color: 0-8
        :return:
        """
        neighs = [(x, y)] + self.get_neighbour(x, y)
        for x, y in neighs:
            if 0 <= x <= self.COLS and 0 <= y <= self.ROWS:
                self.data[y][x] = color

    def get_neighbour(self,x,y):
        return [ (x-1, y-1), (x, y-1), (x+1, y-1),
                 (x-1, y), (x+1, y),
                 (x-1, y+1), (x, y+1), (x+1, y+1)]

    def clear(self):
        """
        clears board to all white
        :return: None
        """
        self.data = self._create_empty_board()

    def _create_empty_board(self):
        """
        creates an empty board (all white)
        :return: None
        """
        return [[0 for _ in range(self.COLS)] for _ in range(self.ROWS)]

    def fill(self, x, y):
        """
        fills in a specific shape or area using recursion
        :param x: int
        :param y: int
        :return: None
        """
        pass

    def get_board(self):
        """
        gets the data of the board
        :return: (int,int,int)[]
        """
        return self.data
