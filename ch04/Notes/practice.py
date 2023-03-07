import pygame

for event in pygame.event.get():
     if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_SPACE:
             random.shuffle(order)
             turns = len(order)
             result = []
             for color in order:
                 for c, hb in hitboxes.items(): #reset boxes to main color
                     pygame.draw.rect(screen, main_colors[c], hb)
                 pygame.draw.rect(screen, highlight_colors[color], hitboxes[color])
                 pygame.display.flip()
                 pygame.time.delay(1000)
         elif event.key == pygame.K_q:
             done = True
     elif event.type == pygame.MOUSEBUTTONDOWN:
         turns = turns - 1
         if hitboxes["red"].collidepoint(event.pos):
             result.append("red")
         elif hitboxes["purple"].collidepoint(event.pos):
             result.append("purple")
         elif hitboxes["green"].collidepoint(event.pos):
             result.append("green")
         elif hitboxes["blue"].collidepoint(event.pos):
             result.append("blue")