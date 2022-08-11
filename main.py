import pygame, sys, time, random
from DropSkills import DropSkill
from MainGame import MainGame
from Graphics import Graphics
from setting import * 
from debug import debug

# general setup --------------------------------------------------------------------------------------------- #
## pygame setup
pygame.init()
pygame.mixer.init() 
screen = pygame.display.set_mode(window_size)

pygame.display.set_caption('Invoker Simulator')
pygame.display.set_icon(pygame.image.load('assets/graphics/dota2.png'))

## varibles setup
skill_list = ['EMP', 'Tornado', 'Alacrity', 'Ghost Walk', 'Deafening Blast', \
            'Chaos Meteor', 'Cold Snap', 'Ice Wall', 'Forge Spirit', 'Sun Strike']

key_down_list = [0, 0, 0, 0, 0, 0]

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

def slots_detection():
    pass

# main ------------------------------------------------------------------------------------------------------ #
def main(event_speed):
    slot_i = None

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

            if main_game.game_state == main_game.game_state_list[1]:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        main_game.game_state = main_game.game_state_list[0]
                        main_game.trad_keys = 1
                    if event.key == pygame.K_2:
                        main_game.game_state = main_game.game_state_list[0]
                        main_game.trad_keys = 0

            if main_game.game_state == main_game.game_state_list[0]:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        main_game.obtain_orb('Quas')
                        key_down_list[0] = 1
                    if event.key == pygame.K_w:
                        main_game.obtain_orb('Wex')
                        key_down_list[1] = 1
                    if event.key == pygame.K_e:
                        main_game.obtain_orb('Extort')
                        key_down_list[2] = 1
                    if event.key == pygame.K_r:
                        main_game.invoke()
                        key_down_list[3] = 1
                    if event.key == pygame.K_0:
                        main_game.cheat_key()

                    # debug 功能 k键自杀
                    if event.key == pygame.K_k: main_game.heart = 0

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_q:
                        key_down_list[0] = 0
                    if event.key == pygame.K_w:
                        key_down_list[1] = 0
                    if event.key == pygame.K_e:
                        key_down_list[2] = 0
                    if event.key == pygame.K_r:
                        key_down_list[3] = 0


            
            if main_game.game_state == main_game.game_state_list[0] and main_game.trad_keys == 1:           # 传统按键
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        slot_i = main_game.use_skill(main_game.skill_dict['0'])
                    if event.key == pygame.K_x:
                        slot_i = main_game.use_skill(main_game.skill_dict['1'])
                    if event.key == pygame.K_z:
                        slot_i = main_game.use_skill(main_game.skill_dict['2'])
                    if event.key == pygame.K_v:
                        slot_i = main_game.use_skill(main_game.skill_dict['3'])
                    if event.key == pygame.K_b:
                        slot_i = main_game.use_skill(main_game.skill_dict['4'])
                    if event.key == pygame.K_d:
                        slot_i = main_game.use_skill(main_game.skill_dict['5'])
                    if event.key == pygame.K_y:
                        slot_i = main_game.use_skill(main_game.skill_dict['6'])
                    if event.key == pygame.K_g:
                        slot_i = main_game.use_skill(main_game.skill_dict['7'])
                    if event.key == pygame.K_f:
                        slot_i = main_game.use_skill(main_game.skill_dict['8'])
                    if event.key == pygame.K_t:
                        slot_i = main_game.use_skill(main_game.skill_dict['9'])

                    match slot_i:
                        case None:
                            pass
                        case 0:
                            key_down_list[4] = 1
                        case 1:
                            key_down_list[5] = 1

                    # FIXME: 在此处补充一个检测不同技能键弹起修改keydowlist的功能

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_F10:
                        pass
                    else:
                        key_down_list[4] = 0
                        key_down_list[5] = 0

            if main_game.game_state == main_game.game_state_list[0] and main_game.trad_keys == 0:           # qwerdf按键
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d:
                        main_game.use_skill(main_game.use_skill_qewrdf(0))
                        key_down_list[4] = 1
                    if event.key == pygame.K_f:
                        main_game.use_skill(main_game.use_skill_qewrdf(1))
                        key_down_list[5] = 1

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_d:
                        key_down_list[4] = 0
                    if event.key == pygame.K_f:
                        key_down_list[5] = 0


            if event.type == SPEED_UPDATE_EVENT and main_game.game_state == main_game.game_state_list[0]:
                pygame.time.set_timer(DROP_EVENT, int(event_speed))

            if event.type == DROP_EVENT and main_game.game_state == main_game.game_state_list[0]:
                skill = random.choice(skill_list)
                image = graphics.skill_image_skill_dict[main_game.skill_dict_reverse[skill]]
                drop_group.add(DropSkill(drop_group, skill, image, main_game.drop_speed))

            if event.type == pygame.KEYDOWN and main_game.game_state == main_game.game_state_list[2]:
                if event.key == pygame.K_SPACE: 
                    main_game.restart()
                    event_speed = 3000

        if main_game.game_state == main_game.game_state_list[1]:    # 主界面
            screen.fill(WHITE)
            main_game.update_menu()
            graphics.update_menu()

        if main_game.game_state == main_game.game_state_list[0]:    # 游戏正在执行
            screen.fill(WHITE)
            # screen.blit(background_surface, background_rect)
            graphics.obtain_info(main_game.slot, main_game.obtained_orbs)

            for skill in drop_group.sprites():  # Group.sprites() 加上括号才是返回groups中包含sprites的列表, 没有括号就是Group的方法
                skill.get_dt(dt)

            drop_group.update()
            drop_group.draw(screen)
            main_game.update_active()
            graphics.update_active(main_game.count, main_game.score, main_game.heart, key_down_list, main_game.trad_keys)

            event_speed = update_timer(event_speed)

        if main_game.game_state == main_game.game_state_list[2]:    # 游戏失败
            screen.fill(BLACK)
            main_game.update_fail()
            graphics.update_fail(main_game.score)

            # for event in pygame.event.get():
            #     if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE):
            #         pygame.quit()
            #         sys.exit()

        pygame.display.update()


if __name__ == "__main__":
    main(event_speed)
