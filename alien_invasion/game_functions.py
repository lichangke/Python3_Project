#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   game_functions.py
@Time    :   2019/03/30 23:20:37
@Author  :   leacoder
@Version :   1.0
@Contact :   leacock1991@gmail.com
@License :   
@Desc    :   存储大量让游戏《外星人入侵》 运行的函数  在模块game_functions 而不是run_game() 中完成大部分工作。

'''

# here put the import lib

import sys
import pygame
from bullet import Bullet

# 导入 Alien
from alien import Alien

from time import sleep


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
        # # 在创建新子弹前检查未消失的子弹数是否小于bullets_allowed
        # if len(bullets) < ai_settings.bullets_allowed:
        #     # 创建一颗子弹， 并将其加入到编组bullets中
        #     new_bullet = Bullet(ai_settings, screen, ship)
        #     bullets.add(new_bullet)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, stats, sb, play_button, ship,aliens, bullets):
    """响应按键和鼠标事件"""
    # 游戏退出 飞船左右飞行
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:  # 监视与这个按钮相关的鼠标事件
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, ship,aliens, bullets, mouse_x, mouse_y)

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen,ship, bullets)  # 由函数将 KEYDOWN 事件统一来处理

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)  # 由函数将 KEYUP 事件统一来处理
        # 由 check_keydown_events check_keyup_events 替代
        # elif event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_RIGHT:
        #         # 向右移动飞船
        #         ship.moving_right = True  # 一直按着 一直移动
        #     elif event.key == pygame.K_LIGHT:
        #         # 向右移动飞船
        #         ship.moving_light = True  # 一直按着 一直移动
        # elif event.type == pygame.KEYUP:
        #     if event.key == pygame.K_RIGHT:
        #         ship.moving_right = False  # 松开 停止移动
        #     elif event.key == pygame.K_LIGHT:
        #         ship.moving_light = False  # 松开 停止移动


def check_play_button(ai_settings, screen, stats, sb, play_button, ship,aliens, bullets, mouse_x, mouse_y):
    """在玩家单击Play按钮时开始新游戏"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:  # 可让游戏仅在game_active 为False 时才开始 对 button 响应
        # 重置游戏设置
        ai_settings.initialize_dynamic_settings()

        # 隐藏光标
        pygame.mouse.set_visible(False)

        # 重置游戏统计信息
        stats.reset_stats()
        stats.game_active = True

        # 重置记分牌图像
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()
        # 创建一群新的外星人， 并让飞船居中
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()


def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
    """更新屏幕上的图像， 并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()  # 绘制飞船 先绘制背景再绘制飞船
    aliens.draw(screen)
    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # 显示得分
    sb.show_score()

    # 如果游戏处于非活动状态， 就绘制Play按钮
    if not stats.game_active:
        play_button.draw_button()

    # 让最近绘制的屏幕可见
    pygame.display.flip()


def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """更新子弹的位置， 并删除已消失的子弹"""
    # 更新子弹的位置
    bullets.update()
    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(
        ai_settings, screen, stats, sb, ship, aliens, bullets)


def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """响应子弹和外星人的碰撞"""
    # 删除发生碰撞的子弹和外星人
    # 检查是否有子弹击中了外星人
    # 如果是这样， 就删除相应的子弹和外星人
    # 方法sprite.groupcollide() 将每颗子弹的rect 同每个外星人的rect 进行比较， 并返回一个字典， 其中包含发生了碰撞的子弹和外星人。
    # 在这个字典中， 每个键都是一颗子弹， 而相应的值都是被击中的外星人   两个实参True 告诉Pygame删除发生碰撞的子弹和外星人。
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()

        check_high_score(stats, sb)  # 每当有外星人被消灭， 都需要在更新得分后调用check_high_score() 


    if len(aliens) == 0:
        # 删除现有的子弹并新建一群外星人
        bullets.empty()
        ai_settings.increase_speed()  # 整群外星人都被消灭后调用increase_speed() 来加快游戏的节奏
        # 提高等级
        stats.level += 1
        sb.prep_level()
        create_fleet(ai_settings, screen, ship, aliens)


def fire_bullet(ai_settings, screen, ship, bullets):
    """如果还没有到达限制， 就发射一颗子弹"""
    # 在创建新子弹前检查未消失的子弹数是否小于bullets_allowed
    if len(bullets) < ai_settings.bullets_allowed:
        # 创建一颗子弹， 并将其加入到编组bullets中
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def get_number_aliens_x(ai_settings, alien_width):
    """计算每行可容纳多少个外星人"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

# 可用垂直空间： 将屏幕高度减去第一行外星人的上边距（外星人高度） 、 飞船的高度以及最初外星人群与飞船的距离（外星人高度的两倍）
# 将在飞船上方留出一定的空白区域， 给玩家留出射杀外星人的时间。


def get_number_rows(ai_settings, ship_height, alien_height):
    """计算屏幕可容纳多少行外星人"""
    available_space_y = (ai_settings.screen_height -
                         (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(ai_settings, screen, aliens,  alien_number, row_number):
    """创建一个外星人并将其放在当前行"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    """创建外星人群"""
    # 创建一个外星人， 并计算一行可容纳多少个外星人
    # 外星人间距为外星人宽度
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(
        ai_settings, ship.rect.height, alien.rect.height)
    # 创建第一行外星人
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """检查是否有外星人到达屏幕边缘然后更新所有外星人的位置"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # 检测外星人和飞船之间的碰撞  更新每个外星人的位置后立即检测外星人和飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        # 方法spritecollideany() 接受两个实参  一个被检查物 和 一个被检查编组  在这里，  检查编组是否有成员与被检查物碰撞
        # 它遍历编组aliens ， 并返回它找到的第一个与飞船发生了碰撞的外星人。
        print("Ship hit!!!")
        ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)  # 处理撞击

    # 检查是否有外星人到达屏幕底端
    check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets)


def check_fleet_edges(ai_settings, aliens):
    """有外星人到达边缘时采取相应的措施"""
    for alien in aliens.sprites():  # 遍历外星人群， 并对其中的每个外星人调用check_edges()
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """将整群外星人下移， 并改变它们的方向"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

# 有外星人撞到飞船时， 我们将余下的飞船数减1， 创建一群新的外星人， 并将飞船重新放置到屏幕底端中央


def ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """响应被外星人撞到的飞船"""
    if stats.ships_left > 0:
        # 将ships_left减1
        stats.ships_left -= 1
        # 更新记分牌
        sb.prep_ships()

        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()
        # 创建一群新的外星人， 并将飞船放到屏幕底端中央
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        # 暂停
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)  # 游戏结束后， 我们将重新显示光标


# 如果有外星人到达屏幕底端， 我们将像有外星人撞到飞船那样作出响应。
def check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """检查是否有外星人到达了屏幕底端"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # 像飞船被撞到一样进行处理
            ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
            break


def check_high_score(stats, sb):
    """检查是否诞生了新的最高得分"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()
