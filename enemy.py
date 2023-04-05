import random

import pygame

import constants as con


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((con.ENEMY_SIZE, con.ENEMY_SIZE))
        self.image.fill(con.BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (
            random.randint(0, con.WIDTH),
            random.randint(0, con.HEIGHT)
                )
        self.direction = random.choice(["left", "right", "up", "down"])
        self.move_time = con.ENEMY_MOVE_TIME

    def update(self):
        if self.direction == "left":
            self.rect.x -= con.ENEMY_SPEED
        elif self.direction == "right":
            self.rect.x += con.ENEMY_SPEED
        elif self.direction == "up":
            self.rect.y -= con.ENEMY_SPEED
        elif self.direction == "down":
            self.rect.y += con.ENEMY_SPEED

        if self.rect.left < 0:
            self.rect.left = 0
            self.direction = random.choice(["right", "up", "down"])
        elif self.rect.right > con.WIDTH:
            self.rect.right = con.WIDTH
            self.direction = random.choice(["left", "up", "down"])
        elif self.rect.top < 0:
            self.rect.top = 0
            self.direction = random.choice(["left", "right", "down"])
        elif self.rect.bottom > con.HEIGHT:
            self.rect.bottom = con.HEIGHT
            self.direction = random.choice(["left", "right", "up"])

        time_now = pygame.time.get_ticks()
        if time_now - self.move_time > 5000:
            self.move_time = time_now
            self.direction = random.choice(["left", "right", "up", "down"])