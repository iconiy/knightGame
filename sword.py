import pygame

from pygame import sprite

class Sword:
    def __init__(self):
        self.image = pygame.image.load("sword.png")
        self.rect = self.image.get_rect()
        self.rect.x = pygame.rect.x
        self.rect.y = pygame.rect.y




