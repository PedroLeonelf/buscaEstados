from matplotlib.pyplot import close
from Mapping import *
from Search import *
import time






begin = time.time()
map = Map()


search = Search(map.grafs[10][10], map.grafs[1000][1000], map.grafs)



resp, closedSet = search.aStar()


vect = []
node = resp
while (node.father != None):
    vect.append(node)
    node = node.father
   
    
vect.append(node)

vect.reverse()
print(time.time() - begin)
map.showMap(vect)




