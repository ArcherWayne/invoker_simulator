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
        self.EMP_sound = pygame.mixer.Sound("assets/sound/skill_sounds/EMP.mp3.mpeg")
        self.Tornado_sound = pygame.mixer.Sound("assets/sound/skill_sounds/Tornado_cast.mp3.mpeg")
        self.Alacrity_sound = pygame.mixer.Sound("assets/sound/skill_sounds/Alacrity.mp3.mpeg")
        self.Ghost_Walk_sound = pygame.mixer.Sound("assets/sound/skill_sounds/Ghost_Walk.mp3.mpeg")
        self.Deafening_Blast_sound = pygame.mixer.Sound("assets/sound/skill_sounds/Deafening_Blast.mp3.mpeg")
        self.Choas_Meteor_sound = pygame.mixer.Sound("assets/sound/skill_sounds/Chaos_Meteor.mp3.mpeg")
        self.Cold_Snap_sound = pygame.mixer.Sound("assets/sound/skill_sounds/Cold_Snap.mp3.mpeg")
        self.Ice_Wall_sound = pygame.mixer.Sound("assets/sound/skill_sounds/Ice_Wall.mp3.mpeg")
        self.Forge_Spirit_sound = pygame.mixer.Sound("assets/sound/skill_sounds/Forge_Spirit.mp3.mpeg")
        self.Sun_Strike_sound = pygame.mixer.Sound("assets/sound/skill_sounds/Sun_Strike.mp3.mpeg")
        self.Invoke_sound = pygame.mixer.Sound("assets/sound/skill_sounds/Invoke.mp3.mpeg")

    def play(self, skill):
        match skill:
            case 'EMP': pygame.mixer.Sound.play(self.EMP_sound)
            case 'Tornado': pygame.mixer.Sound.play(self.Tornado_sound)
            case 'Alacrity': pygame.mixer.Sound.play(self.Alacrity_sound)
            case 'Ghost Walk': pygame.mixer.Sound.play(self.Ghost_Walk_sound)
            case 'Deafening Blast': pygame.mixer.Sound.play(self.Deafening_Blast_sound)
            case 'Chaos Meteor': pygame.mixer.Sound.play(self.Choas_Meteor_sound)
            case 'Cold Snap': pygame.mixer.Sound.play(self.Cold_Snap_sound)
            case 'Ice Wall': pygame.mixer.Sound.play(self.Ice_Wall_sound)
            case 'Forge Spirit': pygame.mixer.Sound.play(self.Forge_Spirit_sound)
            case 'Sun Strike': pygame.mixer.Sound.play(self.Sun_Strike_sound)
            case 'Invoke': pygame.mixer.Sound.play(self.Invoke_sound)

            case 'battle_02_end': pygame.mixer.Sound.play

    def play_music(self, stage):
        pygame.mixer.music.set_volume(0.1)
        if self.sound_switch:
            if stage == 'start':
                pygame.mixer.music.load("assets\sound\music/Music_default_battle_02.mp3")
                pygame.mixer.music.play(-1)
            if stage == 'end':
                pygame.mixer.music.load("assets\sound\music/Music_default_battle_02_end.mp3")
                pygame.mixer.music.play()
            if stage == 'stop':
                pygame.mixer.music.stop()

            
