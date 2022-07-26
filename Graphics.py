
import pygame
from setting import * 

class Graphics:
    def __init__(self, group):
        # super(Graphics, self).__init__(groups)
        self.orbs_dict = {'0':'Quas', '1':'Wex', '2':'Extort'}
        self.skill_dict = {'0':'EMP', '1':'Tornado', '2':'Alacrity', '3':'Ghost Walk', '4':'Deafening Blast', \
            '5':'Chaos Meteor', '6':'Cold Snap', '7':'Ice Wall', '8':'Forge Spirit', '9':'Sun Strike'}
        self.skill_dict_reverse = {'EMP':'0', 'Tornado':'1', 'Alacrity':'2', 'Ghost Walk':'3', 'Deafening Blast':'4', \
            'Chaos Meteor':'5', 'Cold Snap':'6', 'Ice Wall':'7', 'Forge Spirit':'8', 'Sun Strike':'9', '':''}
        self.key_dict = {'0':'C', '1':'X', '2':'Z', '3':'V', '4':'B', '5':'D', '6':'Y', '7':'G', '8':'F', '9':'T', '':''}
        self.comb_dict = {'EMP':'WWW', 'Tornado':'QWW', 'Alacrity':'WWE', 'Ghost Walk':'QQW', 'Deafening Blast':'QWE', \
            'Chaos Meteor':'WEE', 'Cold Snap':'QQQ', 'Ice Wall':'QQE', 'Forge Spirit':'QEE', 'Sun Strike':'EEE'}
        self.skill_key_surf = ['', '']
        self.skill_key_rect = ['', '']
        self.drop_skill_group = group

        # font
        self.game_font = pygame.font.Font('assets/font/HuaGuangGangTieZhiHei-KeBianTi-2.ttf', 25)

        # self.obtained_orbs = ['Quas', 'Quas', 'Quas']
        # self.obtained_orbs = ['', '', '']

        # image
        # self.image = pygame.Surface(player_size)
        # self.image.fill('#345678')
        self.Alacrity_image = pygame.image.load('assets/graphics/Alacrity.png').convert_alpha()
        self.Alacrity_image_slot = pygame.transform.scale(self.Alacrity_image, slot_size)
        self.Alacrity_image_skill = pygame.transform.scale(self.Alacrity_image, skill_size)
        self.ChaosMeteor_image = pygame.image.load('assets/graphics/Chaos Meteor.png').convert_alpha()
        self.ChaosMeteor_image_slot = pygame.transform.scale(self.ChaosMeteor_image, slot_size)
        self.ChaosMeteor_image_skill = pygame.transform.scale(self.ChaosMeteor_image, skill_size)
        self.ColdSnap_image = pygame.image.load('assets/graphics/Cold Snap.png').convert_alpha()
        self.ColdSnap_image_slot = pygame.transform.scale(self.ColdSnap_image, slot_size)
        self.ColdSnap_image_skill = pygame.transform.scale(self.ColdSnap_image, skill_size)
        self.DeafeningBlast_image = pygame.image.load('assets/graphics/Deafening Blast.png').convert_alpha()
        self.DeafeningBlast_image_slot = pygame.transform.scale(self.DeafeningBlast_image, slot_size)
        self.DeafeningBlast_image_skill = pygame.transform.scale(self.DeafeningBlast_image, skill_size)
        self.EMP_image = pygame.image.load('assets/graphics/EMP.png').convert_alpha()
        self.EMP_image_slot = pygame.transform.scale(self.EMP_image, slot_size)
        self.EMP_image_skill = pygame.transform.scale(self.EMP_image, skill_size)
        self.Extort_image = pygame.image.load('assets/graphics/Extort.png').convert_alpha()
        self.Extort_image_slot = pygame.transform.scale(self.Extort_image, slot_size)
        self.Extort_image_skill = pygame.transform.scale(self.Extort_image, skill_size)
        self.ForgeSpirit_image = pygame.image.load('assets/graphics/Forge Spirit.png').convert_alpha()
        self.ForgeSpirit_image_slot = pygame.transform.scale(self.ForgeSpirit_image, slot_size)
        self.ForgeSpirit_image_skill = pygame.transform.scale(self.ForgeSpirit_image, skill_size)
        self.GhostWalk_image = pygame.image.load('assets/graphics/Ghost Walk.png').convert_alpha()
        self.GhostWalk_image_slot = pygame.transform.scale(self.GhostWalk_image, slot_size)
        self.GhostWalk_image_skill = pygame.transform.scale(self.GhostWalk_image, skill_size)
        self.IceWall_image = pygame.image.load('assets/graphics/Ice Wall.png').convert_alpha()
        self.IceWall_image_slot = pygame.transform.scale(self.IceWall_image, slot_size)
        self.IceWall_image_skill = pygame.transform.scale(self.IceWall_image, skill_size)
        self.Invoke_image = pygame.image.load('assets/graphics/Invoke.png').convert_alpha()
        self.Invoke_image_slot = pygame.transform.scale(self.Invoke_image, slot_size)
        self.Invoke_image_skill = pygame.transform.scale(self.Invoke_image, skill_size)
        self.Quas_image = pygame.image.load('assets/graphics/Quas.png').convert_alpha()
        self.Quas_image_slot = pygame.transform.scale(self.Quas_image, slot_size)
        self.Quas_image_skill = pygame.transform.scale(self.Quas_image, skill_size)
        self.SunStrike_image = pygame.image.load('assets/graphics/Sun Strike.png').convert_alpha()
        self.SunStrike_image_slot = pygame.transform.scale(self.SunStrike_image, slot_size)
        self.SunStrike_image_skill = pygame.transform.scale(self.SunStrike_image, skill_size)
        self.Tornado_image = pygame.image.load('assets/graphics/Tornado.png').convert_alpha()
        self.Tornado_image_slot = pygame.transform.scale(self.Tornado_image, slot_size)
        self.Tornado_image_skill = pygame.transform.scale(self.Tornado_image, skill_size)
        self.Wex_image = pygame.image.load('assets/graphics/Wex.png').convert_alpha()
        self.Wex_image_slot = pygame.transform.scale(self.Wex_image, slot_size)
        self.Wex_image_skill = pygame.transform.scale(self.Wex_image, skill_size)

        self.Quas_image_icon = pygame.transform.scale(self.Quas_image, icon_size)
        self.Wex_image_icon = pygame.transform.scale(self.Wex_image, icon_size)
        self.Extort_image_icon = pygame.transform.scale(self.Extort_image, icon_size)

        # self.skill_image_dict 
        self.skill_image_slot_dict = {'0':self.EMP_image_slot, '1':self.Tornado_image_slot, '2':self.Alacrity_image_slot, '3':self.GhostWalk_image_slot, '4':self.DeafeningBlast_image_slot, 
            '5':self.ChaosMeteor_image_slot, '6':self.ColdSnap_image_slot, '7':self.IceWall_image_slot, '8':self.ForgeSpirit_image_slot, '9':self.SunStrike_image_slot}
        self.skill_image_skill_dict = {'0':self.EMP_image_skill, '1':self.Tornado_image_skill, '2':self.Alacrity_image_skill, '3':self.GhostWalk_image_skill, '4':self.DeafeningBlast_image_skill, 
            '5':self.ChaosMeteor_image_skill, '6':self.ColdSnap_image_skill, '7':self.IceWall_image_skill, '8':self.ForgeSpirit_image_skill, '9':self.SunStrike_image_skill}
        self.skill_image_icon_dict = {'0':self.Quas_image_icon, '1':self.Wex_image_icon, '2':self.Extort_image_icon}

        # rect
        self.Quas_slot_rect = self.Quas_image_slot.get_rect(topleft = (35, 690))
        self.Wex_slot_rect = self.Wex_image_slot.get_rect(topleft = (125, 690))
        self.Extort_slot_rect = self.Extort_image_slot.get_rect(topleft = (215, 690))
        self.Invoke_slot_rect = self.Invoke_image_slot.get_rect(topleft = (305, 690))
        self.slot_1_rect = pygame.Rect((395, 690), slot_size)
        self.slot_2_rect = pygame.Rect((485, 690), slot_size)
        self.icon_1_rect = pygame.Rect((230, 630), icon_size)
        self.icon_2_rect = pygame.Rect((280, 630), icon_size)
        self.icon_3_rect = pygame.Rect((330, 630), icon_size)

        # keys
        q_text = 'Q'
        self.q_surf = self.game_font.render(q_text, True, Q_COLOR)
        q_topleft = self.Quas_slot_rect.topleft
        self.q_rect = self.q_surf.get_rect(topleft = q_topleft)
        w_text = 'W'
        self.w_surf = self.game_font.render(w_text, True, W_COLOR)
        w_topleft = self.Wex_slot_rect.topleft
        self.w_rect = self.w_surf.get_rect(topleft = w_topleft)
        e_text = 'E'
        self.e_surf = self.game_font.render(e_text, True, E_COLOR)
        e_topleft = self.Extort_slot_rect.topleft
        self.e_rect = self.e_surf.get_rect(topleft = e_topleft)
        r_text = 'R'
        self.r_surf = self.game_font.render(r_text, True, WHITE)
        r_topleft = self.Invoke_slot_rect.topleft
        self.r_rect = self.r_surf.get_rect(topleft = r_topleft)

        self.slot_key_topleft = []
        self.slot_key_topleft.append(self.slot_1_rect.topleft)
        self.slot_key_topleft.append(self.slot_2_rect.topleft)


    def obtain_info(self, slot, orb):
        self.slot = slot
        self.obtained_orbs = orb


    def draw_slots(self):
        screen.blit(self.Quas_image_slot, self.Quas_slot_rect)
        screen.blit(self.Wex_image_slot, self.Wex_slot_rect)
        screen.blit(self.Extort_image_slot, self.Extort_slot_rect)
        screen.blit(self.Invoke_image_slot, self.Invoke_slot_rect)

        for key in self.skill_dict:
            if self.slot[0] == self.skill_dict[key]:
                screen.blit(self.skill_image_slot_dict[key], self.slot_1_rect)
        for key in self.skill_dict:
            if self.slot[1] == self.skill_dict[key]:
                screen.blit(self.skill_image_slot_dict[key], self.slot_2_rect)


    def draw_icons(self):
        match self.obtained_orbs[0]:
            case 'Quas':
                screen.blit(self.skill_image_icon_dict['0'], self.icon_1_rect)
            case 'Wex':
                screen.blit(self.skill_image_icon_dict['1'], self.icon_1_rect)
            case 'Extort':
                screen.blit(self.skill_image_icon_dict['2'], self.icon_1_rect)
        match self.obtained_orbs[1]:
            case 'Quas':
                screen.blit(self.skill_image_icon_dict['0'], self.icon_2_rect)
            case 'Wex':
                screen.blit(self.skill_image_icon_dict['1'], self.icon_2_rect)
            case 'Extort':
                screen.blit(self.skill_image_icon_dict['2'], self.icon_2_rect)
        match self.obtained_orbs[2]:
            case 'Quas':
                screen.blit(self.skill_image_icon_dict['0'], self.icon_3_rect)
            case 'Wex':
                screen.blit(self.skill_image_icon_dict['1'], self.icon_3_rect)
            case 'Extort':
                screen.blit(self.skill_image_icon_dict['2'], self.icon_3_rect)


    def draw_key(self):
        # -------------------------------------------------------------------------------- #
        screen.blit(self.q_surf, self.q_rect)
        screen.blit(self.w_surf, self.w_rect)
        screen.blit(self.e_surf, self.e_rect)
        screen.blit(self.r_surf, self.r_rect)

        # -------------------------------------------------------------------------------- #
        for i, skill in enumerate(self.slot):
            self.skill_key_surf[i] = self.game_font.render(self.key_dict[self.skill_dict_reverse[str(skill)]], True, WHITE)
            self.skill_key_rect[i] = self.skill_key_surf[i].get_rect(topleft=self.slot_key_topleft[i])
            screen.blit(self.skill_key_surf[i], self.skill_key_rect[i])

        for spirites in self.drop_skill_group:
            drop_skill_name = spirites.skill
            comb = self.comb_dict[drop_skill_name]
            drop_skill_comb_surf = self.game_font.render(comb, True, WHITE)
            drop_skill_comb_rect = drop_skill_comb_surf.get_rect(topleft=spirites.rect.topleft)
            screen.blit(drop_skill_comb_surf, drop_skill_comb_rect)

    def draw_count(self, count):
        count_surf = self.game_font.render('连击:'+str(count), True, RED)
        count_rect = count_surf.get_rect(topleft = (420, 630))
        screen.blit(count_surf, count_rect)

    def draw_score(self, score):
        score_surf = self.game_font.render('分数:'+str(score), True, RED)
        score_rect = score_surf.get_rect(topleft = (30, 630))
        screen.blit(score_surf, score_rect)

    def update(self, count, score):
        self.draw_count(count)
        self.draw_score(score)
        self.draw_slots()
        self.draw_icons()
        self.draw_key()

