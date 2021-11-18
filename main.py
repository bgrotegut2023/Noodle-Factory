import pygame
import sys

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1220,720))
        self.backgroundColor = (255,255,255)
        self.activate = True;

        self.menuItems = [];
        

    def checkKeyDownEvents(self,event):
        return
            
    


    def checkEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                checkKeyDownEvents(event)
            if event.type == pygame.QUIT:
                sys.exit()
            
    
    def updateGame(self):
        self.screen.fill(self.backgroundColor)
        pygame.display.flip()
    
    def runGame(self):
        while self.activate:
            self.updateGame();
            self.checkEvents();

if __name__ == "__main__":
    game = Game();
    game.runGame();