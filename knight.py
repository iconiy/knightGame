import pygame


class Knight:
    def __init__(self, game):
        """Sets up knight object"""
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = game.screen.get_rect()

        # Loads in knight image file
        self.image = pygame.image.load("myknight.png")
        self.rect = self.image.get_rect()

        # self.rect.centerx = self.screen_rect.centerx
        # self.rect.centery = self.screen_rect.centerx

        # Set Knights starting position
        self.rect.x = 0
        self.rect.y = 400

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.settings.knight_speed = 5

    def update(self):
        """Update the knights movement"""
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.knight_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.knight_speed
        # if self.moving_left and self.rect.left > 0:
        #     self.x -= self.settings.knight_speed
        # if self.moving_right and self.rect.right < self.screen_rect.right:
        #     self.x += self.settings.knight_speed

        self.rect.x = self.x
        self.rect.y = self.y


    def blitme(self, screen):
        """Draw the knight at its current location"""
        screen.blit(self.image, self.rect)