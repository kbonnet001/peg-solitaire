import pygame
import sys
from European_board import European_board
from Game import Game

if __name__ == "__main__":
    pygame.init()
    game = Game(600, 7, 7)
    game.run()

