import pygame
from pygame.sprite import Sprite
from Movement import move

class Infect(Sprite):
    '''носители вируса'''
    def __init__(self, screen, settings_obj):
        super().__init__()
        self.settings_obj=settings_obj
        self.image=pygame.image.load('images/infect_org.bmp')
        self.original=self.image
        self.image.set_colorkey((212, 48, 53))
        self.rect=self.image.get_rect()
        screen_rect=screen.get_rect()
        self.rect.topright=screen_rect.topright
        self.float_x_rect=float(self.rect.centerx)
        self.float_y_rect=float(self.rect.centery)
        self.type='infect'
        self.immunity_rnd=settings_obj.peac_rnd
    
    def update(self):
        self.image, self.float_x_rect, self.float_y_rect=move(self.settings_obj, self.image,
        self.original, self.rect, self.float_x_rect, self.float_y_rect, 2)
        self.rect.centerx=self.float_x_rect
        self.rect.centery=self.float_y_rect
