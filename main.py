import pygame, sys, time
from MainGame import MainGame
from Graphics import Graphics
import setting
from debug import debug

# general setup --------------------------------------------------------------------------------------------- #
## pygame setup
pygame.init()
screen = pygame.display.set_mode(setting.window_size)

pygame.display.set_caption('Invoker Simulator')
pygame.display.set_icon(pygame.image.load('assets/graphics/dota2.png'))
# background_surface = pygame.transform.scale(
#     pygame.image.load('assets/background/ground.png').convert(), (setting.WIN_WIDTH, setting.WIN_HEIGTH))
# background_rect = background_surface.get_rect(center=(setting.WIN_WIDTH / 2, setting.WIN_HEIGTH / 2))
# clock = pygame.time.Clock()
# font = pygame.font.Font('assets/font/Pixeltype.ttf', 50)

## varibles setup
game_state_list = ['active', 'begin_menu', 'fail']
game_state = game_state_list[0]

# group setup ----------------------------------------------------------------------------------------------- #
# all_sprites = pygame.sprite.Group()
# collision_sprites = pygame.sprite.Group()

# class setup ----------------------------------------------------------------------------------------------- #
# class = Class()
main_game = MainGame()
graphics = Graphics()

# main ------------------------------------------------------------------------------------------------------ #
def main():
    last_time = time.time()
    while True:

        # delta time    ------------------------------------------------------------------------------------- #
        dt = time.time() - last_time
        last_time = time.time()

        # event loop    ------------------------------------------------------------------------------------- #
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE):
                pygame.quit()
                sys.exit()
            if game_state == game_state_list[0]:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        main_game.obtain_orb('Quas')
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        main_game.obtain_orb('Wex')
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        main_game.obtain_orb('Extort')
                    if event.key == pygame.K_r:
                        main_game.invoke()

        if game_state == game_state_list[0]:    # 游戏正在执行
            screen.fill(setting.WHITE)
            # screen.blit(background_surface, background_rect)
            # all_sprites.update()
            # all_sprites.draw(screen)
            graphics.obtain_skill_slot(main_game.slot)
            graphics.update()

        debug(main_game.obtained_orbs)
        debug(main_game.slot, y = 30)
        pygame.display.update()


if __name__ == "__main__":
    main()
