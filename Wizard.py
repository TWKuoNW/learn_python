from Beginner import 初心者

class 法師(初心者):
    def __init__(self, 姓名, 攻擊力=20, 防禦力=10, 血量=150, 法力=20): # constructor
        super().__init__(姓名, 攻擊力, 防禦力, 血量)
        self.法力 = 法力

    def 魔法攻擊(self, 玩家):
        if(玩家.防禦力 < self.法力):
            傷害 = self.法力 - 玩家.防禦力
            玩家.設定血量(玩家.血量 - 傷害)
            print(f"{self.姓名}使用魔法攻擊，攻擊了{玩家.姓名}，造成{傷害}點傷害。")
        else:
            print("魔法攻擊無效")

    def 狀態(self):
        print(f"遊戲ID:{self.姓名}")
        print(f"攻擊力:{self.攻擊力}")
        print(f"防禦力:{self.防禦力}")
        print(f"法力:{self.法力}")
        print(f"血量:{self.血量}")