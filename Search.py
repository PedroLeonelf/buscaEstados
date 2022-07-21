from hashlib import new
from Node import *

CARDINAL = 10
DIAGONAL = 14

class Search:
    def __init__(self, begin, objective,grid):
        self.grid = grid
        self.begin = begin
        self.objective = objective
        self.begin.func = 0
    
    def aStar(self):
        actual = self.begin
        openLst = [actual]
        closedLst = []
        while openLst != []:

            actual = self.getBiggerNode(openLst)
            print(actual.x, actual.y)
            for n in self.getNeighboors(actual):
                print('--', n.x, n.y, 'father:', n.father)
            pause = input('enter:')
            openLst.remove(actual)
            closedLst.append(actual)
            if actual == self.objective:
                return 'yes'
            
            
        
            for neighboor in self.getNeighboors(actual):
                if neighboor in closedLst:
                     continue
                if neighboor not in openLst:
                    neighboor.father = actual
                    print('sim', neighboor.x, neighboor.y, neighboor.father)
                    self.calculateFunc(actual, neighboor)
                    openLst.append(neighboor)
                elif neighboor in openLst and self.checkGcost():
                    self.calculateFunc(actual, neighboor)
                    neighboor.father = actual
            


    

    def getNeighboors(self, actual) -> list:
        vect = []
        x, y = actual.x , actual.y 
        for x1 in range(x-1, x + 2):
            if 0 > x1 or x1 > len(self.grid ) -1  : continue # fora do mapa
            for y1 in range(y-1, y + 2):
                if 0 > y1 or y1 > len(self.grid[0] ) -1 or x1 == x and y1 == y: # fora do mapa  
                    continue
                if self.grid[x1][y1] == 0: # bloqueado  
                    continue
                if self.diagonalBlock(x,y,x1,y1): continue
                vect.append(Node(x1,y1,0))
        return vect
    
    def diagonalBlock(self, x, y, x1, y1) -> bool: # em caso de consideração de canto como vizinho verifica se não a bloqueio ao redor
        if x1 == x - 1 and y1 == y - 1 and (self.grid[x1+1][y1] == 0 or self.grid[x1][y1+1] == 0):  #canto superior esquerdo
            return True
        elif x1 == x+1 and y1 == y-1 and (self.grid[x1-1][y1] == 0 or self.grid[x1][y1+1] == 0):    # canto inferior esquerdo
            return True
        elif x1 == x-1 and y1 == y+1 and (self.grid[x1][y1-1] == 0 or self.grid[x1+1][y1]):         # canto superior direito
            return True
        elif x1 == x+1 and y1 == y+1 and (self.grid[x1][y1-1] == 0 or self.grid[x1-1][y1] == 0):    # canto inferior direito
            return True

        return False

    def calculateFunc(self, actual, neighboor) -> None:
        gCost = self.gCost(actual, neighboor)
        hCost = self.hCost(neighboor)
        neighboor.gCost = gCost
        neighboor.hCost = hCost
        neighboor.func = gCost + hCost


    def hCost(self, neighboor) -> int:
        distX = abs(neighboor.x - self.objective.x)
        distY = abs(neighboor.y - self.objective.y)
        return int(CARDINAL * (abs(distX - distY) + min(distX, distY) * DIAGONAL))


    def gCost(self, actual, neighboor) -> int:
        if (actual.x == neighboor.x + 1 and actual.y == neighboor.y) or (actual.y == neighboor.y and actual.x == neighboor.x - 1): # cardinal cima e baixo
            return CARDINAL
        elif (actual.y == neighboor.y + 1 and actual.x == neighboor.x) or (actual.x == neighboor.x and actual.y == neighboor.y - 1): # cardinal esquerda e direita
            return CARDINAL
        return DIAGONAL

    
    def checkGcost(self, neighboor, actual) -> bool:
        oldGcost = neighboor.gCost
        newGcost = actual.gCost + self.gCost(actual, neighboor)
        return newGcost < oldGcost
    
    def getBiggerNode(self, lst) -> Node:
        bigger = 0
        for node in lst:
            if node.func > bigger: 
                bigger = node.func
        return list(filter(lambda it : it.func == bigger, lst))[0]



