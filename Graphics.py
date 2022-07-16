
import pygame
from setting import * 

class Graphics:
    def __init__(self):
        # super(Graphics, self).__init__(groups)
        self.orbs_dict = {'0':'Quas', '1':'Wex', '2':'Extort'}
        self.skill_dict = {'0':'EMP', '1':'Tornado', '2':'Alacrity', '3':'Ghost Walk', '4':'Deafening Blast', \
            '5':'Chaos Meteor', '6':'Cold Snap', '7':'Ice Wall', '8':'Forge Spirit', '9':'Sun Strike'}

        # font
        self.game_font = pygame.font.Font('assets/font/PoetsenOne-Regular.ttf', 25)

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

        # self.skill_image_dict 
        self.skill_image_slot_dict = {'0':self.EMP_image_slot, '1':self.Tornado_image_slot, '2':self.Alacrity_image_slot, '3':self.GhostWalk_image_slot, '4':self.DeafeningBlast_image_slot, 
            '5':self.ChaosMeteor_image_slot, '6':self.ColdSnap_image_slot, '7':self.IceWall_image_slot, '8':self.ForgeSpirit_image_slot, '9':self.SunStrike_image_slot}
        self.skill_image_skill_dict = {'0':self.EMP_image_skill, '1':self.Tornado_image_skill, '2':self.Alacrity_image_skill, '3':self.GhostWalk_image_skill, '4':self.DeafeningBlast_image_skill, 
            '5':self.ChaosMeteor_image_skill, '6':self.ColdSnap_image_skill, '7':self.IceWall_image_skill, '8':self.ForgeSpirit_image_skill, '9':self.SunStrike_image_skill}

        # rect
        self.Quas_slot_rect = self.Quas_image_slot.get_rect(topleft = (35, 690))
        self.Wex_slot_rect = self.Wex_image_slot.get_rect(topleft = (125, 690))
        self.Extort_slot_rect = self.Extort_image_slot.get_rect(topleft = (215, 690))
        self.Invoke_slot_rect = self.Invoke_image_slot.get_rect(topleft = (305, 690))
        self.slot_1_rect = pygame.Rect((395, 690), slot_size)
        self.slot_2_rect = pygame.Rect((485, 690), slot_size)

        # position
        # self.rect = self.image.get_rect(midtop=(300, 700))
        # self.old_rect = self.rect.copy()

        # # movement
        # self.pos = pygame.math.Vector2(self.rect.topleft)
        # self.direction = pygame.math.Vector2()
        # self.speed = 280

    # def update(self, dt):
    #     self.old_rect = self.rect.copy()

    #     self.pos.x += self.direction.x * self.speed * dt
    #     self.rect.x = round(self.pos.x)

    def obtain_skill_slot(self, slot):
        self.slot = slot

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



    def draw_key(self):
        q_text = 'Q'
        q_surf = self.game_font.render(q_text, True, Q_COLOR)
        q_topleft = self.Quas_slot_rect.topleft
        q_rect = q_surf.get_rect(topleft = q_topleft)
        screen.blit(q_surf, q_rect)

        w_text = 'W'
        w_surf = self.game_font.render(w_text, True, W_COLOR)
        w_topleft = self.Wex_slot_rect.topleft
        w_rect = w_surf.get_rect(topleft = w_topleft)
        screen.blit(w_surf, w_rect)

        e_text = 'E'
        e_surf = self.game_font.render(e_text, True, E_COLOR)
        e_topleft = self.Extort_slot_rect.topleft
        e_rect = e_surf.get_rect(topleft = e_topleft)
        screen.blit(e_surf, e_rect)

        r_text = 'R'
        r_surf = self.game_font.render(r_text, True, WHITE)
        r_topleft = self.Invoke_slot_rect.topleft
        r_rect = r_surf.get_rect(topleft = r_topleft)
        screen.blit(r_surf, r_rect)

    def update(self):
        self.draw_slots()
        self.draw_key()

