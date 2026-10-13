import pygame
import time


pygame.init()


screen = pygame.display.set_mode((800, 600))

x , y = 400, 300
speed = 3
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                x -= speed
            elif keys[pygame.K_RIGHT]:
                x += speed
            elif keys[pygame.K_UP]:
                y -= speed
            elif keys[pygame.K_DOWN]:
                y += speed

            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    elif keys[pygame.K_RIGHT]:
        x += speed
    elif keys[pygame.K_UP]:
        y -= speed
    elif keys[pygame.K_DOWN]:
        y += speed




screen.fill((0,0,0))
pygame.draw.circle(screen, (255, 0 , 0) , (400, 300), 30)


pygame.display.flip()



pygame.quit()