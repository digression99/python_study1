import math

class Player:
    def __init__(self, posX, posY):
        self.posX = posX
        self.posY = posY

    def changePos(self, posX, posY):
        self.posX, self.posY = posX, posY

    def jump(self):
        self.posY += 3

    def reset(self):
        self.posX = self.posY = 0

class GameMap:
    def __init__(self):
        self.map = list()
        for i in range(0, 10):
            self.map.append(list([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))

    def reset(self):
        for i in range(0, 10):
            for j in range(0, 10):
                self.map[i][j] = 0

class GamePlay:
    def __init__(self):
        self.gameMap = GameMap()
        self.player = Player(0, 0)

    def gameReset(self):
        self.gameMap.reset()
        self.player.reset()

    def gameStart(self):
        while 1:
            pass





#def gameReset()