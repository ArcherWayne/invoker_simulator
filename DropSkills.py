from re import M
import pygame, random
from setting import *
from debug import debug

class DropSkill(pygame.sprite.Sprite):
    def __init__(self, groups, skill, image, drop_speed) -> None:
        super().__init__(groups)
        self.skill = skill
        self.image = image
        self.drop_speed = drop_speed
        self.avaibility = 0

        # ----------------------------------------------------------------------------------- #
        start_topleft = [(30, -200), (170, -200), (310, -200), (450, -200)]
        self.rect = self.image.get_rect(topleft = random.choice(start_topleft))

    def get_dt(self, dt):
        self.dt = dt

    def die(self):
        if self.rect.y > dead_distance:
            self.kill()

    def update(self):
        self.die()
        self.rect.y += self.drop_speed * self.dt