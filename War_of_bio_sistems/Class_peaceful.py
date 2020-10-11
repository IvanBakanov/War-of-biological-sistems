import pygame
from random import randint as rnd
from pygame.sprite import Sprite
from Movement import move

class Peaceful(Sprite):
    '''мирные организмы'''
    def __init__(self, screen, settings_obj):
        super().__init__()
        self.settings_obj=settings_obj
        self.image=pygame.image.load('images/peaceful_org.bmp')
        self.original=self.image
        self.image.set_colorkey((29, 175, 100))
        self.rect=self.image.get_rect()
        screen_rect=screen.get_rect()
        self.rect.bottomright=screen_rect.bottomright
        self.float_x_rect=float(self.rect.centerx)
        self.float_y_rect=float(self.rect.centery)
        self.type='peac'
        self.immunity_rnd=settings_obj.peac_rnd
    
    def update(self):
        self.image, self.float_x_rect, self.float_y_rect=move(self.settings_obj, self.image,
        self.original, self.rect, self.float_x_rect, self.float_y_rect, 1)
        self.rect.centerx=self.float_x_rect
        self.rect.centery=self.float_y_rect

            



                    
