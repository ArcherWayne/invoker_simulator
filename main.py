
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
game_state_list = ['active', 'begin_menu', 'fail']
game_state = game_state_list[0]
skill_list = ['EMP', 'Tornado', 'Alacrity', 'Ghost Walk', 'Deafening Blast', \
            'Chaos Meteor', 'Cold Snap', 'Ice Wall', 'Forge Spirit', 'Sun Strike']

DROP_EVENT = pygame.USEREVENT

pygame.time.set_timer(DROP_EVENT, 3000)
clock = pygame.time.Clock()

# group setup ----------------------------------------------------------------------------------------------- #
drop_group = pygame.sprite.Group()

# class setup ----------------------------------------------------------------------------------------------- #
# class = Class()
main_game = MainGame(drop_group)
graphics = Graphics()

# main ------------------------------------------------------------------------------------------------------ #
def main():
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
            if game_state == game_state_list[0]:
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
            if event.type == DROP_EVENT and game_state == game_state_list[0]:
                skill = random.choice(skill_list)
                image = graphics.skill_image_skill_dict[main_game.skill_dict_reverse[skill]]
                drop_group.add(DropSkill(drop_group, skill, image, 200))


        if game_state == game_state_list[0]:    # 游戏正在执行
            screen.fill(WHITE)
            # screen.blit(background_surface, background_rect)
            graphics.obtain_info(main_game.slot, main_game.obtained_orbs)

            for skill in drop_group.sprites():  # Group.sprites() 加上括号才是返回groups中包含sprites的列表, 没有括号就是Group的方法
                skill.get_dt(dt)

            drop_group.update()
            drop_group.draw(screen)
            main_game.update()
            graphics.update()

        debug(len(drop_group.sprites()))
        pygame.display.update()


if __name__ == "__main__":
    main()
