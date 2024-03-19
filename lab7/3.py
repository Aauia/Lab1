import pygame
import sys


pygame.init()


WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Red Ball")


r = 25
x = (WIDTH - r) // 2
y = (HEIGHT - r) // 2
s= 20


running = True
while running:
    screen.fill("WHITE")

 
    pygame.draw.circle(screen, "RED", (x, y), r)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if y - s >= 0:
                    y -= s
            elif event.key == pygame.K_DOWN:
                if y + s<= HEIGHT - r:
                    y +=s
            elif event.key == pygame.K_LEFT:
                if x - s>= 0:
                    x -= s
            elif event.key == pygame.K_RIGHT:
                if x + s<= WIDTH - r:
                    x += s

pygame.quit()
sys.exit()


