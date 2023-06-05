import numpy as np
import cv2

if __name__ == '__main__':
    img1=cv2.imread("./img1.png")
    hsv = cv2.cvtColor(img1, code=cv2.COLOR_BGR2HSV)


    #define range of blue color in hsv
    #lower_blue= np.array([110, 50, 50])
    #upper_blue = np.array([130, 255,255])

    # define range of blue color in green
    lower_blue = np.array([35, 43, 46])
    upper_blue = np.array([99, 255, 255])
    #根据蓝色的范围，标记图片中哪些位置是蓝色的
    #i你Range是否在这个范围内, lower~upper:蓝色
    #如果在，就是255，不然就是0
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    print(mask)

    print(mask.max(), mask.min())
    #cv2.imshow('hsv', mask)


    res = cv2.bitwise_and(img1,img1,mask=mask) #二进制运算 &
    print(res)

    #cond = res(res[::] == 0)
    #np.where((res == 0).all(axis = -1),np.array([255,255,255]).res)

    for i in range(res.shape[0]):
        for j in range(res.shape[1]):
            if (res[i,j] == 0).all():   #判断像素是黑色，都是0才是纯黑色
                res[i,j] = 255          #重新设定值，设为白色


    cv2.imshow('hsv', res)

    cv2.waitKey(0)
    cv2.destroyAllWindows()