import cv2
import numpy as np
from scipy import signal
from sklearn import preprocessing as p 

class Channel:
    def __init__(self):
        self.filtre = cv2.imread('Template/Filtre/filtre3.png',1)
        self.filtre = cv2.resize(self.filtre,(20,20))
        self.filtre = self.filtre/255
        self.growthFuction = self.defaultGrowFunction
        
    def conv2D(self,world,channelId):
        return signal.convolve2d(world,self.filtre[:,:,channelId],boundary='symm',mode='same')
        
    def step(self,world,nbChannel,channelId):
        resConvTotal = []
        for c in range(nbChannel):
            resConv = self.conv2D(world[:,:,c],c)
            if c == 0:
                resConvTotal = resConv
            else:
                resConvTotal+=resConv
        min_max_scaler = p.MinMaxScaler() 
        resConvTotal = min_max_scaler.fit_transform(resConvTotal)
        resConvTotal = resConvTotal*5 
        return world[:,:,channelId] + self.defaultGrowFunction(resConvTotal)
    
    def defaultGrowFunction(self,x):
         return np.exp(-(((x-2.5)/1)**2)/2)*2-1