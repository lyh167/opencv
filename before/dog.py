import cv2
import numpy as np
if __name__ == "__main__":
    dog = cv2.imread("./dog.png")
    gray = cv2.cvtColor(dog, cv2.COLOR_BGR2GRAY)
    gray2= cv2.GaussianBlur(gray,(5,5),0)
    canny = cv2.Canny(gray2,150,200)

    cv2.imshow("dog",gray)
    cv2.imshow("dog2", gray2)
    cv2.imshow("canny", canny)
    cv2.waitKey(5000)
    cv2.destroyAllWindows()