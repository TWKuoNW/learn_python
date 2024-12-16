import tkinter as tk

class GameUI:
    def __init__(self, root):
        # 介面設計
        self.root = root
        self.root.title("猜數字遊戲")
        # self.root.iconbitmap('favicon.ico')
        self.root.geometry("640x480") # 視窗大小

        self.menubar = tk.Menu(self.root) # 建立主選單
        
        self.newGame = tk.Menu(self.menubar)  # 建立子選單，選單綁定 menubar 主選單
        self.menubar.add_command(label="新遊戲", command = self.new_game) # 
        
        self.store = tk.Menu(self.menubar) 
        self.menubar.add_cascade(label = '商店', menu = self.store) # 建立主選單，內容為子選單

        self.bag = tk.Menu(self.menubar)
        self.menubar.add_cascade(label = '背包', menu = self.bag)

        self.record = tk.Menu(self.menubar)
        self.menubar.add_cascade(label = '紀錄', menu = self.record)

        self.root.config(menu = self.menubar) # 主視窗加入主選單
                
        self.label = tk.Label(root, text="請輸入 1 到 100 之間的數字：")
        self.label.pack(pady=10)
        
        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)
        
        self.button = tk.Button(root, text="猜一猜", command=self.nothing)
        self.button.pack(pady=10)
        
        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady = 5)

    def nothing(self):
        pass

    def new_game(self):
        print("新遊戲")

if(__name__ == "__main__"):
    # 創建主視窗
    root = tk.Tk()
    game = GameUI(root)
    root.mainloop()