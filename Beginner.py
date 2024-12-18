class 初心者():    
    def __init__(self, 姓名, 攻擊力=10, 防禦力=5, 血量=100): # constructor
        self.姓名 = 姓名
        self.攻擊力 = 攻擊力
        self.防禦力 = 防禦力
        self.血量 = 血量
    
    def 普通攻擊(self, 玩家): # method
        if(玩家.防禦力 < self.攻擊力):
            傷害 = self.攻擊力 - 玩家.防禦力
            玩家.設定血量(玩家.血量 - 傷害)
            print(f"{self.姓名}使用普通攻擊，攻擊了{玩家.姓名}，造成{傷害}點傷害。")
        else:
            print("普通攻擊無效")

    def 設定血量(self, 修改後血量):
        self.血量 = 修改後血量

    def 狀態(self):
        print(f"遊戲ID:{self.姓名}")
        print(f"攻擊力:{self.攻擊力}")
        print(f"防禦力:{self.防禦力}")
        print(f"血量:{self.血量}")