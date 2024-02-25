import cv2
import numpy as np
from scipy import signal

class Channel:
    def __init__(self):
        self.filtre = cv2.imread('Template/Filtre/filtre1.png', 0)
        self.growthFuction = self.defaultGrowFunction
        
    def conv2D(self,world):
        return signal.convolve2d(world,self.filtre,boundary='symm',mode='same')
        
    def step(self,world):
        resConv = self.conv2D(world)
        return world + self.defaultGrowFunction(resConv)
    
    def defaultGrowFunction(self,x):
         return np.exp(-(((x-2.5)/1)**2)/2)*2-1