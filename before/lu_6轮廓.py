import cv2
import numpy as np

if __name__ == "__main__":
    img = cv2.imread("./rose.jpeg")
    hsv = cv2.cvtColor(img, code=cv2.COLOR_BGR2HSV)
    #轮廓查找, 通过颜色
    # lower_red = (156,50,50) #浅红色
    # upper_red = (180,255,255)#深红色
    # mask = cv2.inRange(hsv, lower_red, upper_red)

    #轮廓查找, 通过手工绘制
    h,w,c = img.shape
    mask = np.zeros((h,w), dtype=np.uint8)
    x_data=np.array([56, 90, 93, 105, 130, 131,
                     137, 135, 137, 153, 164, 234,
                     234, 225, 223, 244, 255, 282,
                     322, 341, 372, 348, 347, 357, 348,
                     323, 314, 281, 285, 172, 121,
                     103, 92, 85, 66, 76, 75,
                     76, 58])
    y_data=np.array([352, 402, 415, 425, 461, 492,
                     507, 516, 540, 543, 536, 509,
                     487, 471, 463, 462, 467, 444,
                     446, 411, 291, 278, 269, 236, 232,
                     254, 232, 192, 186, 196, 216,
                     239, 238, 250, 274, 298, 327,
                     338, 351])
    pts=np.c_[x_data, y_data] #横纵坐标合并, 点(x,y)
    #pts = np.vstack((x_data, y_data)).astype(np.uint8).T
    print(pts)
    cv2.fillPoly(mask, [pts], (255), 8, 0)
    res=cv2.bitwise_and(img, img, mask=mask)
    cv2.imshow("flower",res)
    cv2.waitKey(5000)
    cv2.destroyAllWindows()