import pygame

import constants as con


class Pacman(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((con.PLAYER_SIZE, con.PLAYER_SIZE))
        self.image.fill(con.YELLOW)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = "stop"

    def update(self):
        if self.direction == "left":
            self.rect.x -= con.PLAYER_SPEED
        elif self.direction == "right":
            self.rect.x += con.PLAYER_SPEED
        elif self.direction == "up":
            self.rect.y -= con.PLAYER_SPEED
        elif self.direction == "down":
            self.rect.y += con.PLAYER_SPEED

        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > con.WIDTH:
            self.rect.right = con.WIDTH
        elif self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > con.HEIGHT:
            self.rect.bottom = con.HEIGHT
