#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: colecurtis.22
"""
import pygame
pygame.init()

screen = pygame.display.set_mode((600, 400))

blue = (0, 0, 255)
red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)

font = pygame.font.SysFont("Arial", 30)

class Surface:
    def __init__(self, questionText, shape1color, shape2color):
        self.surface = pygame.Surface((600, 400))
        self.surface.fill(white)
        
        qText = font.render(questionText, True, black)
        self.surface.blit(qText, (50, 50))
        
        self.rect = pygame.draw.rect(self.surface, shape1color, (150, 200, 120, 120))
        self.circle = pygame.draw.circle(self.surface, shape2color, (370, 260), 50)
        

surface1 = Surface("Click the Blue Shape", blue, red)

surface2 = Surface("Click the Green Shape", red, green)

surface3 = Surface("Click the Red Shape", green, red)

keepGoing = True
screen.blit(surface1.surface, (0, 0))
pygame.display.flip()
currentSurface = 1
wrongShowing = False
rightSelected = False
acceptClicks = True

surface4 = pygame.Surface((600, 400))
surface4.fill(white)
winText = font.render("You win! Click anywhere to quit", True, black)
surface4.blit(winText, (50, 50))

while keepGoing:
    wrong = font.render("Not Quite!", True, (black))
    correct = font.render("Correct!", True, (black))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepGoing = False
            
        if event.type == pygame.MOUSEBUTTONDOWN and acceptClicks:
            if currentSurface == 1:
                if rightSelected == False:
                    if surface1.rect.collidepoint(event.pos):
                        rightSelected = True
                        surface1.surface.blit(correct, (50, 150))
                        screen.blit(surface1.surface, (0, 0))
                        pygame.display.flip()
                        acceptClicks = False
                        pygame.time.wait(3000) 
                    
                        currentSurface = 2
                        screen.blit(surface2.surface, (0, 0))
                        pygame.display.flip()
                        acceptClicks = True
                        rightSelected = False
                        wrongShowing = False
                        
                if wrongShowing == False:
                    if surface1.circle.collidepoint(event.pos):
                        surface1.surface.blit(wrong, (50, 350))
                        screen.blit(surface1.surface, (0, 0))
                        pygame.display.flip()
                        wrongShowing = True
                    
            elif currentSurface == 2:
                if rightSelected == False:
                    if surface2.circle.collidepoint(event.pos):
                        rightSelected = True
                        surface2.surface.blit(correct, (50, 150))
                        screen.blit(surface2.surface, (0, 0))
                        pygame.display.flip()
                        acceptClicks = False
                        pygame.time.wait(3000)
                    
                        currentSurface = 3
                        screen.blit(surface3.surface, (0, 0))
                        pygame.display.flip()
                        acceptClicks = True
                        rightSelected = False
                        wrongShowing = False
                        
                if wrongShowing == False:
                    if surface2.rect.collidepoint(event.pos):
                        surface2.surface.blit(wrong, (50, 350))
                        screen.blit(surface2.surface, (0, 0))
                        pygame.display.flip()
                        wrongShowing = True
                        
                    
            elif currentSurface == 3:
                if rightSelected == False:
                    if surface3.circle.collidepoint(event.pos):
                        rightSelected = True
                        surface3.surface.blit(correct, (50, 150))
                        screen.blit(surface3.surface, (0, 0))
                        pygame.display.flip()
                        acceptClicks = False
                        pygame.time.wait(3000)
                    
                        currentSurface = 4
                        screen.blit(surface4, (0, 0))
                        pygame.display.flip()
                        acceptClicks = True
                        rightSelected = False
                        wrongShowing = False
                        
                if wrongShowing == False:
                    if surface3.rect.collidepoint(event.pos):
                        surface3.surface.blit(wrong, (50, 350))
                        screen.blit(surface3.surface, (0, 0))
                        pygame.display.flip()
                        wrongShowing = True
            
            elif currentSurface == 4:
                pygame.time.wait(1000)
                keepGoing = False
pygame.quit()