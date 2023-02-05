import pygame
pygame.init()
screen = pygame.display.set_mode()
screen.fill([255, 0, 0])
pygame.draw.circle(screen, "orange", [200,0], 50)
pygame.time.wait(2000)
