from random import choice
import pygame

class SE:
    def __init__(self):

        self.sound_switch = 1
        # 0 EMP www C   
        # 1 Tornado qww X
        # 2 Alacrity wwe Z  
        # 3 Ghost Walk qqw V    
        # 4 Deafening Blast qwe B   
        # 5 Chaos Meteor wee D  
        # 6 Cold Snap qqq Y 
        # 7 Ice Wall qqe G  
        # 8 Forge Spirirt qee F 
        # 9 Sun Strike eee T

        #     self.skill_dict = {'0':'EMP', '1':'Tornado', '2':'Alacrity', '3':'Ghost Walk', '4':'Deafening Blast', \
        # '5':'Chaos Meteor', '6':'Cold Snap', '7':'Ice Wall', '8':'Forge Spirit', '9':'Sun Strike'}
        self.EMP_sound =                pygame.mixer.Sound("assets/sound/skill_sounds/EMP.mp3.mpeg")
        self.Tornado_sound =            pygame.mixer.Sound("assets/sound/skill_sounds/Tornado_cast.mp3.mpeg")
        self.Alacrity_sound =           pygame.mixer.Sound("assets/sound/skill_sounds/Alacrity.mp3.mpeg")
        self.Ghost_Walk_sound =         pygame.mixer.Sound("assets/sound/skill_sounds/Ghost_Walk.mp3.mpeg")
        self.Deafening_Blast_sound =    pygame.mixer.Sound("assets/sound/skill_sounds/Deafening_Blast.mp3.mpeg")
        self.Choas_Meteor_sound =       pygame.mixer.Sound("assets/sound/skill_sounds/Chaos_Meteor.mp3.mpeg")
        self.Cold_Snap_sound =          pygame.mixer.Sound("assets/sound/skill_sounds/Cold_Snap.mp3.mpeg")
        self.Ice_Wall_sound =           pygame.mixer.Sound("assets/sound/skill_sounds/Ice_Wall.mp3.mpeg")
        self.Forge_Spirit_sound =       pygame.mixer.Sound("assets/sound/skill_sounds/Forge_Spirit.mp3.mpeg")
        self.Sun_Strike_sound =         pygame.mixer.Sound("assets/sound/skill_sounds/Sun_Strike.mp3.mpeg")
        self.Invoke_sound =             pygame.mixer.Sound("assets/sound/skill_sounds/Invoke.mp3.mpeg")

        self.background_music_select = choice(range(1, 19))

        self.Invo_attack_01_zh = pygame.mixer.Sound("assets/sound/dialog/Invo_attack_01_zh.mp3.mp3")
        self.Invo_attack_06_zh = pygame.mixer.Sound("assets/sound/dialog/Invo_attack_06_zh.mp3.mp3")
        self.Invo_attack_08_zh = pygame.mixer.Sound("assets/sound/dialog/Invo_attack_08_zh.mp3.mp3")
        self.Invo_attack_09_zh = pygame.mixer.Sound("assets/sound/dialog/Invo_attack_09_zh.mp3.mp3")
        self.Invo_attack_12_zh = pygame.mixer.Sound("assets/sound/dialog/Invo_attack_12_zh.mp3.mp3")

        self.Invo_attack_list = [self.Invo_attack_01_zh, self.Invo_attack_06_zh, self.Invo_attack_08_zh, self.Invo_attack_09_zh, self.Invo_attack_12_zh]

        self.Invo_failure_01_zh = pygame.mixer.Sound("assets/sound/dialog/Invo_failure_01_zh.mp3.mp3")
        self.Invo_failure_02_zh = pygame.mixer.Sound("assets/sound/dialog/Invo_failure_02_zh.mp3.mp3")
        self.Invo_failure_03_zh = pygame.mixer.Sound("assets/sound/dialog/Invo_failure_03_zh.mp3.mp3")
        self.Invo_failure_04_zh = pygame.mixer.Sound("assets/sound/dialog/Invo_failure_04_zh.mp3.mp3")
        self.Invo_failure_05_zh = pygame.mixer.Sound("assets/sound/dialog/Invo_failure_05_zh.mp3.mp3")
        self.Invo_failure_06_zh = pygame.mixer.Sound("assets/sound/dialog/Invo_failure_06_zh.mp3.mp3")
        self.Invo_failure_09_zh = pygame.mixer.Sound("assets/sound/dialog/Invo_failure_09_zh.mp3.mp3")
        self.Invo_failure_10_zh = pygame.mixer.Sound("assets/sound/dialog/Invo_failure_10_zh.mp3.mp3")
        self.Invo_failure_11_zh = pygame.mixer.Sound("assets/sound/dialog/Invo_failure_11_zh.mp3.mp3")
        self.Invo_failure_12_zh = pygame.mixer.Sound("assets/sound/dialog/Invo_failure_12_zh.mp3.mp3")

        self.Invo_failure_list = [self.Invo_failure_01_zh, self.Invo_failure_02_zh, self.Invo_failure_03_zh, 
        self.Invo_failure_04_zh, self.Invo_failure_05_zh, self.Invo_failure_06_zh, 
        self.Invo_failure_09_zh, self.Invo_failure_10_zh, self.Invo_failure_11_zh, 
        self.Invo_failure_12_zh]

        self.Invo_level_10_zh = pygame.mixer.Sound("assets/sound/dialog/Invo_level_10_zh.mp3.mp3")
        self.Invo_level_12_zh = pygame.mixer.Sound("assets/sound/dialog/Invo_level_12_zh.mp3.mp3")

        self.Invo_level_list = [self.Invo_level_10_zh, self.Invo_level_12_zh]

        self.Invo_spawn_02_zh = pygame.mixer.Sound("assets/sound/dialog/Invo_spawn_02_zh.mp3.mp3")
        self.Invo_spawn_03_zh = pygame.mixer.Sound("assets/sound/dialog/Invo_spawn_03_zh.mp3.mp3")
        self.Invo_spawn_04_zh = pygame.mixer.Sound("assets/sound/dialog/Invo_spawn_04_zh.mp3.mp3")
        self.Invo_spawn_05_zh = pygame.mixer.Sound("assets/sound/dialog/Invo_spawn_05_zh.mp3.mp3")

        self.Invo_spawn_list = [self.Invo_spawn_02_zh, self.Invo_spawn_03_zh, self.Invo_spawn_04_zh, self.Invo_spawn_05_zh]

        self.Invo_cast_01_zh = pygame.mixer.Sound("assets/sound/dialog/Invo_cast_01_zh.mp3.mp3")
        self.Invo_cast_02_zh = pygame.mixer.Sound("assets/sound/dialog/Invo_cast_02_zh.mp3.mp3")
        self.Invo_cast_03_zh = pygame.mixer.Sound("assets/sound/dialog/Invo_cast_03_zh.mp3.mp3")

        self.Invo_cast_list = [self.Invo_cast_01_zh, self.Invo_cast_02_zh, self.Invo_cast_03_zh]

    def play(self, skill):
        # pygame.mixer.Sound.set_volume(0.5)
        match skill:
            case 'EMP':                pygame.mixer.Sound.play(self.EMP_sound)                  .set_volume(0.5)
            case 'Tornado':            pygame.mixer.Sound.play(self.Tornado_sound)              .set_volume(0.5)
            case 'Alacrity':           pygame.mixer.Sound.play(self.Alacrity_sound)             .set_volume(0.5)
            case 'Ghost Walk':         pygame.mixer.Sound.play(self.Ghost_Walk_sound)           .set_volume(0.5)
            case 'Deafening Blast':    pygame.mixer.Sound.play(self.Deafening_Blast_sound)      .set_volume(0.5)
            case 'Chaos Meteor':       pygame.mixer.Sound.play(self.Choas_Meteor_sound)         .set_volume(0.5)
            case 'Cold Snap':          pygame.mixer.Sound.play(self.Cold_Snap_sound)            .set_volume(0.5)
            case 'Ice Wall':           pygame.mixer.Sound.play(self.Ice_Wall_sound)             .set_volume(0.5)
            case 'Forge Spirit':       pygame.mixer.Sound.play(self.Forge_Spirit_sound)         .set_volume(0.5)
            case 'Sun Strike':         pygame.mixer.Sound.play(self.Sun_Strike_sound)           .set_volume(0.5)
            case 'Invoke':             pygame.mixer.Sound.play(self.Invoke_sound)               .set_volume(0.5)

    def play_dialog(self, situation):
        if situation == 'attack':
            pygame.mixer.Sound.play(choice(self.Invo_attack_list))

        if situation == 'failure':
            pygame.mixer.Sound.play(choice(self.Invo_failure_list))

        if situation == 'high_scoure':
            pygame.mixer.Sound.play(choice(self.Invo_level_list))

        if situation == 'spawn':
            pygame.mixer.Sound.play(choice(self.Invo_spawn_list))

        if situation == 'cast':
            pygame.mixer.Sound.play(choice(self.Invo_cast_list))

    def play_music(self, stage):
        pygame.mixer.music.set_volume(0.3)
        if self.sound_switch:
            if stage == 'start':
                pygame.mixer.music.load("assets\sound\music"+"\\"+str(self.background_music_select)+" (1).mp3")
                pygame.mixer.music.play(-1)
            if stage == 'end':
                pygame.mixer.music.load("assets\sound\music"+"\\"+str(self.background_music_select)+" (2).mp3")
                pygame.mixer.music.play()
            if stage == 'stop':
                pygame.mixer.music.stop()

    def reset_music(self):
        self.background_music_select = choice(range(1, 19))
