class GameStats():
    """跟踪游戏的统计信息"""

    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()

        self.game_active = True

    def reset_stats(self):
        self.ball_not_catch = 0
