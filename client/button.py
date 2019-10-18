"""
Stores interface for button and two concrete button classes
to be used in the UI.
"""
import pygame


class Button:

    def __init__(self, x, y, width, height, color, border_color=(0,0,0)):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color
        self.border_color = border_color
        self.BORDER_WIDTH = 2

    def draw(self, win):
        pygame.draw.rect(win, self.border_color, (self.x, self.y, self.width, self.height), 0)
        pygame.draw.rect(win, self.color, (
        self.x + self.BORDER_WIDTH, self.y + self.BORDER_WIDTH, self.width - self.BORDER_WIDTH * 2,
        self.height - self.BORDER_WIDTH * 2), 0)

    def click(self, x, y):
        """
        if user clicked on button
        :param x: float
        :param y: float
        :return: bool
        """

        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            return True  # user clicked button

        return False


class TextButton(Button):
    def __init__(self, x, y, width, height, color, text, border_color=(0,0,0)):
        super().__init__(x, y, width, height, color, border_color)
        self.text = text
        self.text_font = pygame.font.SysFont("comicsans", 30)

    def change_font_size(self, size):
        self.text_font = pygame.font.SysFont("comicsans", size)

    def draw(self, win):
        super().draw(win)
        txt = self.text_font.render(self.text, 1, (0,0,0))
        win.blit(txt, (self.x + self.width/2 - txt.get_width()/2, self.y + self.height/2 - txt.get_height()/2))






