from threading import Thread
from application.LENIA import LENIA
import cv2
import numpy as np
import sys
import time
from application.app import app

def cli():
    np.set_printoptions(threshold=sys.maxsize)
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

def start_flask():
    app.run(debug=True)

if __name__ == '__main__':
    flask_thread = Thread(target=start_flask)
    flask_thread.start()

    time.sleep(2) 
    cli()