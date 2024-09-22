import sys
import pygame

from settings import Settings
from knight import Knight

class Knightgame:
    """Setup Game"""
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.knight = Knight(self)
        self.clock = pygame.time.Clock()
        self.running = True

        pygame.display.set_caption('Knight Game')

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            # Watch for keyboard and mouse events
            self._check_events()
            self._check_screen()
            self.clock.tick(60)
            self.knight.update()


    def _check_events(self):
        """Check for events from player"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            if event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_ESCAPE:
            sys.exit()
        if event.key == pygame.K_RIGHT:
            self.knight.moving_right = True
        if event.key == pygame.K_LEFT:
            self.knight.moving_left = True
        if event.key == pygame.K_UP:
            self.knight.moving_up = True
        if event.key == pygame.K_DOWN:
            self.knight.moving_down = True

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.knight.moving_right = False
        if event.key == pygame.K_LEFT:
            self.knight.moving_left = False
        if event.key == pygame.K_UP:
            self.knight.moving_up = False
        if event.key == pygame.K_DOWN:
            self.knight.moving_down = False

    def _check_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.knight.blitme(self.screen)
        pygame.display.flip()


if __name__ == '__main__':
    game = Knightgame()
    game.run_game()