class Settings():
    
    '''НАСТРОЙКИ ИГРЫ'''
    def __init__(self):

        # Настройки экрана
        self.screen_w=600
        self.screen_h=500
        self.screen_caption='War of biological sistems'
        self.screen_color=(128, 128, 128)
        
        # Настройки организмов
        self.org_speed=2.5
        self.org_rot_speed=0
        self.develop_speed=0.3
        self.peac_rnd=2000
        self.heal_rnd=2000
        self.war_rnd=2000
        self.live_rnd=50000
        self.die_rnd=30000
        self.immunity_step=10
        self.warlike_org_speed=0
        
