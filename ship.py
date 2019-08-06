import pygame
class Ship():
    def __init__(self, ai_setting, screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen
        self.ai_setting = ai_setting
        # 获取绝对路径
        # self.root_path = __file__.replace('ship.py','')
        #加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('.\\images\\\\ship1.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部 
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # self.rect.centery = self.screen_rect.bottom - self.ai_setting.ship_height
        self.centerx = float(self.rect.centerx)
        self.bottom = float(self.rect.bottom)
        #移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """根据移动标志调整飞船位置"""
        # 更新飞船的center值 而不是rect 因为centerx只能接受整数 转换一下
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_setting.ship_speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.centerx -= self.ai_setting.ship_speed_factor
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.bottom -= self.ai_setting.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.bottom += self.ai_setting.ship_speed_factor
        # 根据self.center更新rect对象
        self.rect.centerx = self.centerx
        self.rect.bottom = self.bottom

    def ship_center(self):
        self.centerx = self.screen_rect.centerx
        self.rect.centerx = self.centerx
        self.bottom = self.screen_rect.bottom
        self.rect.bottom = self.bottom

    def blitme(self):
        """指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)

"""
使用函数
加载图片 pygame.image.load()
屏幕定位 screen.rect()
得到定位 screen.get_rect()
绘制 screen.blit()
"""