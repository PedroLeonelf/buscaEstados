from PIL import Image
import matplotlib.pyplot as plt 
from matplotlib import image as showImg
from Node import *
import time

# começar com grafos
class Map:
    def __init__(self) -> None:
        self.img = Image.open('imagem.png')
        self.pix = self.img.load()
        self.grafs = []
        self.map = []
        self.makeMap()

    def makeMap(self) -> None:
        
        # self.map = [[1,1,1,1,1,1,0,1],[1,0,0,1,1,1,0,1],[1,1,1,1,1,1,0,1],[1,1,1,1,1,1,0,1],[1,1,1,1,1,1,1,1]]
        
        # for i in range(0, self.img.height):
        #     vect = []
        #     for j in range(0, self.img.width):
        #         vect.append(1) if self.pix[i,j][0] != 0 else vect.append(0)
        #     self.map.append(vect)

        
        for i in range(self.img.height):
            vect = []
            for j in range(self.img.width):
                vect.append(Node(i,j, 1 if self.pix[j,i][0] != 0 else 0))
            self.grafs.append(vect)
        # self.setGrafos()

    def showMap(self, vect, closedSet) -> None:
        
        plotGrid = [[[y.isEmpty * 255, y.isEmpty * 255, y.isEmpty * 255] for y in x] for x in self.grafs]
        x = []
        y = []
        x1 = []
        y2 = []
        for node in vect:
            x.append(node.y)
            y.append(node.x)
        for str in closedSet:
            x1.append(str.split(':')[0])
            y2.append(str.split(':')[1])


        print(len(closedSet))
        plt.scatter(x,y)
        # plt.scatter(x[0],y[0],color='green')
        # plt.scatter(x[-1],y[-1],color='red')
        # plt.scatter(y2,x1, color = 'orange')
        
        plt.imshow(plotGrid)
        plt.show()

    
    def setGrafos(self) -> None:
        for idx1, lst in enumerate(self.map):
            vect = []
            for idx2, isEmpty in enumerate(lst):
                vect.append(Node(idx1, idx2, isEmpty))
            self.grafs.append(vect)




        


    


                



                



        







