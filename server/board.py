"""
Stores the state of the drawing board.
"""


class Board(object):
    ROWS = COLS = 720

    def __init__(self):
        self.data = self._create_empty_board()

    def update(self, x, y, color):
        self.data[y][x] = color

    def clear(self):
        self.data = self._create_empty_board()

    def _create_empty_board(self):
        return [[(255,255,255) for _ in range(self.COLS)] for _ in range(self.ROWS)]

    def fill(self, x, y):
        pass

    def get_board(self):
        return self.data