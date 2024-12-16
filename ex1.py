import random # 引入亂數函式庫

ans = int(random.random() * 100) + 1 # 運用亂數建立一隨機答案
max = 100   # 設定答案的上限數字
min = 1     # 設定答案的下限數字

while(True): # 無窮迴圈
    print(f"請猜數字 {min} ~ {max} : ", end = "") # 提示玩家答案範圍
    try:
        player = int(input()) # 玩家輸入的數字存入player變數
        # 判斷答案是否正確
        if(player == ans): # 玩家猜對了
            print("答對了")
            
            player_input = input("是否繼續遊玩:")

            # 判斷玩家是否想繼續遊玩
            if(player_input == 'y'): # 想
                # 重新生成一個新答案，並且重置範圍
                ans = int(random.random() * 100) + 1 
                max = 100
                min = 1 
            else: # 不想
                print("感謝遊玩，遊戲結束")
                break
        elif(player > ans and player < max): # 玩家猜的數字比答案大
            max = player # 最大數字變成玩家所猜的數字
        elif(player < ans and player > min): # 玩家猜的數字比答案小
            min = player # 最小數字變成玩家所猜的數字
            
    except:
        print('輸入錯誤')