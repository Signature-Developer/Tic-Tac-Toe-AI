from scripts.Constants import *
import pygame

class Game(pygame.sprite.Sprite):
    def __init__(self) -> None:
        pass

    def load_background(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 == 0:
                    color = DARK_BLUE
                else:
                    color = LIGHT_BLUE
                pygame.draw.rect(surface, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
