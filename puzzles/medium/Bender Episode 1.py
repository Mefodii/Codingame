import sys
import math


class Bender:
    # SOUTH == 0
    # EAST == 1
    # NORTH == 2
    # WEST == 3
    
    def __init__(self, gameMap):
        self.gameMap = gameMap
        self.pos = self.calculateStartPos()
        self.direction = 0
        self.invert = 1
        self.destination = self.calculateDestination()
        self.teleports = self.CalculateTeleports()
        self.breaker = False
        self.movesLog = []
        
        self.blockedLog = 0
        self.visitedLog = 0
        self.finish = False
        self.test = 0
        
    def calculateStartPos(self):
        x = 0
        y = 0
        for row in self.gameMap:
            for cell in row:
                if cell == "@":
                    pos = x,y
                    return pos
                x += 1
            x = 0
            y += 1
        
    def calculateDestination(self):
        x = 0
        y = 0
        for row in self.gameMap:
            for cell in row:
                if cell == "$":
                    pos = x,y
                    return pos
                x += 1
            x = 0
            y += 1
        
    def CalculateTeleports(self):
        t = []
        x = 0
        y = 0
        for row in self.gameMap:
            for cell in row:
                if cell == "T":
                    pos = x,y
                    t.append(pos)
                    x = 0
                    y = 0
                x += 1
            x = 0
            y += 1
        return t
    
    def printMap(self):
        for row in self.gameMap:
            print("".join(row), file=sys.stderr)

    def move(self):
        self.test +=1
        if self.test > 200:
            print(self.movesLog)
            print(self.pos, self.direction)
            exit(0)
        nextPos = self.tryMove()
        x = nextPos[0]
        y = nextPos[1]
        nextCell = self.gameMap[y][x]
        if nextCell == "#":
            if self.blockedLog > 4:
                self.finish = True
                self.movesLog = ["LOOP"]
            else:
                self.blockedLog += 1
                self.direction += self.invert%4
                self.move()
        elif nextCell == "X":
            if self.blockedLog > 4:
                self.finish = True
                self.movesLog = ["LOOP"]
            else:
                self.blockedLog += 1
                self.direction += self.invert%4
                print(self.direction)
                self.move()
        elif nextCell == "$":
            self.finish = True
            self.pos = nextPos
            self.addMove()
        elif nextCell == " " or nextCell == "@":
            self.pos = nextPos
            self.addMove()
        
        if(not self.finish):
            self.blockedLog = 0
    
    def addMove(self):
        if self.direction == 0:
            self.movesLog.append("SOUTH")
        elif self.direction == 1:
            self.movesLog.append("EAST")
        elif self.direction == 2:
            self.movesLog.append("NORTH")
        else:
            self.movesLog.append("WEST")
    
    def tryMove(self):
        if self.direction == 0:
            return [self.pos[0], self.pos[1]+1]
        elif self.direction == 1:
            return [self.pos[0]+1, self.pos[1]]
        elif self.direction == 2:
            return [self.pos[0], self.pos[1]-1]
        else:
            return [self.pos[0]-1, self.pos[1]]
    
    def run(self):
        while self.finish != True:
            self.move()
        for move in self.movesLog:
            print(move)
        
l, c = [int(i) for i in input().split()]
m = []
for i in range(l):
    row = list(input())
    m.append(row)

player = Bender(m)

player.printMap()
player.run()

