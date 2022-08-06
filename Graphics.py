import pygame
from random import randint, choice
from setting import *


class Graphics:
    def __init__(self, group):
        # super(Graphics, self).__init__(groups)
        self.orbs_dict = {'0': 'Quas', '1': 'Wex', '2': 'Extort'}
        self.skill_dict = {'0': 'EMP', '1': 'Tornado', '2': 'Alacrity', '3': 'Ghost Walk', '4': 'Deafening Blast',
                           '5': 'Chaos Meteor', '6': 'Cold Snap', '7': 'Ice Wall', '8': 'Forge Spirit', '9': 'Sun Strike'}
        self.skill_dict_reverse = {'EMP': '0', 'Tornado': '1', 'Alacrity': '2', 'Ghost Walk': '3', 'Deafening Blast': '4',
                                   'Chaos Meteor': '5', 'Cold Snap': '6', 'Ice Wall': '7', 'Forge Spirit': '8', 'Sun Strike': '9', '': ''}
        self.key_dict = {'0': 'C', '1': 'X', '2': 'Z', '3': 'V', '4': 'B',
                         '5': 'D', '6': 'Y', '7': 'G', '8': 'F', '9': 'T', '': ''}
        self.comb_dict = {'EMP': 'WWW', 'Tornado': 'QWW', 'Alacrity': 'WWE', 'Ghost Walk': 'QQW', 'Deafening Blast': 'QWE',
                          'Chaos Meteor': 'WEE', 'Cold Snap': 'QQQ', 'Ice Wall': 'QQE', 'Forge Spirit': 'QEE', 'Sun Strike': 'EEE'}
        self.skill_key_surf = ['', '']
        self.skill_key_rect = ['', '']
        self.drop_skill_group = group

        # font
        self.game_font = pygame.font.Font(
            'assets/font/HuaGuangGangTieZhiHei-KeBianTi-2.ttf', 25)

        # self.obtained_orbs = ['Quas', 'Quas', 'Quas']
        # self.obtained_orbs = ['', '', '']

        # image
        # self.image = pygame.Surface(player_size)
        # self.image.fill('#345678')
        self.Alacrity_image = pygame.image.load(
            'assets/graphics/Alacrity.png').convert_alpha()
        self.Alacrity_image_slot = pygame.transform.scale(
            self.Alacrity_image, slot_size)
        self.Alacrity_image_skill = pygame.transform.scale(
            self.Alacrity_image, skill_size)
        self.ChaosMeteor_image = pygame.image.load(
            'assets/graphics/Chaos Meteor.png').convert_alpha()
        self.ChaosMeteor_image_slot = pygame.transform.scale(
            self.ChaosMeteor_image, slot_size)
        self.ChaosMeteor_image_skill = pygame.transform.scale(
            self.ChaosMeteor_image, skill_size)
        self.ColdSnap_image = pygame.image.load(
            'assets/graphics/Cold Snap.png').convert_alpha()
        self.ColdSnap_image_slot = pygame.transform.scale(
            self.ColdSnap_image, slot_size)
        self.ColdSnap_image_skill = pygame.transform.scale(
            self.ColdSnap_image, skill_size)
        self.DeafeningBlast_image = pygame.image.load(
            'assets/graphics/Deafening Blast.png').convert_alpha()
        self.DeafeningBlast_image_slot = pygame.transform.scale(
            self.DeafeningBlast_image, slot_size)
        self.DeafeningBlast_image_skill = pygame.transform.scale(
            self.DeafeningBlast_image, skill_size)
        self.EMP_image = pygame.image.load(
            'assets/graphics/EMP.png').convert_alpha()
        self.EMP_image_slot = pygame.transform.scale(self.EMP_image, slot_size)
        self.EMP_image_skill = pygame.transform.scale(
            self.EMP_image, skill_size)
        self.Extort_image = pygame.image.load(
            'assets/graphics/Extort.png').convert_alpha()
        self.Extort_image_slot = pygame.transform.scale(
            self.Extort_image, slot_size)
        self.Extort_image_skill = pygame.transform.scale(
            self.Extort_image, skill_size)
        self.ForgeSpirit_image = pygame.image.load(
            'assets/graphics/Forge Spirit.png').convert_alpha()
        self.ForgeSpirit_image_slot = pygame.transform.scale(
            self.ForgeSpirit_image, slot_size)
        self.ForgeSpirit_image_skill = pygame.transform.scale(
            self.ForgeSpirit_image, skill_size)
        self.GhostWalk_image = pygame.image.load(
            'assets/graphics/Ghost Walk.png').convert_alpha()
        self.GhostWalk_image_slot = pygame.transform.scale(
            self.GhostWalk_image, slot_size)
        self.GhostWalk_image_skill = pygame.transform.scale(
            self.GhostWalk_image, skill_size)
        self.IceWall_image = pygame.image.load(
            'assets/graphics/Ice Wall.png').convert_alpha()
        self.IceWall_image_slot = pygame.transform.scale(
            self.IceWall_image, slot_size)
        self.IceWall_image_skill = pygame.transform.scale(
            self.IceWall_image, skill_size)
        self.Invoke_image = pygame.image.load(
            'assets/graphics/Invoke.png').convert_alpha()
        self.Invoke_image_slot = pygame.transform.scale(
            self.Invoke_image, slot_size)
        self.Invoke_image_skill = pygame.transform.scale(
            self.Invoke_image, skill_size)
        self.Quas_image = pygame.image.load(
            'assets/graphics/Quas.png').convert_alpha()
        self.Quas_image_slot = pygame.transform.scale(
            self.Quas_image, slot_size)
        self.Quas_image_skill = pygame.transform.scale(
            self.Quas_image, skill_size)
        self.SunStrike_image = pygame.image.load(
            'assets/graphics/Sun Strike.png').convert_alpha()
        self.SunStrike_image_slot = pygame.transform.scale(
            self.SunStrike_image, slot_size)
        self.SunStrike_image_skill = pygame.transform.scale(
            self.SunStrike_image, skill_size)
        self.Tornado_image = pygame.image.load(
            'assets/graphics/Tornado.png').convert_alpha()
        self.Tornado_image_slot = pygame.transform.scale(
            self.Tornado_image, slot_size)
        self.Tornado_image_skill = pygame.transform.scale(
            self.Tornado_image, skill_size)
        self.Wex_image = pygame.image.load(
            'assets/graphics/Wex.png').convert_alpha()
        self.Wex_image_slot = pygame.transform.scale(self.Wex_image, slot_size)
        self.Wex_image_skill = pygame.transform.scale(
            self.Wex_image, skill_size)

        self.Quas_image_icon = pygame.transform.scale(
            self.Quas_image, icon_size)
        self.Wex_image_icon = pygame.transform.scale(self.Wex_image, icon_size)
        self.Extort_image_icon = pygame.transform.scale(
            self.Extort_image, icon_size)

        # self.skill_image_dict
        self.skill_image_slot_dict = {'0': self.EMP_image_slot, '1': self.Tornado_image_slot, '2': self.Alacrity_image_slot, '3': self.GhostWalk_image_slot, '4': self.DeafeningBlast_image_slot,
                                      '5': self.ChaosMeteor_image_slot, '6': self.ColdSnap_image_slot, '7': self.IceWall_image_slot, '8': self.ForgeSpirit_image_slot, '9': self.SunStrike_image_slot}
        self.skill_image_skill_dict = {'0': self.EMP_image_skill, '1': self.Tornado_image_skill, '2': self.Alacrity_image_skill, '3': self.GhostWalk_image_skill, '4': self.DeafeningBlast_image_skill,
                                       '5': self.ChaosMeteor_image_skill, '6': self.ColdSnap_image_skill, '7': self.IceWall_image_skill, '8': self.ForgeSpirit_image_skill, '9': self.SunStrike_image_skill}
        self.skill_image_icon_dict = {
            '0': self.Quas_image_icon, '1': self.Wex_image_icon, '2': self.Extort_image_icon}

        # rect
        self.Quas_slot_rect = self.Quas_image_slot.get_rect(topleft=(35, 690))
        self.Wex_slot_rect = self.Wex_image_slot.get_rect(topleft=(125, 690))
        self.Extort_slot_rect = self.Extort_image_slot.get_rect(
            topleft=(215, 690))
        self.Invoke_slot_rect = self.Invoke_image_slot.get_rect(
            topleft=(305, 690))
        self.slot_1_rect = pygame.Rect((395, 690), slot_size)
        self.slot_2_rect = pygame.Rect((485, 690), slot_size)
        self.icon_1_rect = pygame.Rect((230, 630), icon_size)
        self.icon_2_rect = pygame.Rect((280, 630), icon_size)
        self.icon_3_rect = pygame.Rect((330, 630), icon_size)

        # keys
        q_text = 'Q'
        self.q_surf = self.game_font.render(q_text, True, Q_COLOR)
        q_topleft = self.Quas_slot_rect.topleft
        self.q_rect = self.q_surf.get_rect(topleft=q_topleft)
        w_text = 'W'
        self.w_surf = self.game_font.render(w_text, True, W_COLOR)
        w_topleft = self.Wex_slot_rect.topleft
        self.w_rect = self.w_surf.get_rect(topleft=w_topleft)
        e_text = 'E'
        self.e_surf = self.game_font.render(e_text, True, E_COLOR)
        e_topleft = self.Extort_slot_rect.topleft
        self.e_rect = self.e_surf.get_rect(topleft=e_topleft)
        r_text = 'R'
        self.r_surf = self.game_font.render(r_text, True, WHITE)
        r_topleft = self.Invoke_slot_rect.topleft
        self.r_rect = self.r_surf.get_rect(topleft=r_topleft)

        self.slot_key_topleft = []
        self.slot_key_topleft.append(self.slot_1_rect.topleft)
        self.slot_key_topleft.append(self.slot_2_rect.topleft)

        # heart
        self.heart_image = pygame.transform.scale(pygame.image.load(
            'assets/graphics/heart.png').convert_alpha(), (40, 40))
        self.heart_rect_1 = pygame.Rect((5, 10), (40, 40))
        self.heart_rect_2 = pygame.Rect((50, 10), (40, 40))
        self.heart_rect_3 = pygame.Rect((95, 10), (40, 40))
        self.heart_rect_4 = pygame.Rect((140, 10), (40, 40))
        self.heart_rect_5 = pygame.Rect((185, 10), (40, 40))
        self.heart_rect_list = [self.heart_rect_1, self.heart_rect_2, self.heart_rect_3, self.heart_rect_4, self.heart_rect_5]

        self.info_1_list = ['嘿几把, 民工三连都不会!', '哎呦, 天道酬勤懂不懂!', '嘿宝, 小火人控符会不会玩', '高手玩是神，菜鸟玩是狗(特指你)。',\
                '飓风摧毁停车场', '长的太骚 技能太浪', '走路姿势过于得瑟', '刷的快输出高容易死', '牛逼啊，我让你牛。', '你怎么这么肉?', \
                '无他，但手熟(卡)尔。']
        self.info_1 = choice(self.info_1_list)

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

    def blit_red_broad(self, key_down_list):
        red_road_size = (90, 90)
        topleft_1 = (30, 685)
        topleft_2 = (120, 685)
        topleft_3 = (210, 685)
        topleft_4 = (300, 685)
        topleft_5 = (390, 685)
        topleft_6 = (480, 685)
        red_broad = pygame.Surface(red_road_size).convert_alpha()
        red_broad.fill(RED)
        red_broad_rect_1 = red_broad.get_rect(topleft=topleft_1)
        red_broad_rect_2 = red_broad.get_rect(topleft=topleft_2)
        red_broad_rect_3 = red_broad.get_rect(topleft=topleft_3)
        red_broad_rect_4 = red_broad.get_rect(topleft=topleft_4)
        red_broad_rect_5 = red_broad.get_rect(topleft=topleft_5)
        red_broad_rect_6 = red_broad.get_rect(topleft=topleft_6)
        red_broad_rect = [red_broad_rect_1, red_broad_rect_2, red_broad_rect_3, red_broad_rect_4, red_broad_rect_5, red_broad_rect_6]

        for i, slots in enumerate(key_down_list):
            if slots:
                screen.blit(red_broad, red_broad_rect[i])

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
            self.skill_key_surf[i] = self.game_font.render(
                self.key_dict[self.skill_dict_reverse[str(skill)]], True, WHITE)
            self.skill_key_rect[i] = self.skill_key_surf[i].get_rect(
                topleft=self.slot_key_topleft[i])
            screen.blit(self.skill_key_surf[i], self.skill_key_rect[i])

        for spirites in self.drop_skill_group:
            drop_skill_name = spirites.skill
            comb = self.comb_dict[drop_skill_name]
            drop_skill_comb_surf = self.game_font.render(comb, True, WHITE)
            drop_skill_comb_rect = drop_skill_comb_surf.get_rect(
                topleft=spirites.rect.topleft)
            screen.blit(drop_skill_comb_surf, drop_skill_comb_rect)

    def draw_count(self, count):
        count_surf = self.game_font.render('连击:'+str(count), True, RED)
        count_rect = count_surf.get_rect(topleft=(420, 630))
        screen.blit(count_surf, count_rect)

    def draw_score(self, score):
        score_surf = self.game_font.render('分数:'+str(score), True, RED)
        score_rect = score_surf.get_rect(topleft=(30, 630))
        screen.blit(score_surf, score_rect)

    def draw_heart(self, heart):
        for i in range(heart):  # 0 1 2 3 4
            screen.blit(self.heart_image, self.heart_rect_list[i])

    def update_active(self, count, score, heart, key_down_list):
        self.blit_red_broad(key_down_list)
        self.draw_count(count)
        self.draw_score(score)
        self.draw_heart(heart)
        self.draw_slots()
        self.draw_icons()
        self.draw_key()

    def update_fail(self, score):
        self.end_info(score)


    def end_info(self, score):
        info_2 = '你的分:'
        info_3 = str(score)
        info_4 = '按空格重启'

        info_1_surf = pygame.transform.scale(
            self.game_font.render(self.info_1, False, WHITE), (430, 60))
        info_2_surf = pygame.transform.scale(
            self.game_font.render(info_2, False, WHITE), (140, 60))
        info_3_surf = self.game_font.render(info_3, False, WHITE)
        info_4_surf = pygame.transform.scale(
            self.game_font.render(info_4, False, WHITE), (200, 60))

        info_1_rect = info_1_surf.get_rect(topleft=(90, 90))
        info_2_rect = info_2_surf.get_rect(topleft=(230, 180))
        info_3_rect = info_3_surf.get_rect(midtop=(300, 250))
        info_4_rect = info_4_surf.get_rect(topleft=(200, 470))

        screen.blit(info_1_surf, info_1_rect)
        screen.blit(info_2_surf, info_2_rect)
        screen.blit(info_3_surf, info_3_rect)
        screen.blit(info_4_surf, info_4_rect)
