from PIL import Image
import matplotlib.pyplot as plt 
from matplotlib import image as showImg
from Node import *
class Map:
    def __init__(self) -> None:
        self.img = Image.open('imagem.png')
        self.pix = self.img.load()
        self.makeMap()
        self.grafs = []

    def makeMap(self) -> None:
        self.map = []
        for i in range(0, self.img.height):
            vect = []
            for j in range(0, self.img.width):
                vect.append(1) if self.pix[i,j][0] != 0 else vect.append(0)
            self.map.append(vect)    

    def showMap(self) -> None:
        custom = [[1,1,1,1,1,1,0,1],[1,0,0,1,1,1,0,1],[1,1,1,1,1,1,0,1],[1,1,1,1,1,1,0,1],[1,1,1,1,1,1,1,1]]
        # plot_grid = [[[y * 255, y * 255, y * 255] for y in x] for x in self.map]
        plot_grid = [[[y * 255, y * 255, y * 255] for y in x] for x in custom]
        plt.imshow(plot_grid)
        plt.show()

    
    def setGrafos(self) -> None:
        
        for idx1, lst in enumerate(self.map):
            for idx2, blocked in enumerate(lst):
                self.grafs.append(Node(idx1, idx2, blocked))
        
        # for graf in self.grafs:
        #     self.addNeighboor(graf)

    
    def addNeighboor(self, graf) -> None:
        x, y = graf.x - 1, graf.y - 1
        for x1 in range(x, x + 2):
            if 0 < x1 < self.map.width  : continue # fora do mapa
            for y1 in range(y, y + 2):
                if 0 < y1 < self.map.height or self.getGraf(x1,y1).block :  # fora do mapa ou bloqueado
                    continue

                

    def getGraf(self, x,y) -> Node:
        return list(filter(lambda it : it.x == x and it.y == y, self.grafs))[0]

                



        







