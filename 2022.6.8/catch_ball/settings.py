class Settings():
    """存储游戏所有设置的类"""

    def __init__(self):
        """初始化游戏设置"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (193, 210, 240)

        # 狗狗的设置
        self.dog_speed_factor = 1.5

        # 球的设置
        self.ball_speed_factor = 0.9
        self.ball_limit = 3
