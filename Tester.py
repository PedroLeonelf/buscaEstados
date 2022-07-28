from Search import *
from GraphVisibility import *
from Mapping import *
import time
class Tester:
    def __init__(self, y,x,y1,x1,visGraph = False):
        self.map = Map()
        self.begin = self.map.grafs[int(x)][int(y)]
        self.objective = self.map.grafs[int(x1)][int(y1)]
        self.visGraph = visGraph
        self.makeSearch()
        
    def makeSearch(self):
        if self.begin.isEmpty == 0 or self.objective.isEmpty == 0:
            print("Begin and/or objective blocked(s)!")        
            return
        if self.visGraph:
            inicio = time.time()
            search = Search(self.begin, self.objective, self.map.grafs, hasVisGraph= True)
            gv = GraphVisibility(self.map.grafs, search)
            gv.defineBeginEndEdges(self.begin,self.objective)
            print(f'Time grafo de visualização:{time.time() - inicio}')
        else:
            gv = None
            search = Search(self.begin, self.objective, self.map.grafs, hasVisGraph= False)
        beginTime = time.time()
        node, openList = search.aStar()
        print('Time in seconds:',time.time() - beginTime)
        print('OpenNodes:', len(openList))
        print('Distance:', node.func)
        self.makeMapAndPath(node,gv)

    def makeMapAndPath(self, node,gv):
        vect = []
        while (node.father != None):
            vect.append(node)
            node = node.father
        vect.append(node)
        vect.reverse()
        if self.visGraph:
            self.map.showMap(vect=vect,corners=gv.corners.keys(), edges = gv.getEdges(), connect= True)
        else:
            self.map.showMap(vect=vect, connect= False)




