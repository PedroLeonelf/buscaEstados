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
        
        for i in range(0, self.img.height):
            vect = []
            for j in range(0, self.img.width):
                vect.append(1) if self.pix[j,i][0] != 0 else vect.append(0)
            self.map.append(vect)

        
        # for i in range(self.img.height):
        #     vect = []
        #     for j in range(self.img.width):
        #         vect.append(Node(i,j, 1 if self.pix[j,i][0] != 0 else 0))
        #     self.grafs.append(vect)
        self.setGrafos()

    def showMap(self, vect = None, corners = None, edges = None, connect = False) -> None:
        
        plotGrid = [[[y.isEmpty * 255, y.isEmpty * 255, y.isEmpty * 255] for y in x] for x in self.grafs]
        x = []
        y = []
        
        for node in vect:
            x.append(node.y)
            y.append(node.x)




        # xCorner, yCorner = [], []
        # for corner in corners:
        #     xCorner.append(corner[1])
        #     yCorner.append(corner[0])

        # for k,v in edges.items():
        #     for dic in v:
        #         point = [k[1], int(dic.split(':')[1])]
        #         points2 = [k[0],int(dic.split(':')[0])]
        #         plt.plot(point, points2, color = 'purple')

        if connect:
            plt.plot(x,y)
        else:
            plt.scatter(x,y)
        # plt.scatter(x[0],y[0],color='green')
        # plt.scatter(x[-1],y[-1],color='red')
        # plt.scatter(xCorner, yCorner, color='brown')
        
        plt.imshow(plotGrid)

        # plt.plot([2,0],[2,3])
        # plt.plot([0,3],[2,2])


        plt.show()

    
    def setGrafos(self) -> None:
        for idx1, lst in enumerate(self.map):
            vect = []
            for idx2, isEmpty in enumerate(lst):
                vect.append(Node(idx1, idx2, isEmpty))
            self.grafs.append(vect)




        


    


                



                



        







