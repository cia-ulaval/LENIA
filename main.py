from application.LENIA import LENIA
import cv2
import numpy as np
import sys
import time


def cli():
    np.set_printoptions(threshold=sys.maxsize)
    print('start server !! Youpi !')
    l = LENIA(640,480,3)
    looping = True
    nbStep = 60
    i=0
    while i<nbStep:
        print(round(i/nbStep,2))
        # l.showSimulation()
        l.nextStep()
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            looping = False
            cv2.destroyAllWindows()
        i+=1
    l.generateAnimation()

if __name__ == '__main__':
    cli()