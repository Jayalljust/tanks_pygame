import pygame

class Tank():

    def __init__(self,screen):
        '''инициализация танка'''

        self.screen = screen
        self.image = pygame.image.load('images/Player tank.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx

    def display (self):
        '''рисует танк'''
        self.screen.blit(self.image, self.rect)
