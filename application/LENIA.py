from application.world import World
from application.Channel import Channel
import matplotlib.animation as animation
import cv2
from IPython import display 
import time
import matplotlib.pyplot as plt
class LENIA:
    def __init__(self,width,height, nbChannel):
        self.world = World(height,width,nbChannel)
        self.channels = [Channel() for _ in range(nbChannel)]
        # self.history = [[plt.imshow(self.world.world*255,cmap='Greys',animated=True)]]
        self.history = [[plt.imshow(self.world.world*255,animated=True)]]
        
        
    def nextStep(self):
        for c in range(len(self.channels)):
            self.world.world[:,:,c] = self.channels[c].step(self.world.world,len(self.channels),c)
            self.world.CheckBoundaries()
            
        # self.history.append([plt.imshow(self.world.world*255,cmap='Greys',animated=True)])
        self.history.append([plt.imshow(self.world.world*255,animated=True)])

        
    def generateAnimation(self):
        fig, _ = plt.subplots()
        ani = animation.ArtistAnimation(fig, self.history, interval=50, blit=True,
                                repeat_delay=1000)
        plt.show()
        ani.save(filename="pillow_example.apng", writer="pillow")
  

