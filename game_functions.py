"""
避免主程序过长 创建公共函数库
"""
import sys
from time import sleep
import pygame
from bullet import Bullet
from alien import Alien
# 监控鼠标事件
def check_keydown_events(event, ai_setting, screen, ship, bullets):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
         ship.moving_up = True
    elif event.key == pygame.K_DOWN:
         ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        #创建一颗子弹 并加入到 bullets 编组中
        fire_bullet(ai_setting, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event, ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
         ship.moving_up = False
    elif event.key == pygame.K_DOWN:
         ship.moving_down = False

def check_play_button(ai_setting,play_button,screen, stats, sb, ship, aliens, bullets, mouse_x, mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # 隐藏光标
        pygame.mouse.set_visible(False)
        # 重置游戏信息
        ai_setting.initialize_dynamic_setting()
        stats.reset_stats()
        stats.game_active = True
        # 得分清零
        stats.score = 0
        sb.prep_score()

        # 清空外星人 和子弹列表
        aliens.empty()
        bullets.empty()

        # 创建一群新外星人
        create_fleet(ai_setting, screen, aliens)
        ship.ship_center()
    else:
        # stats.game_active = False
        pygame.mouse.set_visible(True)

def check_events(ai_setting, stats, sb, screen, ship, aliens, bullets, play_button):
    """响应鼠标 键盘事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_setting,play_button,screen, stats, sb, ship, aliens, bullets, mouse_x, mouse_y)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_setting, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def bullets_update(bullets):
    '''更新子弹位置'''
    bullets.update()
    '''删除已经消失的子弹'''
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
def fire_bullet(ai_setting, screen, ship,bullets):
    #创建一颗子弹 并加入到 bullets 编组中
    new_bullet = Bullet( ai_setting, screen, ship)
    bullets.add(new_bullet)
def create_fleet(ai_setting, screen, aliens):
    """创建外星人群"""
    #创建一个外星人 并计算一行可容纳多少个外星人
    #外星人间距 为一个外星人的宽度
    #创建第一行外星人
    alien = Alien(ai_setting, screen)
    for row_number in range(alien.number_rows):
        for alien_number in range(alien.number_aliens_x):
            #创建一个外星人 并将其加入到当前行
            create_alien(ai_setting, screen, aliens, alien_number, row_number)

def create_alien(ai_setting, screen, aliens, alien_number, row_number):
    """创建一个外星人 并将其加入到当前行"""
    alien = Alien(ai_setting, screen)
    # alien类里使用了 alien.x 做中介 需要更新每个外星人此时的x属性
    alien.x = alien.rect.x + 2 * alien.rect.x *alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def check_fleet_edges(ai_setting, aliens):
    """有外人到达边缘时采取相应的措施"""
    for alien in aliens:
        if alien.check_edges():
            change_fleet_direction(ai_setting, aliens)
            break
def change_fleet_direction(ai_setting, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_setting.fleet_drop_speed
    ai_setting.fleet_direction *= -1

def update_aliens(ai_setting, stats, sb, screen, aliens, bullets, ship):
    '''更新外星人位置'''
    check_fleet_edges(ai_setting, aliens)
    aliens.update()
    check_bullet_alien_collisions(ai_setting, stats, sb, screen, aliens, bullets)
    """检测外星人和飞船之间的碰撞"""
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_setting, stats, screen, ship, aliens, bullets)
    # 检测外星人是否到达底部
    check_aliens_bottom(ai_setting, stats, screen, ship, aliens, bullets)

def check_bullet_alien_collisions(ai_setting, stats, sb, screen, aliens, bullets):
    # 检查是否有子弹击中了外星人
    # 如果击中 就删除对应的子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    # 检测外星人是否全部被消灭 并重新创建 记分
    if collisions:
        stats.score += ai_setting.alien_points
        sb.prep_score()
    if len(aliens) == 0:
        bullets.empty()
        ai_setting.increase_speed()
        create_fleet(ai_setting, screen, aliens)


"""存储值监察"""
def ship_hit(ai_setting, stats, screen, ship, aliens, bullets):
    """响应被外星人撞到"""
    # 将ship_left 减 1
    print(str(stats.ships_left) + '1')
    if stats.ships_left > 0:
        stats.ships_left -=1
        # 清空外星人和子弹列表
        aliens.empty()
        bullets.empty()

        #创建一群新外星人
        create_fleet(ai_setting, screen, aliens)
        ship.ship_center()

        # 暂停0.5秒
        sleep(0.5)
    else:
        stats.game_active = False

def check_aliens_bottom(ai_setting, stats, screen, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_setting, stats, screen, ship, aliens, bullets)
            break

def update_screen(ai_setting, stats, sb, screen, ship, aliens, bullets, play_button):
    # 每次循环重新绘制屏幕
    screen.fill(ai_setting.bg_color)

    # 在飞船 和外星人后面重绘所有子弹
    if stats.game_active:
        ship.blitme()
        aliens.draw(screen)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # 显示得分
    sb.show_score()
    if not stats.game_active:
        play_button.draw_button()

    '''让最近绘制的屏幕可见'''
    pygame.display.flip()
