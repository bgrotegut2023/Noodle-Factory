import pygame
import sys

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.setMode((1920,1080))
        self.backgroundColor = (0,0,0)
        self.activate = True;

    def checkKeyDownEvents(event):
        if event.type == pygame.K_q:
            sys.exit()
            


    def checkEvents():
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                checkKeyDownEvents(event)
    
    def updateGame():
        self.screen.fill(self.backgroundColor)
    
    def runGame():
        while self.activate:
            updateGame()
        