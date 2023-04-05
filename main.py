import pygame

import constants as con
from enemy import Enemy
from pacman import Pacman

pygame.init()

# создаем окно
screen = pygame.display.set_mode((con.WIDTH, con.HEIGHT))
pygame.display.set_caption("Pacman Game")

# создаем спрайты
all_sprites = pygame.sprite.Group()
player = Pacman(con.WIDTH // 2, con.HEIGHT // 2)
enemies = pygame.sprite.Group()
for i in range(con.NUM_ENEMIES):
    enemy = Enemy()
    enemies.add(enemy)
    all_sprites.add(enemy)
all_sprites.add(player)

# задний фон
background = pygame.Surface(screen.get_size())
background.fill(con.BLACK)

clock = pygame.time.Clock()

# цикл игры
running = True
while running:
    clock.tick(60)

    # обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.direction = "left"
            elif event.key == pygame.K_RIGHT:
                player.direction = "right"
            elif event.key == pygame.K_UP:
                player.direction = "up"
            elif event.key == pygame.K_DOWN:
                player.direction = "down"
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and player.direction == "left":
                player.direction = "stop"
            elif event.key == pygame.K_RIGHT and player.direction == "right":
                player.direction = "stop"
            elif event.key == pygame.K_UP and player.direction == "up":
                player.direction = "stop"
            elif event.key == pygame.K_DOWN and player.direction == "down":
                player.direction = "stop"

    all_sprites.update()

    # проверка столкновений
    hits = pygame.sprite.spritecollide(player, enemies, True)
    if hits:
        for enemy in hits:
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

    # отрисовка спрайтов
    screen.blit(background, (0, 0))
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
