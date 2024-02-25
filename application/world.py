import numpy as np

class World:
    def __init__(self,width,height,nbChannel=1):
        self.world = np.zeros((width,height))
        self.world[220][220] = 1
        
    def CheckBoundaries(self):
        self.world[self.world<0] = 0
        self.world[self.world>1] = 1
        
    
        
    