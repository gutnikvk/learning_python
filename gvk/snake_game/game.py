import random
import pygame
from pygame.locals import *
import time


class Player:
    x = []
    y = []
    speed = 16
    direction = 0

    def update(self):
        if self.direction == 'right':
            self.x += self.speed
        elif self.direction == 'left':
            self.x -= self.speed
        elif self.direction == 'up':
            self.y -= self.speed
        elif self.direction == 'down':
            self.y += self.speed

    def move_right(self):
        self.direction = 'right'

    def move_left(self):
        self.direction = 'left'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'


class Game:
    window_width = 800
    window_height = 800
    player = 0

    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self.player = Player()

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode([self.window_width, self.window_height], pygame.HWSURFACE)
        pygame.display.set_caption("Snake game")
        self._running = True
        self._image_surf = pygame.image.load("python.png")

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def loop(self):
        pass

    def render(self):
        self._display_surf.fill((0, 0, 0))
        self._display_surf.blit(self._image_surf, (self.player.x, self.player.y))
        pygame.display.flip()

    def cleanup(self):
        pygame.quit()

    def execute(self):
        if self.on_init() == False:
            self._running = False

        while (self._running):
            pygame.event.pump()
            keys = pygame.key.get_pressed()

            if (keys[K_RIGHT]):
                self.player.move_right()

            if (keys[K_LEFT]):
                self.player.move_left()

            if (keys[K_UP]):
                self.player.move_up()

            if (keys[K_DOWN]):
                self.player.move_down()

            if (keys[K_ESCAPE]):
                self._running = False

            self.loop()
            self.render()
        self.cleanup()

if __name__ == "__main__":
    game = Game()
    game.execute()