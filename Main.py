# execução: Main.py (posição inicial x) (posição inicial y) (posição final x) (posição final y) (grafoDeVisibilidade 1)
# exemplo sem grafo de visualização:  Main.py 10 10 100 100 
# exemplo com grafo de visualização:  Main.py 10 10 100 100 1
from Tester import *
import sys



x,y,x1,y1 = sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4]
useVisGraph = False
if len(sys.argv) == 6 and sys.argv[5] == '1' :
    useVisGraph = True
tester = Tester(x,y,x1,y1,useVisGraph)







