# MODULE IMPORTS
from sys import exit
import pygame

# CUSTOM SCRIPTS
from scripts.Constants import *

pygame.init()

class Main:
    def __init__(self) -> None:
        #* SCREEN SETUP
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Tic Tac Toe")

    def loop(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()


            pygame.display.update()

if __name__ == "__main__":
    main = Main()
    main.loop()