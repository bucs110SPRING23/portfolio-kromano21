import pygame
import random
import math
pygame.init()
screen = pygame.display.set_mode(size = (600, 600))
Hitbox1 = pygame.Rect(0, 300, 100, 100)
Hitbox2 = pygame.Rect(500, 300, 100, 100)
rectangle1 = pygame.draw.rect(screen, "blue", (0, 300, 100, 100))
rectangle2 = pygame.draw.rect(screen, "red", (500, 300, 100, 100))
pygame.display.flip()
pygame.time.wait(5000)
active = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if Hitbox1.collidepoint(event.pos):
                screen.fill("blue")
                pygame.draw.circle(screen, "red", (300, 300), 300)
                pygame.draw.circle(screen, "red", (300, 300), 299)
                pygame.draw.line(screen, "black", (300, 0), (300, 600))
                pygame.draw.line(screen, "black", (0, 300), (600, 300))
                pygame.display.flip()
                pygame.time.wait(2000)
                player1score = 0
                player2score = 0
                for i in range(10):
                    x = random.randrange(0, 600)
                    y = random.randrange(0, 600)
                    x2 = random.randrange(0, 600)
                    y2 = random.randrange(0, 600)
                    distancefromcenter = math.hypot(x - 300, y - 300)
                    distancefromcenter2 = math.hypot(x2 - 300, y2 - 300)
                    if distancefromcenter <= 300:
                        pygame.draw.circle(screen, "white", (x, y), 5)
                    elif distancefromcenter > 300:
                        pygame.draw.circle(screen, "pink", (x, y), 5)
                    pygame.display.flip()
                    pygame.time.wait(1000)
                    if distancefromcenter2 <= 300:
                        pygame.draw.circle(screen, "black", (x2, y2), 5)
                    elif distancefromcenter2 > 300:
                        pygame.draw.circle(screen, "green", (x2, y2), 5)
                    pygame.display.flip()
                    pygame.time.wait(1000)
                    if distancefromcenter <= 300:
                        player1score += 1
                    if distancefromcenter2 <= 300:
                        player2score += 1
                font = pygame.font.Font(None, 48)
                if player1score == player2score:
                    text = font.render("There is a tie!", True, "white")
                    screen.blit(text, (300, 300))
                elif player1score > player2score:
                    text = font.render("Player one wins!", True, "white")
                    screen.blit(text, (300, 300))
                    text2 = font.render("You guessed right!", True, "white")
                    screen.blit(text2, (300, 400))
                else:
                    text = font.render("Player two wins!", True, "white")
                    screen.blit(text, (300, 300))
                    text2 = font.render("You guessed wrong!", True, "white")
                    screen.blit(text2, (300, 400))
                pygame.display.flip()
                pygame.time.wait(5000)
                pygame.quit()

            if Hitbox2.collidepoint(event.pos):
                screen.fill("blue")
                pygame.draw.circle(screen, "red", (300, 300), 300)
                pygame.draw.circle(screen, "red", (300, 300), 299)
                pygame.draw.line(screen, "black", (300, 0), (300, 600))
                pygame.draw.line(screen, "black", (0, 300), (600, 300))
                pygame.display.flip()
                pygame.time.wait(2000)
                player1score = 0
                player2score = 0
                for i in range(10):
                    x = random.randrange(0, 600)
                    y = random.randrange(0, 600)
                    x2 = random.randrange(0, 600)
                    y2 = random.randrange(0, 600)
                    distancefromcenter = math.hypot(x - 300, y - 300)
                    distancefromcenter2 = math.hypot(x2 - 300, y2 - 300)
                    if distancefromcenter <= 300:
                        pygame.draw.circle(screen, "white", (x, y), 5)
                    elif distancefromcenter > 300:
                        pygame.draw.circle(screen, "pink", (x, y), 5)
                    pygame.display.flip()
                    pygame.time.wait(1000)
                    if distancefromcenter2 <= 300:
                        pygame.draw.circle(screen, "black", (x2, y2), 5)
                    elif distancefromcenter2 > 300:
                        pygame.draw.circle(screen, "green", (x2, y2), 5)
                    pygame.display.flip()
                    pygame.time.wait(1000)
                    if distancefromcenter <= 300:
                        player1score += 1
                    if distancefromcenter2 <= 300:
                        player2score += 1
                font = pygame.font.Font(None, 48)
                if player1score == player2score:
                    text = font.render("There is a tie!", True, "white")
                    screen.blit(text, (300, 300))
                elif player1score > player2score:
                    text = font.render("Player one wins!", True, "white")
                    screen.blit(text, (300, 300))
                    text2 = font.render("You guessed wrong!", True, "white")
                    screen.blit(text2, (300, 400))
                else:
                    text = font.render("Player two wins!", True, "white")
                    screen.blit(text, (300, 300))
                    text2 = font.render("You guessed right!", True, "white")
                    screen.blit(text2, (300, 400))
                pygame.display.flip()
                pygame.time.wait(5000)
                pygame.quit()