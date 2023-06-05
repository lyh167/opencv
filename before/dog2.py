# import cv2
# import numpy as np
# if __name__ == "__main__":
#     dog = cv2.imread("./dog.png")
#     gray = cv2.cvtColor(dog, cv2.COLOR_BGR2GRAY)
#
#     img, contours = cv2.findContours(gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#     print(img, contours)
#     # img2 = cv2.drawContours(img, contours, 3, (0, 255, 0), 3)
#     cv2.imshow('imageshow', img)
#     # cv2.imshow("img2", img2)
#     cv2.waitKey(5000)
#     cv2.destroyAllWindows()

import cv2
import numpy as np

img = cv2.imread('./dog.png')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
image, contours = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.imshow('imageshow', image)  # 显示返回值image，其实与输入参数的thresh原图没啥区别
cv2.waitKey(0)

# img = cv2.drawContours(img, contours, -1, (0, 255, 0), 5)  # img为三通道才能显示轮廓
# cv2.imshow('drawimg', img)
# cv2.waitKey(0)
cv2.destroyAllWindows()