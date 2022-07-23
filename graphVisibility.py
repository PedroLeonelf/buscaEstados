from Node import *
from Search import DIAGONAL

RIGHT = (0,1)
LEFT = (0,-1)
DOWN = (1,0) 
UP = (-1,0)
UPLEFT = (-1,-1)
UPRIGHT = (-1,1)
DOWNLEFT= (1,-1)
DOWNRIGHT = (1,1)

class GraphVisibility:
    def __init__(self, grid, searchObj) -> None:
        self.grid = grid
        
        self.corners = {}
        self.searchObj = searchObj
        self.defineCorners()
        self.defineCornersEdges()
        

    def defineCorners(self) -> list:      

        for line in self.grid:
            for node in line:
                if not node.isEmpty:
                    neighboors = self.getNeighboors(node)
                    if len(neighboors) < 5 : continue # filtrar cantos para não sobrecarregar o algoritmo
                    self.markCorners(node,neighboors)

    
    def getNeighboors(self, node) -> set():
        neighboors = set()
        x, y = node.x , node.y 
        for x1 in range(x-1, x + 2):
            if 0 > x1 or x1 > len(self.grid ) -1  : continue # fora do mapa
            for y1 in range(y-1, y + 2):
                if 0 > y1 or y1 > len(self.grid[0] ) -1 or x1 == x and y1 == y: # fora do mapa ou vizinho igual ao atual
                    continue
                if not self.grid[x1][y1].isEmpty: # bloqueado  
                    continue
                neighboors.add(self.grid[x1][y1])
        return neighboors



    def markCorners(self, node, neighboors) -> None:
        x,y = node.x, node.y
        for neighboor in neighboors:
            if self.searchObj.distance(node,neighboor) == DIAGONAL and not self.searchObj.diagonalBlock(x,y,neighboor.x, neighboor.y):
                self.corners[neighboor.getPos()] = neighboor

    def defineCornersEdges(self):
        for node in self.corners.values():
            self.getHreach(node)
    
    def defineBeginEndEdges(self, begin, end):
        self.getHreach(begin)
        self.getHreach(end)
        for k,v in end.neighboors.items():
            self.grid[int(k.split(':')[0])][int(k.split(':')[1])].neighboors[f'{end.x}:{end.y}'] = v
    
    
     


    
    def getEdges(self) -> dict:
        dict = {}
        for node in self.corners.values():
            dict[node.getPos()] = node.neighboors
        return dict

    def getHreach(self, node) -> None:
        self.actualNode = node
        maxUp = self.clearence(node, UP)
        maxLeft = self.clearence(node, LEFT)
        maxRight = self.clearence(node, RIGHT)
        maxDown = self.clearence(node, DOWN)
        self.getDiagonals(node, UPRIGHT, maxUp, maxRight)
        self.getDiagonals(node, UPLEFT, maxUp, maxLeft)
        self.getDiagonals(node, DOWNLEFT, maxDown, maxLeft)
        self.getDiagonals(node, DOWNRIGHT, maxDown, maxRight)
    
    def getDiagonals(self, node, diagonal, limitUpDown, limitLeftRight) -> None:
        self.clearence(node, diagonal)
        x,y = node.x + diagonal[0] , node.y + diagonal[1]
        moves = 0
        while(not self.outOrBlock(x, y)):
            node = self.grid[node.x + diagonal[0]][ node.y + diagonal[1]]
            moves += DIAGONAL
            if diagonal == UPRIGHT:
                self.clearence(node,UP, moves, limitUpDown)
                self.clearence(node,RIGHT,moves, limitLeftRight)
            elif diagonal == UPLEFT:
                self.clearence(node,UP, moves, limitUpDown)
                self.clearence(node,LEFT, moves, limitLeftRight)
            elif diagonal == DOWNLEFT:
                self.clearence(node,DOWN, moves, limitUpDown)
                self.clearence(node,LEFT, moves, limitLeftRight)                
            elif diagonal == DOWNRIGHT:
                self.clearence(node,DOWN, moves, limitUpDown)
                self.clearence(node,RIGHT, moves, limitLeftRight)
            x += diagonal[0]
            y += diagonal[1]                


    def clearence(self, node, direction, previousMove = 0, limit = None) -> int:
        moves, x, y = 0, node.x + direction[0], node.y + direction[1]
        if limit != None:
            if moves+ 1 + previousMove > limit: return 0
        while not self.outOrBlock(x,y):
            if self.isCorner(x,y) and f'{x}:{y}'not in self.actualNode.neighboors: 
                self.actualNode.neighboors[f'{x}:{y}'] = ((moves + 1) * self.getValueDirection(direction) + previousMove)
            x += direction[0]
            y += direction[1]
            moves+=1
        return moves
   

    def outOrBlock(self, x, y) -> bool:
        outOfMap = (0 > x or x > len(self.grid ) -1 or  0 > y or y > len(self.grid[0] ) -1) 
        if outOfMap : return True
        block = not self.grid[x][y].isEmpty
        return block
    
    def isCorner(self, x, y):
        return self.grid[x][y].getPos() in self.corners.keys()
    
    def getValueDirection(self, direction):
        if direction in [UP, RIGHT, DOWN, LEFT]:
            return 10
        return 14





