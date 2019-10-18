import pygame
from button import Button, TextButton
from board import Board
from top_bar import TopBar
from main_menu import MainMenu
from leaderboard import Leaderboard
from player import Player
from bottom_bar import BottomBar
from chat import Chat


class Game:
    BG = (255,255,255)

    def __init__(self):
        self.WIDTH = 1300
        self.HEIGHT = 1000
        self.win = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.leaderboard = Leaderboard(50,125)
        self.board = Board(305,125)
        self.top_bar = TopBar(10,10,1280,100)
        self.top_bar.change_round(1)
        self.players = [Player("Tim"), Player("Joe"), Player("Bill"), Player("Jeff"), Player("TBob")]
        self.skip_button = TextButton(85, 830, 125, 60, (255,255,0), "Skip")
        self.bottom_bar = BottomBar(305,880,self)
        self.chat = Chat(1050, 125)
        self.draw_color = (0,0,0)
        for player in self.players:
            self.leaderboard.add_player(player)
    
    def draw(self):
        self.win.fill(self.BG)
        self.leaderboard.draw(self.win)
        self.top_bar.draw(self.win)
        self.board.draw(self.win)
        self.skip_button.draw(self.win)
        self.bottom_bar.draw(self.win)
        self.chat.draw(self.win)
        pygame.display.update()

    def check_clicks(self):
        """
        handles clicks on buttons and screen
        :return: None
        """
        mouse = pygame.mouse.get_pos()

        # Check click on skip button
        if self.skip_button.click(*mouse):
            print("Clicked skip button")

        clicked_board = self.board.click(*mouse)

        if clicked_board:
            self.board.update(*clicked_board, self.draw_color)

    def run(self):
        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(60)
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break

                if pygame.mouse.get_pressed()[0]:
                    self.check_clicks()
                    self.bottom_bar.button_events()

                if event.type == pygame.KEYDOWN:
                    # gets the key name
                    key_name = pygame.key.name(event.key)

                    # converts to uppercase the key name
                    key_name = key_name.lower()
                    self.chat.type(key_name)

        pygame.quit()


if __name__ == "__main__":
    pygame.font.init()
    g = Game()
    g.run()
