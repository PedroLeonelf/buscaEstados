from Node import *
from Search import DIAGONAL
import enum
 
# directions enum


class Directions(enum.Enum):
    RIGHT = 1
    LEFT = 2
    DOWN = 3 
    UP = 4
    UPLEFT = 5
    UPRIGHT = 6
    DOWNLEFT= 7
    DOWNRIGHT = 8



class GraphVisibility:
    def __init__(self, grid, searchObj) -> None:
        self.grid = grid
        
        self.corners = {}
        self.searchObj = searchObj
        self.defineCorners()
        print('Moves:',self.clearence(self.grid[2][3], Directions.RIGHT))

    def defineCorners(self) -> list:      
         
        for line in self.grid:
            for node in line:
                if not node.isEmpty:
                    neighboors = self.getNeighboors(node)
                    if len(neighboors) < 5 : continue # filtrar cantos para não sobrecarregar o algoritmo
                    self.markCorners(node,neighboors)

    
    def getNeighboors(self, node) -> list:
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


    def getHreach(self, node, cardinal, diagonal) -> list:
        subgoal = []
        maxLineLen = self.clearence(node)
        maxDiagMov = self.clearence(node)
        for i in range(maxDiagMov):
            pass

    def clearence(self, node, direction) -> int:
        moves, x, y = 0, node.x, node.y
        if direction == Directions.UP:
            while not self.cornerOrBlock(x-1,y):
                x =-1
                moves+=1
        elif direction == Directions.DOWN:
            while not self.cornerOrBlock(x+1,y):
                x += 1
                moves +=1 
        elif direction == Directions.LEFT:
            while not self.cornerOrBlock(x,y-1):
                y -= 1
                moves+=1
        elif direction == Directions.RIGHT:
            while not self.cornerOrBlock(x,y+1):
                y+=1
                moves+=1
        return moves+1    

    def cornerOrBlock(self, x, y) -> bool:
        block = not self.grid[x][y].isEmpty
        corner = self.grid[x][y].getPos() in self.corners.keys()
        outOfMap = (0 > x or x > len(self.grid ) -1 or  0 > y or y > len(self.grid[0] ) -1)  
        return  block or corner or outOfMap



# GetDirectHReachable(cell s, cardinal dir. c, diagonal dir. d)
    # SubgoalVector list = {};
    # int maxLineLength = Clearance(s,c);
    # int nDiagMoves = Clearance(s,d);
    # for int i = 1 ... nDiagMoves
        # s = neighbor of s toward d;
        # l = Clearance(s,c);
        # if (l < maxLineLength)
            # maxLineLength = l;
            # s’ = the cell l+1 moves away from s toward c;
            # if (s’ is a subgoal)
                # list.add(s’);

    # return list;