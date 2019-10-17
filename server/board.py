"""
Stores the state of the drawing board.
"""


class Board(object):
    ROWS = COLS = 720

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
        self.data[y][x] = color

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
