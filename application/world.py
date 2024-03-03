import numpy as np
import cv2

class World:
    def __init__(self,width,height,nbChannel=1):
        # self.world = np.random.random((width,height,nbChannel))
        self.world = np.random.randn(width,height,nbChannel)
        # self.world = cv2.imread('Template/World/worldTemplate5.png')
        # self.world = cv2.resize(self.world,(width,height))
        
    def CheckBoundaries(self):
        self.world[self.world<0] = 0
        self.world[self.world>1] = 1
        
    
        
    