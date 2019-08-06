
class GameStats():
    """跟踪游戏的统计信息"""
    def __init__(self, ai_setting):
        """初始化统计信息"""
        self.ai_setting = ai_setting
        self.game_active = False
        self.reset_stats()

    def reset_stats(self):
        """初始化在游戏运行期间可能的变化的信息统计"""
        self.ships_left = self.ai_setting.ship_limit

    def reset_stats(self):
        """初始化随游戏进行可能变化的统计信息"""
        self.ships_left = self.ai_setting.ship_limit
        self.score = 0
        