"""
导入模块 sys(系统模块) pygame setting
"""
import pygame
from pygame.sprite import Group
from setting import Settings
from ship import Ship
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
import game_functions as gf

def run_game():
    '''初始化游戏并创建一个屏幕对象'''
    pygame.init()
    ai_setting = Settings()
    screen = pygame.display.set_mode(
        (ai_setting.screen_width,ai_setting.screen_height))
    pygame.display.set_caption(ai_setting.game_title)

    # 创建一艘飞船
    ship = Ship(ai_setting, screen)

    # 创建一个用于存储外星人的编组
    aliens = Group()
    #创建一个用于存储子弹的编组
    bullets = Group()

    #创建外星人群
    gf.create_fleet(ai_setting, screen, aliens)

    # 创建一个用于存储游戏统计信息的实例 及记分牌
    stats = GameStats(ai_setting)
    sb = Scoreboard(ai_setting, screen, stats)

    # 创建游戏开始按钮
    play_button = Button(ai_setting, screen, 'Play')
    play_button.test("this is a test")
    '''开始游戏'''
    while True:
        '''监听键盘 鼠标事件'''
        gf.check_events(ai_setting, stats, sb, screen, ship, aliens, bullets, play_button)
        if stats.game_active == True:
            '''飞船移动'''
            ship.update()
            '''更新子弹位置'''
            gf.bullets_update(bullets)
            '''更新外星人位置'''
            gf.update_aliens(ai_setting, stats, sb, screen, aliens, bullets, ship)
        '''让最近绘制的屏幕可见'''
        gf.update_screen(ai_setting, stats, sb, screen, ship, aliens, bullets, play_button)

run_game()

"""
方法记录
初始化   pygame.init()
窗口尺寸 pygame.display.set_mode((900,500))
窗口标题 pygame.display.set_caption("Alien Invasion")
事件监听 pygame.event.get()
背景颜色 screen.fill(bg_color)
屏幕可见 pygame.display.flip()
关闭窗口 sys.exit()
"""