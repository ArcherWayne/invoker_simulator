# from tabnanny import check
# from numpy import obj2sctype
import pygame
import setting
from debug import debug


class MainGame:
    def __init__(self) -> None:
        #  Quas, Wex and Extort, 冰, 雷, 火
        # self.orbs_list = ['Quas', 'Wex', '']
        # self.skill_list = ['EMP', 'Tornado', 'Alacrity', 'Ghost Walk', 'Deafening Blast', \
        #     'Chaos  Meteor', 'Cold Snap', 'Ice Wall', 'Forge Spirit', 'Sun Strike']

        self.orbs_dict = {'0':'Quas', '1':'Wex', '2':'Extort'}
        self.skill_dict = {'0':'EMP', '1':'Tornado', '2':'Alacrity', '3':'Ghost Walk', '4':'Deafening Blast', \
            '5':'Chaos Meteor', '6':'Cold Snap', '7':'Ice Wall', '8':'Forge Spirit', '9':'Sun Strike'}
        # 0 EMP
        # 1 Tornado
        # 2 Alacrity
        # 3 Ghost Walk
        # 4 Deafening Blast
        # 5 Chaos Meteor
        # 6 Cold Snap
        # 7 Ice Wall
        # 8 Forge Spirirt
        # 9 Sun Strike

        self.obtained_orbs = []
        self.invoke_dict = {'Quas':0, 'Wex':0, 'Extort':0}

        self.slot = ['', '']

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
                    pass
                else:
                    self.slot[1] = self.slot[0]
                    self.slot[0] = self.skill_dict['6']
            if self.invoke_dict['Quas'] == 2 and self.invoke_dict['Wex'] == 1:
                if self.check_if_in_slot(self.skill_dict['3']):
                    pass
                else:
                    self.slot[1] = self.slot[0]
                    self.slot[0] = self.skill_dict['3']
            if self.invoke_dict['Quas'] == 2 and self.invoke_dict['Extort'] == 1:
                if self.check_if_in_slot(self.skill_dict['7']):
                    pass
                else:
                    self.slot[1] = self.slot[0]
                    self.slot[0] = self.skill_dict['7']


            if self.invoke_dict['Wex'] == 3:
                if self.check_if_in_slot(self.skill_dict['0']):
                    pass
                else:
                    self.slot[1] = self.slot[0]
                    self.slot[0] = self.skill_dict['0']
            if self.invoke_dict['Wex'] == 2 and self.invoke_dict['Quas'] == 1:
                if self.check_if_in_slot(self.skill_dict['1']):
                    pass
                else:
                    self.slot[1] = self.slot[0]
                    self.slot[0] = self.skill_dict['1']
            if self.invoke_dict['Wex'] == 2 and self.invoke_dict['Extort'] == 1:
                if self.check_if_in_slot(self.skill_dict['2']):
                    pass
                else:
                    self.slot[1] = self.slot[0]
                    self.slot[0] = self.skill_dict['2']


            if self.invoke_dict['Extort'] == 3:
                if self.check_if_in_slot(self.skill_dict['9']):
                    pass
                else:
                    self.slot[1] = self.slot[0]
                    self.slot[0] = self.skill_dict['9']
            if self.invoke_dict['Extort'] == 2 and self.invoke_dict['Quas'] == 1:
                if self.check_if_in_slot(self.skill_dict['8']):
                    pass
                else:
                    self.slot[1] = self.slot[0]
                    self.slot[0] = self.skill_dict['8']
            if self.invoke_dict['Extort'] == 2 and self.invoke_dict['Wex'] == 1:
                if self.check_if_in_slot(self.skill_dict['5']):
                    pass
                else:
                    self.slot[1] = self.slot[0]
                    self.slot[0] = self.skill_dict['5']


            if self.invoke_dict['Quas'] == 1 and self.invoke_dict['Wex'] == 1 and self.invoke_dict['Extort'] == 1:
                if self.check_if_in_slot(self.skill_dict['4']):
                    pass
                else:
                    self.slot[1] = self.slot[0]
                    self.slot[0] = self.skill_dict['4']

                
            self.invoke_dict = {'Quas':0, 'Wex':0, 'Extort':0}


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
    def use_skill(skill):
        pass




