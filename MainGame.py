import pygame, time
from setting import *
from debug import debug


class MainGame:
    def __init__(self, group) -> None:
        #  Quas, Wex and Extort, 冰, 雷, 火
        # self.orbs_list = ['Quas', 'Wex', '']
        # self.skill_list = ['EMP', 'Tornado', 'Alacrity', 'Ghost Walk', 'Deafening Blast', \
        #     'Chaos  Meteor', 'Cold Snap', 'Ice Wall', 'Forge Spirit', 'Sun Strike']

        self.orbs_dict = {'0':'Quas', '1':'Wex', '2':'Extort'}
        self.skill_dict = {'0':'EMP', '1':'Tornado', '2':'Alacrity', '3':'Ghost Walk', '4':'Deafening Blast', \
            '5':'Chaos Meteor', '6':'Cold Snap', '7':'Ice Wall', '8':'Forge Spirit', '9':'Sun Strike'}
        self.skill_dict_reverse = {'EMP':'0', 'Tornado':'1', 'Alacrity':'2', 'Ghost Walk':'3', 'Deafening Blast':'4', \
            'Chaos Meteor':'5', 'Cold Snap':'6', 'Ice Wall':'7', 'Forge Spirit':'8', 'Sun Strike':'9'}
        self.key_dict = {'0':'C', '1':'X', '2':'Z', '3':'V', '4':'B', '5':'D', '6':'Y', '7':'G', '8':'F', '9':'T', }
        self.comb_dict = {'EMP':'WWW', 'Tornado':'QWW', 'Alacrity':'WWE', 'Ghost Walk':'QQW', 'Deafening Blast':'QWE', \
            'Chaos Meteor':'WEE', 'Cold Snap':'QQQ', 'Ice Wall':'QQE', 'Forge Spirit':'QEE', 'Sun Strike':'EEE'}
        self.drop_group = group


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

        # qqq=急速冷却 Y 受到冰元素影响
        # qqw=幽冥漫步 V 受到冰元素影响
        # qww=飓风 X 伤害和距离主要取决于雷、持续时间取决于冰
        # qwe=超声波 B 受雷元素影响击退时间
        # www=磁暴 C 受雷元素影响炸蓝数量
        # wwe=灵动迅捷 Z 雷元素影响攻速、火元素影响攻击力
        # wee=陨石 D 受火元素影响伤害
        # eee=天火 T 受火元素影响伤害
        # eqq=冰墙 G 收到冰元素
        # eeq=火人 F 冰火同时大于4时可以召唤双火人

        # self.obtained_orbs = []
        self.obtained_orbs = ['', '', '']
        self.invoke_dict = {'Quas':0, 'Wex':0, 'Extort':0}

        self.slot = ['', '']
        self.key_list = []

        # red_rect
        self.red_surf = pygame.Surface((560, 120), pygame.SRCALPHA, 32).convert_alpha()
        self.red_surf.fill(RED)
        self.red_rect = self.red_surf.get_rect(topleft = (20, 500))

        # game mechanics
        self.score = 0
        self.start_time = time.time()
        self.skill_used_time = self.start_time
        self.count = 0
        self.drop_speed = 200
        self.heart = 5
        self.game_state_list = ['active', 'menu', 'fail']
        self.game_state = self.game_state_list[0]

    # game = active ------------------------------------------------------------------------ # 

    def obtain_orb(self, orb_type):
        self.update_obtained_orbs(orb_type)

    def update_obtained_orbs(self, added_orb):
        if len(self.obtained_orbs) >= 3:
            obtained_orbs_copy = self.obtained_orbs[1:]
            obtained_orbs_copy.append(added_orb)
            self.obtained_orbs = obtained_orbs_copy
        elif len(self.obtained_orbs) < 3:
            self.obtained_orbs.append(added_orb)

    def check_if_in_slot(self, skill):
        if skill == self.slot[0] or skill == self.slot[1]:
            return True
        else:
            return False

    def switch_slot(self):
        temp = self.slot[0]
        self.slot[0] = self.slot[1]
        self.slot[1] = temp

    def invoke(self):
        if len(self.obtained_orbs) != 3:
            pass
        else:

            for orb in self.obtained_orbs:
                if orb == self.orbs_dict['0']:
                    self.invoke_dict['Quas'] += 1 
                if orb == self.orbs_dict['1']:
                    self.invoke_dict['Wex'] += 1
                if orb == self.orbs_dict['2']:
                    self.invoke_dict['Extort'] += 1

            if self.invoke_dict['Quas'] == 3:
                if self.check_if_in_slot(self.skill_dict['6']):
                    if self.skill_dict['6'] == self.slot[1]: self.switch_slot()
                else:
                    self.slot[1] = self.slot[0]
                    self.slot[0] = self.skill_dict['6']
            if self.invoke_dict['Quas'] == 2 and self.invoke_dict['Wex'] == 1:
                if self.check_if_in_slot(self.skill_dict['3']):
                    if self.skill_dict['3'] == self.slot[1]: self.switch_slot()
                else:
                    self.slot[1] = self.slot[0]
                    self.slot[0] = self.skill_dict['3']
            if self.invoke_dict['Quas'] == 2 and self.invoke_dict['Extort'] == 1:
                if self.check_if_in_slot(self.skill_dict['7']):
                    if self.skill_dict['7'] == self.slot[1]: self.switch_slot()
                else:
                    self.slot[1] = self.slot[0]
                    self.slot[0] = self.skill_dict['7']


            if self.invoke_dict['Wex'] == 3:
                if self.check_if_in_slot(self.skill_dict['0']):
                    if self.skill_dict['0'] == self.slot[1]: self.switch_slot()
                else:
                    self.slot[1] = self.slot[0]
                    self.slot[0] = self.skill_dict['0']
            if self.invoke_dict['Wex'] == 2 and self.invoke_dict['Quas'] == 1:
                if self.check_if_in_slot(self.skill_dict['1']):
                    if self.skill_dict['1'] == self.slot[1]: self.switch_slot()
                else:
                    self.slot[1] = self.slot[0]
                    self.slot[0] = self.skill_dict['1']
            if self.invoke_dict['Wex'] == 2 and self.invoke_dict['Extort'] == 1:
                if self.check_if_in_slot(self.skill_dict['2']):
                    if self.skill_dict['2'] == self.slot[1]: self.switch_slot()
                else:
                    self.slot[1] = self.slot[0]
                    self.slot[0] = self.skill_dict['2']


            if self.invoke_dict['Extort'] == 3:
                if self.check_if_in_slot(self.skill_dict['9']):
                    if self.skill_dict['9'] == self.slot[1]: self.switch_slot()
                else:
                    self.slot[1] = self.slot[0]
                    self.slot[0] = self.skill_dict['9']
            if self.invoke_dict['Extort'] == 2 and self.invoke_dict['Quas'] == 1:
                if self.check_if_in_slot(self.skill_dict['8']):
                    if self.skill_dict['8'] == self.slot[1]: self.switch_slot()
                else:
                    self.slot[1] = self.slot[0]
                    self.slot[0] = self.skill_dict['8']
            if self.invoke_dict['Extort'] == 2 and self.invoke_dict['Wex'] == 1:
                if self.check_if_in_slot(self.skill_dict['5']):
                    if self.skill_dict['5'] == self.slot[1]: self.switch_slot()
                else:
                    self.slot[1] = self.slot[0]
                    self.slot[0] = self.skill_dict['5']


            if self.invoke_dict['Quas'] == 1 and self.invoke_dict['Wex'] == 1 and self.invoke_dict['Extort'] == 1:
                if self.check_if_in_slot(self.skill_dict['4']):
                    if self.skill_dict['4'] == self.slot[1]: self.switch_slot()
                else:
                    self.slot[1] = self.slot[0]
                    self.slot[0] = self.skill_dict['4']

                
            self.invoke_dict = {'Quas':0, 'Wex':0, 'Extort':0}

    def use_skill(self, skill):
        if skill in self.slot:
            for spirites in self.drop_group:
                if skill == spirites.skill and spirites.avaibility:
                    spirites.kill()
                    self.count += 1
                    self.skill_used_interval = time.time() - self.skill_used_time
                    self.skill_used_time = time.time()
                    print(self.skill_used_interval)

                    self.add_score()
    
    def cheat_key(self):
        for spirites in self.drop_group:
            if spirites.avaibility:
                spirites.kill()
                self.count += 1
                self.skill_used_interval = time.time() - self.skill_used_time
                self.skill_used_time = time.time()
                print(self.skill_used_interval)

                self.add_score()

    def add_score(self):
        self.score += int((1+0.1*self.count)*(0.5*self.duration_time + (2.5 - 0.5*self.skill_used_interval)))

    def check_collison(self):
        for spirites in self.drop_group:
            if self.red_rect.colliderect(spirites):
                spirites.avaibility = 1
            else:
                spirites.avaibility = 0

    def count_break(self):
        self.count = 0

    def game_over(self):
        if self.heart <= 0:
            self.game_state = self.game_state_list[2]

    def update_active(self):
        for spirites in self.drop_group:
            if spirites.rect.y > dead_distance:
                self.count_break()
                self.heart -= 1

        self.duration_time = time.time()-self.start_time

        if self.drop_speed < 800:
            self.drop_speed = 200 + int(3*self.duration_time)

        screen.blit(self.red_surf, self.red_rect)
        self.check_collison()
        self.game_over()

    # game = fail ---------------------------------------------------------------------------- #
    def restart(self):
        self.drop_group.empty()

        self.score = 0
        self.start_time = time.time()
        self.skill_used_time = self.start_time
        self.count = 0
        self.drop_speed = 200
        self.heart = 5

        self.obtained_orbs = ['', '', '']
        self.invoke_dict = {'Quas':0, 'Wex':0, 'Extort':0}
        self.slot = ['', '']

        self.game_state = self.game_state_list[0]


    def update_fail(self):
        pass

