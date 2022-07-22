import time
from Node import *
import operator

CARDINAL = 10
DIAGONAL = 14

class Search:
    
    def __init__(self, begin, objective,grid):
        self.grid = grid
        self.begin = begin
        self.objective = objective
        self.begin.func = 0
        self.getTot = 0
        
    
    def aStar(self):
        actual = self.begin
        openDic = {f'{actual.x}:{actual.y}' : actual.func}
        
        closedSet = set()
        actual.gCost = 0
        actual.Fcost = 0
        
        while openDic != {}:
            
            inicio = time.time()
            actual = self.getMinorNode(openDic)
            self.getTot += time.time() - inicio

            closedSet.add(f'{actual.x}:{actual.y}')
            openDic.pop(f'{actual.x}:{actual.y}')
            
            if actual == self.objective:
                print('total:',self.getTot) 
                return actual, closedSet
            
            neighboors = self.getNeighboors(actual)
            for neighboor in neighboors:
                
                
                if f'{neighboor.x}:{neighboor.y}' in closedSet:
                     continue
                
                if f'{neighboor.x}:{neighboor.y}' not in openDic.keys(): 
                    
                    neighboor.father = actual
                    self.calculateFunc(actual, neighboor)
                    openDic[f'{neighboor.x}:{neighboor.y}'] = neighboor.func
                    
                elif f'{neighboor.x}:{neighboor.y}'in openDic.keys() and self.checkGcost(neighboor, actual):
                    self.calculateFunc(actual, neighboor)
                    neighboor.father = actual
                
                
                
                





            
            # print(actual.getPos())
            # for neighboor in self.getNeighboors(actual):
            #     print('-- Vizinho:',neighboor.getPos(), neighboor.getCosts())
            # enter = input('pressione para continuar:')
            


    

    def getNeighboors(self, actual) -> set:

        neighboors = set()
        x, y = actual.x , actual.y 
        for x1 in range(x-1, x + 2):
            if 0 > x1 or x1 > len(self.grid ) -1  : continue # fora do mapa
            for y1 in range(y-1, y + 2):
                if 0 > y1 or y1 > len(self.grid[0] ) -1 or x1 == x and y1 == y: # fora do mapa 
                    continue
                if not self.grid[x1][y1].isEmpty: # bloqueado  
                    continue
                if self.diagonalBlock(x,y,x1,y1): continue
                neighboors.add(self.grid[x1][y1])
        
        return neighboors
    
    def diagonalBlock(self, x, y, x1, y1) -> bool: # em caso de consideração de canto como vizinho verifica se não a bloqueio ao redor
        if x1 == x - 1 and y1 == y - 1 and (not self.grid[x1+1][y1].isEmpty or not self.grid[x1][y1+1].isEmpty):  #canto superior esquerdo
            return True
        elif x1 == x+1 and y1 == y-1 and (not self.grid[x1-1][y1].isEmpty or not self.grid[x1][y1+1].isEmpty):    # canto inferior esquerdo
            return True
        elif x1 == x-1 and y1 == y+1 and (not self.grid[x1][y1-1].isEmpty or not self.grid[x1+1][y1].isEmpty):    # canto superior direito
            return True
        elif x1 == x+1 and y1 == y+1 and (not self.grid[x1][y1-1].isEmpty or not self.grid[x1-1][y1].isEmpty):    # canto inferior direito
            return True

        return False

    def calculateFunc(self, actual, neighboor) -> None:
        
        gCost = self.distance(actual, neighboor) + actual.gCost
        hCost = self.hCost(neighboor)
        neighboor.gCost = gCost
        neighboor.hCost = hCost
        neighboor.func = gCost + hCost


    def hCost(self, neighboor) -> int:
        distX = abs(neighboor.x - self.objective.x)
        distY = abs(neighboor.y - self.objective.y)
        if distX > distY:
            return DIAGONAL * distY + CARDINAL * (distX - distY)
        return DIAGONAL * distX + CARDINAL * (distY - distX)
    





    def distance(self, actual, neighboor) -> int:
        if (actual.x == neighboor.x + 1 and actual.y == neighboor.y) or (actual.y == neighboor.y and actual.x == neighboor.x - 1): # cardinal cima e baixo
            return CARDINAL
        elif (actual.y == neighboor.y + 1 and actual.x == neighboor.x) or (actual.x == neighboor.x and actual.y == neighboor.y - 1): # cardinal esquerda e direita
            return CARDINAL
        return DIAGONAL

    
    def checkGcost(self, neighboor, actual) -> bool:
        oldGcost = neighboor.gCost
        newGcost = actual.gCost + self.distance(actual, neighboor)
        return newGcost < oldGcost
    



    def getMinorNode(self, dic) -> Node:
        
        # key = min(dic.items(), key=operator.itemgetter(1))[0]
        key = min(dic, key=dic.get) # performace 1
        x,y = key.split(':')[0], key.split(':')[1]
        
        return self.grid[int(x)][int(y)]







