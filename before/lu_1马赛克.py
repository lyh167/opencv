import cv2
import numpy  as np
if __name__ == "__main__":
    lu = cv2.imread("./lu.png")
    #方法一
    # print(lu.shape) #高,宽
    # img1=cv2.resize(lu,(32,51))
    # img2=cv2.resize(img1,(323,510))
    # cv2.imshow("lu",img2)

    #方法2
    # print(lu.shape) #高,宽
    # img1=cv2.resize(lu,(32,51))
    # img2=np.repeat(img1, 10, axis = 0)
    # img3=np.repeat(img2, 10, axis = 1)
    # cv2.imshow("lu",img3)

    #方法3
    print(lu.shape) #高,宽
    img1=lu[::10, ::10] #每十个取出意个像素, 细节
    cv2.namedWindow("lu", flags=cv2.WINDOW_NORMAL)
    cv2.resizeWindow("lu", 323, 510)
    # img2=np.repeat(img1, 10, axis = 0)
    # img3=np.repeat(img2, 10, axis = 1)
    cv2.imshow("lu",img1)


    cv2.waitKey(0)
    cv2.destroyAllWindows()