# MODULE IMPORTS
from sys import exit
import pygame

# CUSTOM SCRIPTS
from scripts.Constants import *
from scripts.Game import Game

pygame.init()

class Main:
    def __init__(self) -> None:
        #* SCREEN SETUP
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Tic Tac Toe")

        # GAME SETUP
        self.game = Game()

    def loop(self) -> None:
        while True:
            self.screen.fill(BLACK)
            self.game.load_background(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()


            pygame.display.update()

if __name__ == "__main__":
    main = Main()
    main.loop()