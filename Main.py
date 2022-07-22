from Mapping import *
from Search import *
import time

map = Map()
begin = time.time()

search = Search(map.grafs[10][10], map.grafs[800][400], map.grafs)
resp, closedSet = search.aStar()
vect = []
node = resp
while (node.father != None):
    vect.append(node)
    node = node.father
   
    
vect.append(node)

vect.reverse()
print(time.time() - begin)
map.showMap(vect, closedSet)




