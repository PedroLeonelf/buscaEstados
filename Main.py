from Mapping import *
from Search import *


gridTest = [[1,1,1,1,1,1,0,1],[1,0,0,1,1,1,0,1],[1,1,1,1,1,1,0,1],[1,1,1,1,1,1,0,1],[1,1,1,1,1,1,1,1]]
search = Search(Node(0,0,0), Node(0,7,0), gridTest)
print(search.aStar())
