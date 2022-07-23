

class Node:
    def __init__(self, x, y, isEmpty) -> None:
        self.x = x
        self.y = y
        self.isEmpty = isEmpty
        self.neighboors = {}
        self.func = None
        self.gCost = None
        self.hCost = None
        self.father = None
    
    def getPos(self) -> (int):
        return (self.x, self.y)
    
    def getCosts(self) -> str:
        return f'g = {self.gCost} h = {self.hCost} f = {self.func}'
    

    


    

