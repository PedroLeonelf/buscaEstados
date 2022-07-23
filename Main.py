import graphlib
from Mapping import *
from Search import *
import time

from graphVisibility import *

begin = time.time()
map = Map()
search = Search(map.grafs[0][0], map.grafs[0][7], map.grafs)
gv = GraphVisibility(map.grafs, search)



# resp = search.aStar()
# vect = []
# node = resp
# while (node.father != None):
#     vect.append(node)
#     node = node.father
# vect.append(node)
# vect.reverse()
print(time.time() - begin)
map.showMap(corners=gv.corners.keys())




