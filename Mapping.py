from PIL import Image
import matplotlib.pyplot as plt 
from matplotlib import image as showImg
from Node import *
class Map:
    def __init__(self) -> None:
        self.img = Image.open('imagem.png')
        self.pix = self.img.load()
        self.makeMap()

    def makeMap(self) -> None:
        self.map = []
        for i in range(0, self.img.height):
            vect = []
            for j in range(0, self.img.width):
                vect.append(1) if self.pix[i,j][0] != 0 else vect.append(0)
            self.map.append(vect)    

    def showMap(self):
        plot_grid = [
        [[y * 255, y * 255, y * 255] for y in x]
        for x in self.map
        ]
        print(self.map)
        plt.imshow(plot_grid)
        plt.show()

    
    def getCorners(self):
        corners = []
        for i in range(self.img.width):
            for j in range(self.img.height):
                if self.checkCorner(i,j,self.map[i][j]):corners.append(1) 

        



map = Map()
map.showMap()
