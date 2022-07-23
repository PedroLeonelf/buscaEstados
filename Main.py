from Mapping import *
from Search import *
import time
from graphVisibility import *


map = Map()
begin,end = map.grafs[10][10], map.grafs[900][900]

withVisGraph = False
if withVisGraph:
    search = Search(begin, end, map.grafs, hasVisGraph= True)
    gv = GraphVisibility(map.grafs, search)
    gv.defineBeginEndEdges(begin,end)
else:
    search = Search(begin, end, map.grafs, hasVisGraph= False)
beginTime = time.time()
resp = search.aStar()
vect = []
node = resp
while (node.father != None):
    vect.append(node)
    node = node.father
vect.append(node)
vect.reverse()
print(time.time() - beginTime)
if withVisGraph:
    map.showMap(vect=vect,corners=gv.corners.keys(), edges = gv.getEdges(), connect= True)
else:
    map.showMap(vect)




