import pygame

pygame.init()

screen = pygame.display.set_mode((400, 200))

x , y = 200, 100

speed = 5

clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False