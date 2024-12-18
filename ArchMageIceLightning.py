from Wizard import 法師

class 冰雷魔導士(法師):
    def __init__(self, 姓名, 攻擊力=30, 防禦力=20, 血量=200, 冰球攻擊=30, 落雷=40):   #更改基本數值
        super().__init__(姓名, 攻擊力, 防禦力, 血量)            #將上面更改數值回傳到第7-10的地方
        self.冰球攻擊 = 冰球攻擊                                      #冰球攻擊造成30傷害
        self.落雷 = 落雷                                          #落雷攻擊造成40傷害
    
    def 冰雷攻擊(self, 玩家):
        if(玩家.防禦力 < (self.冰球攻擊 + self.落雷)):            #假如玩家的防禦力低於冰球攻擊+落雷
            傷害 = self.冰球攻擊 + self.落雷 - 玩家.防禦力      #造成傷害，傷害=冰球攻擊30+落雷40-防禦力20
            玩家.設定血量(玩家.血量 - 傷害 )                    #設定血量= 血量200 - 傷害
            print(f"{self.姓名}使用冰雷攻擊，攻擊了{玩家.姓名}，造成{傷害}點傷害。")    
        else:
            print("冰雷魔法攻擊無效")
    
    def 技能列(self):
        return "可選的技能有 1:普通攻擊, 2:魔法攻擊, 3:冰雷攻擊"
    
    def 狀態(self): # override
        print(f"遊戲ID:{self.姓名}")
        print(f"攻擊力:{self.攻擊力}")
        print(f"防禦力:{self.防禦力}")
        print(f"法力:{self.法力}")
        print(f"冰球攻擊:{self.冰球攻擊}")
        print(f"落雷:{self.落雷}")
        print(f"血量:{self.血量}")