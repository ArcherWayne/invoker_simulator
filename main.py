
from turtle import update
import pygame, sys, time, random
from DropSkills import DropSkill
from MainGame import MainGame
from Graphics import Graphics
from setting import * 
from debug import debug

# general setup --------------------------------------------------------------------------------------------- #
## pygame setup
pygame.init()
screen = pygame.display.set_mode(window_size)

pygame.display.set_caption('Invoker Simulator')
pygame.display.set_icon(pygame.image.load('assets/graphics/dota2.png'))
# background_surface = pygame.transform.scale(
#     pygame.image.load('assets/background/ground.png').convert(), (setting.WIN_WIDTH, setting.WIN_HEIGTH))
# background_rect = background_surface.get_rect(center=(setting.WIN_WIDTH / 2, setting.WIN_HEIGTH / 2))
# font = pygame.font.Font('assets/font/Pixeltype.ttf', 50)

## varibles setup
skill_list = ['EMP', 'Tornado', 'Alacrity', 'Ghost Walk', 'Deafening Blast', \
            'Chaos Meteor', 'Cold Snap', 'Ice Wall', 'Forge Spirit', 'Sun Strike']

DROP_EVENT = pygame.USEREVENT
event_speed = 3000
pygame.time.set_timer(DROP_EVENT, event_speed)
SPEED_UPDATE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(SPEED_UPDATE_EVENT, 5000)
clock = pygame.time.Clock()

# group setup ----------------------------------------------------------------------------------------------- #
drop_group = pygame.sprite.Group()

# class setup ----------------------------------------------------------------------------------------------- #
# class = Class()
main_game = MainGame(drop_group)
graphics = Graphics(drop_group)

# function -------------------------------------------------------------------------------------------------- #
def update_timer(event_speed):
    if event_speed > 1000:
        event_speed = 4000 - 1000*((2*(main_game.duration_time/60)+3)/3)
    else: 
        event_speed = 1000
    return event_speed

# main ------------------------------------------------------------------------------------------------------ #
def main(event_speed):
    last_time = time.time()
    while True:

        # delta time    ------------------------------------------------------------------------------------- #
        dt = time.time() - last_time
        last_time = time.time()
        clock.tick(FPS)

        # event loop    ------------------------------------------------------------------------------------- #
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE):
                pygame.quit()
                sys.exit()
            if main_game.game_state == main_game.game_state_list[0]:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q: main_game.obtain_orb('Quas')
                    if event.key == pygame.K_w: main_game.obtain_orb('Wex')
                    if event.key == pygame.K_e: main_game.obtain_orb('Extort')
                    if event.key == pygame.K_r: main_game.invoke()
                    if event.key == pygame.K_c: main_game.use_skill(main_game.skill_dict['0'])
                    if event.key == pygame.K_x: main_game.use_skill(main_game.skill_dict['1'])
                    if event.key == pygame.K_z: main_game.use_skill(main_game.skill_dict['2'])
                    if event.key == pygame.K_v: main_game.use_skill(main_game.skill_dict['3'])
                    if event.key == pygame.K_b: main_game.use_skill(main_game.skill_dict['4'])
                    if event.key == pygame.K_d: main_game.use_skill(main_game.skill_dict['5'])
                    if event.key == pygame.K_y: main_game.use_skill(main_game.skill_dict['6'])
                    if event.key == pygame.K_g: main_game.use_skill(main_game.skill_dict['7'])
                    if event.key == pygame.K_f: main_game.use_skill(main_game.skill_dict['8'])
                    if event.key == pygame.K_t: main_game.use_skill(main_game.skill_dict['9'])
                    if event.key == pygame.K_0: main_game.cheat_key()
            if event.type == SPEED_UPDATE_EVENT and main_game.game_state == main_game.game_state_list[0]:
                pygame.time.set_timer(DROP_EVENT, int(event_speed))

            if event.type == DROP_EVENT and main_game.game_state == main_game.game_state_list[0]:
                skill = random.choice(skill_list)
                image = graphics.skill_image_skill_dict[main_game.skill_dict_reverse[skill]]
                drop_group.add(DropSkill(drop_group, skill, image, main_game.drop_speed))


        if main_game.game_state == main_game.game_state_list[0]:    # 游戏正在执行
            screen.fill(WHITE)
            # screen.blit(background_surface, background_rect)
            graphics.obtain_info(main_game.slot, main_game.obtained_orbs)

            for skill in drop_group.sprites():  # Group.sprites() 加上括号才是返回groups中包含sprites的列表, 没有括号就是Group的方法
                skill.get_dt(dt)

            drop_group.update()
            drop_group.draw(screen)
            main_game.update()
            graphics.update(main_game.count, main_game.score)

            event_speed = update_timer(event_speed)

        if main_game.game_state == main_game.game_state_list[2]:    # 游戏失败
            screen.fill(BLACK)

        pygame.display.update()


if __name__ == "__main__":
    main(event_speed)
