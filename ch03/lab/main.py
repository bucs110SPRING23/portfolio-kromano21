import pygame
import random
import math
pygame.init()
screen = pygame.display.set_mode(size = (600, 600))
screen.fill("blue")
pygame.draw.circle(screen, "red", (300, 300), 300)
pygame.draw.circle(screen, "red", (300, 300), 299)
pygame.draw.line(screen, "black", (300, 0), (300, 600))
pygame.draw.line(screen, "black", (0, 300), (600, 300))
pygame.display.flip()
pygame.time.wait(2000)
for i in range(10):
    x = random.randrange(0, 600)
    y = random.randrange(0, 600)
    distance_from_center = math.hypot(x - 300, y - 300)
    if distance_from_center <= 300:
        pygame.draw.circle(screen, "white", (x, y), 5)
    elif distance_from_center > 300:
        pygame.draw.circle(screen, "black", (x, y), 5)
    pygame.display.flip()
    pygame.time.wait(2000)
pygame.time.wait(5000)