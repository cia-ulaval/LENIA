from application.world import World
from application.Channel import Channel
import cv2

class LENIA:
    def __init__(self,width,height, nbChannel):
        self.world = World(width,height,nbChannel)
        self.channels = [Channel() for _ in range(nbChannel)]
        
        
    def nextStep(self):
        print('new step')
        self.world.world = self.channels[0].step(self.world.world)
        self.world.CheckBoundaries()
        print(self.world.world)
        
    def showSimulation(self):
        cv2.imshow('simulation', self.world.world) 