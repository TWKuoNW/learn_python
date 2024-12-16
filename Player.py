class Player():
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.gold = 0

    def setScore(self, score):
        self.score = score

    def setGold(self, gold):
        self.gold = gold
        
if(__name__ == "__main__"):
    KuoNW = Player("KuoNW")
    