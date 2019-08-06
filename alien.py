import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """表示单个外星人的类"""
    def __init__(self, ai_setting, screen):
        """初始化外星人并设置其起始位置"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_setting = ai_setting

        # 加载外星人图像 并设置其rect属性
        # self.root_path = __file__.replace('alien.py','')
        self.image = pygame.image.load('.\\images\\alien1.bmp')
        self.rect = self.image.get_rect()

        # 每个外星人的最初位置都在屏幕左上角附近
        """
        随机出现的x的位置 width 至 screen-width
        """
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # 储存外星人的准确位置
        self.x = float(self.rect.x)

        # 计算每行存储的外星人数量 及可以容纳多少行
        self.available_space_x = ai_setting.screen_width - (2 * self.x)
        self.number_aliens_x = int(self.available_space_x / (2 * self.x))
        self.available_space_y = (ai_setting.screen_height - (3 * self.rect.height) - ai_setting.ship_height)
        self.number_rows = int(self.available_space_y / (2 * self.rect.height))

    def blitme(self):
        """在指定位置绘制外星人"""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """如果外星人位于屏幕边缘 就返回True"""
        if self.rect.right >= self.ai_setting.screen_width:
            return True
        elif self.rect.left <= 0:
            return True
    def update(self):
        """更新外星人位置"""
        self.x += (self.ai_setting.alien_speed_factor * self.ai_setting.fleet_direction)
        self.rect.x = self.x
