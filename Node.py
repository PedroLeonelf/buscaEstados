class Node:
    def __init__(self, x, y, blocked) -> None:
        self.x = x
        self.y = y
        self.blocked = blocked
        self.neighboors = []
        self.func = None
        self.gCost = None
        self.hCost = None
        self.father = None
    

    


    

