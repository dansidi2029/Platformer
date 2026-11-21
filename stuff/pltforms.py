import pygame
from Settings import SCREEN_WIDTH
class Tilemap(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:/Users/Codewiz/Documents/Dan Sidi/stuff/Brick_Block")
        self.image = pygame.transform.scale(SCREEN_WIDTH, 100)