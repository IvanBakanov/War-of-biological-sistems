import pygame
from random import randint as rnd

def move(settings_obj, image, original, rect, float_x_rect, float_y_rect, side):
    rnd_=rnd(1, 5)
    if rnd_==1:
        if float_x_rect+settings_obj.org_speed<=settings_obj.screen_w:
            float_x_rect+=settings_obj.org_speed
            if float_x_rect<settings_obj.screen_w/2:
                if side==3:
                    float_x_rect+=settings_obj.develop_speed+0.2
                elif side==4:
                    float_x_rect+=settings_obj.warlike_org_speed
    elif rnd_==2:
        if float_x_rect-settings_obj.org_speed>=0:
            float_x_rect-=settings_obj.org_speed
            if float_x_rect>settings_obj.screen_w/2:
                if side==1 or side==2:
                    float_x_rect-=settings_obj.develop_speed+0.2
    elif rnd_==3:
        if float_y_rect+settings_obj.org_speed<=settings_obj.screen_h:
            float_y_rect+=settings_obj.org_speed
            if float_y_rect<settings_obj.screen_h/2:
                if side==2 or side==3:
                    float_y_rect+=settings_obj.develop_speed
    elif rnd_==4:
        if float_y_rect-settings_obj.org_speed>=0:
            float_y_rect-=settings_obj.org_speed
            if float_y_rect>settings_obj.screen_h/2:
                if side==1:
                    float_y_rect-=settings_obj.develop_speed
                elif side==4:
                    float_y_rect-=settings_obj.warlike_org_speed
    else:
        rnd_=rnd(1, 2)
        if rnd_==1:
            image=pygame.transform.rotate(original, settings_obj.org_rot_speed)
        else:
            image=pygame.transform.rotate(original, -settings_obj.org_rot_speed)
    return image, float_x_rect, float_y_rect
