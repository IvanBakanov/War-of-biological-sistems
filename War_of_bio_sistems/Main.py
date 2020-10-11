import pygame
from Settings import Settings
import Game_functions as gf
from pygame.sprite import Group

pygame.init()
settings_obj=Settings()

# Создаем поверхность игры
screen=pygame.display.set_mode((settings_obj.screen_w, settings_obj.screen_h))
pygame.display.set_caption(settings_obj.screen_caption)
bg_color=settings_obj.screen_color

# Количество организмов
num_peac=50
num_infect=100
num_heal=50
num_war=50

# Создаем группы организмов
peac_gr=Group()
gf.do_peac_group(screen, settings_obj, num_peac, peac_gr)
infect_gr=Group()
gf.do_infect_group(screen, settings_obj, num_infect, infect_gr)
heal_gr=Group()
gf.do_heal_group(screen, settings_obj, num_heal, heal_gr)
war_gr=Group()
gf.do_war_group(screen, settings_obj, num_war, war_gr)

# Основной цикл игры
while True:
    events=pygame.event.get()
    # Отслеживаем события
    gf.check_events(events)
    # Обновляем скорость игры
    sum_=sum([len(peac_gr), len(infect_gr), len(heal_gr), len(war_gr)])
    settings_obj.org_speed=sum_/50
    settings_obj.warlike_org_speed=settings_obj.org_speed/10
    # Обновляем позиции организмов
    gf.update_peac(peac_gr)
    gf.update_infect(screen, settings_obj, infect_gr, peac_gr, heal_gr, war_gr)
    gf.update_heal(heal_gr)
    gf.update_war(war_gr)
    # Рисуем объекты
    gf.screen_draw(screen, bg_color, peac_gr, infect_gr, heal_gr, war_gr)
