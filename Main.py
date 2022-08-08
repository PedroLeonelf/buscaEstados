# execução: python3 Main.py (posição inicial x) (posição inicial y) (posição final x) (posição final y) (grafoDeVisibilidade 1)
# exemplo com 100 pontos aleatorios:  python3 Main.py
# exemplo sem grafo de visualização:  python3 Main.py 10 10 100 100 
# exemplo com grafo de visualização:  python3 Main.py 10 10 100 100 1

from Tester import *
import sys

if __name__ == '__main__': # Main
    if len(sys.argv) == 1:
        OneHundredPoints()
    x,y,x1,y1 = sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4]
    useVisGraph = False # sem grafo de visualização
    if len(sys.argv) == 6 and sys.argv[5] == '1' :
        useVisGraph = True # com grafo de visualização
    tester = Tester(x,y,x1,y1,useVisGraph)