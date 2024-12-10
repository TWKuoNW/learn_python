import time

class human():
    def __init__(self):  # 建立預設屬性的寫法
        self.eye = 2       # 兩個眼睛
        self.ear = 2       # 兩個耳朵
        self.nose = 1      # 一個鼻子
        self.mouth = 1     # 一張嘴巴
    
    def run(self):
        print("啟動跑步模式...")

    def sleep(self):
        print("睡覺...")

KuoNW = human()        
KuoNW.run()
time.sleep(5)
KuoNW.sleep()