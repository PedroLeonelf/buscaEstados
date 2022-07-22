from Mapping import *
from Search import *
import time






begin = time.time()
map = Map()


search = Search(map.grafs[100][100], map.grafs[450][300], map.grafs)



resp = search.aStar()


vect = []
node = resp
while (node.father != None):
    vect.append(node)
    node = node.father
   
    
vect.append(node)

vect.reverse()
print(time.time() - begin)
map.showMap(vect)


# for nod in vect:
#     print(nod.x, nod.y)

