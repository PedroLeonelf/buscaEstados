from Search import *
from GraphVisibility import *
from Mapping import *
import time
import random
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
            print(f'Tempo para fazer o grafo de visualização:{time.time() - inicio}')
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




class OneHundredPoints:
    def __init__(self) -> None:
        self.map = Map()
        self.points = [(random.randrange(1, len(self.map.grafs[0]), 1),random.randrange(1, len(self.map.grafs[0]), 1)) for _ in range(100)]
        self.changeBlockPoints()
        print(f'Random points:{self.points}')
        self.makeVisGraph()
        self.makeSearchs()    
    def changeBlockPoints(self) -> None:
        for idx, _ in enumerate(self.points):
            x,y = self.points[idx][0],self.points[idx][1]
            while not self.map.grafs[x][y].isEmpty: # Enquanto tiver ponto bloqueado troca por outro aleatorio
                self.points[idx] = (random.randint(1, len(self.map.grafs[0])-1), random.randint(1, len(self.map.grafs[0])-1))
                x,y = self.points[idx][0],self.points[idx][1]


    def makeVisGraph(self) -> None:
        inicio = time.time()
        self.gv = GraphVisibility(self.map.grafs, Search(self.map.grafs[0][0],self.map.grafs[0][1],self.map.grafs, True))
        print(f'Time to make Visibility Graph:{time.time() - inicio}s')



    def makeSearchs(self) -> None:
        
        for searchIdx in range(50):
            begin,objective = self.map.grafs[self.points[searchIdx][0]][self.points[searchIdx][1]], self.map.grafs[self.points[searchIdx+50][0]][self.points[searchIdx+50][1]]
            searchAStar = Search(begin, objective, self.map.grafs, hasVisGraph= False)
            searchVisGraph = Search(begin, objective, self.map.grafs, hasVisGraph= True)
            self.gv.defineBeginEndEdges(begin,objective)
            # aStar
            beginTime = time.time()
            node, openList = searchAStar.aStar()
            self.writeInfo(f'{searchIdx+1}-Astar {self.points[searchIdx]} -> {self.points[searchIdx+50]} - time:{round(time.time() - beginTime,2)}s, openNodes:{len(openList)}, distance:{node.func}')
            # VisGraph
            beginTime = time.time()
            node, openList = searchVisGraph.aStar()
            self.writeInfo(f'{searchIdx+1}-VisGraph {self.points[searchIdx]} -> {self.points[searchIdx+50]} - time:{round(time.time() - beginTime,5)}s, openNodes:{len(openList)}, distance:{node.func}')
            self.writeInfo(' ')

    def writeInfo(self, txt) -> None:
        with open('OneHundredPoints.txt', 'a') as file:
            file.write(txt + '\n')
    
 
        

        

