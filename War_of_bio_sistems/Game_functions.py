import sys
import pygame
from random import randint as rnd
from Class_peaceful import Peaceful
from Class_infect import Infect
from Class_healing import Healing
from Class_warlike import Warlike

def check_events(events):
    for event in events:
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

def update_peac(peac_gr):
    peac_gr.update()

def update_infect(screen, settings_obj, infect_gr, peac_gr, heal_gr, war_gr):
    infect_gr.update()
    for sprite in infect_gr.sprites():
        see_collis_peac(sprite, screen, settings_obj, peac_gr, infect_gr)
        see_collis_heal(sprite, screen, settings_obj, peac_gr, heal_gr, war_gr, infect_gr)
        see_collis_war(sprite, screen, settings_obj, war_gr, infect_gr)
        rnd_1=rnd(1, settings_obj.live_rnd)
        rnd_2=rnd(1, settings_obj.die_rnd)
        if rnd_1==settings_obj.live_rnd:
            check_org_type(sprite, screen, settings_obj, peac_gr, heal_gr, war_gr, infect_gr)
        if rnd_2==settings_obj.die_rnd:
            infect_gr.remove(sprite)     
            
def see_collis_peac(sprite, screen, settings_obj, peac_gr, infect_gr):
    list_1=pygame.sprite.spritecollide(sprite, peac_gr, False)
    if len(list_1)>0:
        for i in list_1:
            rnd_=rnd(1, i.immunity_rnd)
            if rnd_==i.immunity_rnd:
                do_infect(i, screen, settings_obj, infect_gr)
                peac_gr.remove(i)

def see_collis_heal(sprite, screen, settings_obj, peac_gr, heal_gr, war_gr, infect_gr):
    list_2=pygame.sprite.spritecollide(sprite, heal_gr, False)
    if len(list_2)>0:
        for i in list_2:
            rnd_=rnd(1, i.immunity_rnd)
            if rnd_==i.immunity_rnd:
                do_infect(i, screen, settings_obj, infect_gr)
                heal_gr.remove(i)
            elif rnd_<=settings_obj.heal_rnd/300:
                check_org_type(sprite, screen, settings_obj, peac_gr, heal_gr, war_gr, infect_gr)

def see_collis_war(sprite, screen, settings_obj, war_gr, infect_gr):
    list_3=pygame.sprite.spritecollide(sprite, war_gr, False)
    if len(list_3)>0:
        for i in list_3:
            rnd_=rnd(1, i.immunity_rnd)
            if rnd_==i.immunity_rnd:
                do_infect(i, screen, settings_obj, infect_gr)
                war_gr.remove(i)
            elif rnd_<=settings_obj.war_rnd/300:
                infect_gr.remove(sprite)

def do_infect(i, screen, settings_obj, infect_gr):
    new_infect_obj=Infect(screen, settings_obj)
    new_infect_obj.float_x_rect, new_infect_obj.float_y_rect=i.float_x_rect, i.float_y_rect
    new_infect_obj.type=i.type
    new_infect_obj.immunity_rnd=i.immunity_rnd
    infect_gr.add(new_infect_obj)

def check_org_type(sprite, screen, settings_obj, peac_gr, heal_gr, war_gr, infect_gr):
    if sprite.type=='peac' or sprite.type=='infect':
        new_sprite=Peaceful(screen, settings_obj)
        peac_gr.add(new_sprite)
    elif sprite.type=='heal':
        new_sprite=Healing(screen, settings_obj)
        heal_gr.add(new_sprite)
    elif sprite.type=='war':
        new_sprite=Warlike(screen, settings_obj)
        war_gr.add(new_sprite)
    new_sprite.float_x_rect, new_sprite.float_y_rect=sprite.float_x_rect, sprite.float_y_rect
    new_sprite.immunity_rnd=sprite.immunity_rnd+settings_obj.immunity_step
    infect_gr.remove(sprite)

def update_heal(heal_gr):
    heal_gr.update()

def update_war(war_gr):
    war_gr.update()

def do_peac_group(screen, settings_obj, num_peac, peac_gr):
    for i in range(num_peac):
        peac_obj=Peaceful(screen, settings_obj)
        peac_gr.add(peac_obj)

def do_infect_group(screen, settings_obj, num_infect, infect_gr):
    for i in range(num_infect):
        infect_obj=Infect(screen, settings_obj)
        infect_gr.add(infect_obj)

def do_heal_group(screen, settings_obj, num_heal, heal_gr):
    for i in range(num_heal):
        heal_obj=Healing(screen, settings_obj)
        heal_gr.add(heal_obj)

def do_war_group(screen, settings_obj, num_war, war_gr):
    for i in range(num_war):
        war_obj=Warlike(screen, settings_obj)
        war_gr.add(war_obj)

def update_textinput(events, textinput):
    if textinput.update(events):
        print(textinput.get_text())

def screen_draw(screen, bg_color, peac_gr, infect_gr, heal_gr, war_gr):
    screen.fill(bg_color)
    peac_gr.draw(screen)
    heal_gr.draw(screen)
    war_gr.draw(screen)
    infect_gr.draw(screen)
    pygame.display.flip()
