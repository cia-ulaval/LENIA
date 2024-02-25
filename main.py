from application.LENIA import LENIA
import cv2

def cli():
    print('start server !! Youpi !')
    l = LENIA(640,480,1)
    looping = True
    while looping:
        l.nextStep()
        l.showSimulation()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            looping = False
            cv2.destroyAllWindows()


if __name__ == '__main__':
    cli()