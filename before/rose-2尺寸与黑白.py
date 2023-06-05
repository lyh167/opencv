import numpy as np
import cv2

if __name__=='__main__':
    rose=cv2.imread("./rose.jpeg")

    rose2 = cv2.resize(rose, (305,305))

    gray = cv2.cvtColor(rose, code = cv2.COLOR_BGR2GRAY)

    #H:(色彩/色度) [0, 179]
    #S:(饱和度) [0,255]
    #V:(亮度) [0, 255]
    hsv = cv2.cvtColor(rose, code = cv2.COLOR_BGR2HSV)

    cv2.imshow('rose', hsv)
    cv2.waitKey(5000)
    cv2.destroyAllWindows()