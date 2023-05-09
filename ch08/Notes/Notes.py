#Switching game screens
import pygame
import pygame_menu
def mainloop():

    while True:
        if self.state == "GAME":
            self.gameloop()
        elif self.stsate == "END":
            self.endloop()

def endloop():
    font_object = pygame.font.SysFont(None, 48)
    font_object.render("You Won!")

def startloop(self):
    self.menu = pygame_menu.Menu("Start Screen", self.width, self.hight)
    self.menu.add.label("Click to Start Program", font_size = 28)
    self.menu.add.button("Start",self.startgame, align = pygame_menu.locals.ALIGN_CENTER)

while self.state == "START":
    self.menu.update(ptgame.get.events())
    self.menu.draw(self.screen)
    pygame.display.flip()

def startgame(self):
    self.state = "GAME"
