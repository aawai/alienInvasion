"""
游戏设置类
"""
class Settings():
    def __init__(self):
        """初始化的游戏设置"""
        #屏幕设置
        self.screen_width = 500
        self.screen_height = 700
        #元组
        self.bg_color = (230,230,230)
        self.game_title = "Alien Invasion"
        """飞船设置"""
        #飞船半径
        self.ship_height = 60
        #移动步长
        self.ship_speed_factor = 1
        self.ship_limit = 2
        """子弹设置"""
        self.bullet_speed_factor = 2
        self.bullet_width = 3
        self.bullet_height = 12
        self.bullet_color = (60, 60, 60)

        """外星人设置"""
        # 移动速度
        self.alien_speed_factor = 0.3
        #撞到屏幕边缘 即下滑10个像素
        self.fleet_drop_speed = 10
        # fleet_direction为1表示向右移动 -1表示向左移动
        self.fleet_direction = 1
        # 加快游戏速度
        self.speedup_scale = 1.2

        """记分"""
        self.alien_points = 50

        self.initialize_dynamic_setting()

    def initialize_dynamic_setting(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed_factor = 1
        self.bullet_speed_factor = 2
        self.alien_speed_factor = 0.3

        # fleet_direction 为1表示向右为-1表示向左
        self.fleet_direction = 1
    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
