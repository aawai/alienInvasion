import pygame.font

class Button():
    def __init__(self, ai_setting, screen, msg):
        """初始化按钮的属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # 设置按钮尺寸和其他属性
        self.width, self.height = 200, 50
        self.button_color = (242, 5, 5)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None, 48)

        # 创建按钮的rect对象 并居中
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # 按钮标签只需要创建一次
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """"将msg渲染为图像， 并使其在按钮上居中"""
        self.msg_imgage = self.font.render(msg, True, self.text_color,
            self.button_color)
        self.msg_imgage_rect = self.msg_imgage.get_rect()
        self.msg_imgage_rect.center = self.rect.center

    def test(self, msg):
        print(msg)

    def draw_button(self):
        # 绘制按钮
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_imgage, self.msg_imgage_rect)