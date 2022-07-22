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
        actual.gCost = 0
        while openLst != []:
            actual = self.getMinorNode(openLst)
            # for node in openLst:
            #     print(node.getPos(), node.func, node.gCost, node.hCost)
            # enter = input('enter:')
            # print(f"Actual:{actual.getPos()}")

            closedLst.append(actual)
            openLst.remove(actual)
            if actual == self.objective:
                return actual
            if actual != self.begin:
                print(actual.getPos(), actual.getCosts(), actual.father.getPos())
            for neighboor in self.getNeighboors(actual):
                
                if neighboor in closedLst:
                     continue
                if neighboor not in openLst:
                    neighboor.father = actual
                    self.calculateFunc(actual, neighboor)
                    openLst.append(neighboor)
                elif neighboor in openLst and self.checkGcost(neighboor, actual):
                    self.calculateFunc(actual, neighboor)
                    neighboor.father = actual





            
            # print(actual.getPos())
            # for neighboor in self.getNeighboors(actual):
            #     print('-- Vizinho:',neighboor.getPos(), neighboor.getCosts())
            # enter = input('pressione para continuar:')
            


    

    def getNeighboors(self, actual) -> list:
        neighboors = []
        x, y = actual.x , actual.y 
        for x1 in range(x-1, x + 2):
            if 0 > x1 or x1 > len(self.grid ) -1  : continue # fora do mapa
            for y1 in range(y-1, y + 2):
                if 0 > y1 or y1 > len(self.grid[0] ) -1 or x1 == x and y1 == y: # fora do mapa 
                    continue
                if not self.grid[x1][y1].isEmpty: # bloqueado  
                    continue
                if self.diagonalBlock(x,y,x1,y1): continue
                neighboors.append(self.grid[x1][y1])
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
    
    def getMinorNode(self, lst) -> Node:
        minor = lst[0].func
    
        return list(filter(lambda it : it.func == minor, lst))[0]







