from PIL import Image
import matplotlib.pyplot as plt 
from Node import *
import time

# começar com grafos
class Map:
    def __init__(self) -> None:
        self.img = Image.open('imagem.png')
        self.pix = self.img.load()
        self.grafs = []
        inicio = time.time()
        self.makeMap()
        print(f'Time to make grid:{time.time()-inicio}')
  

    def makeMap(self) -> None:
        
        # self.map = [[1,1,1,1,1,1,0,1],[1,0,0,1,1,1,0,1],[1,1,1,1,1,1,0,1],[1,1,1,1,1,1,0,1],[1,1,1,1,1,1,1,1]] #testes
        for i in range(self.img.height): 
            vect = []
            for j in range(self.img.width):
                vect.append(Node(i,j, 1 if self.pix[j,i][0] != 0 else 0))
            self.grafs.append(vect) # matriz de Nodos

    def showMap(self, vect = None, corners = None, edges = None, connect = False) -> None:
        plotGrid = [[[y.isEmpty * 255, y.isEmpty * 255, y.isEmpty * 255] for y in x] for x in self.grafs]

        # xCorner, yCorner = [], [] # ver cantos do grafo de visualização
        # for corner in corners:
        #     xCorner.append(corner[1])
        #     yCorner.append(corner[0])
        # plt.scatter(xCorner, yCorner, color='brown') 

        # for k,v in edges.items():# ver arestas do grafo de visualização
        #     for dic in v:
        #         point = [k[1], int(dic.split(':')[1])]
        #         points2 = [k[0],int(dic.split(':')[0])]
        #         plt.plot(point, points2, color = 'purple')
        x = []
        y = []
        for node in vect: # caminho percorrido
            x.append(node.y)
            y.append(node.x)
        if connect: # se for grafo de visualização
            plt.plot(x,y) # linha
        else:
            plt.scatter(x,y)# pontos
        plt.scatter(x[0],y[0],color='green') # inicio
        plt.scatter(x[-1],y[-1],color='red') # fim
        
        plt.imshow(plotGrid)
        plt.show()

    




        


    


                



                



        







