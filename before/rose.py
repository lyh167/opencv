import cv2
import numpy as np

print(__name__)
if __name__ != '__mian__':
    print("hello")
    rose=cv2.imread("./rose.jpeg")
    print(rose.shape) #(650, 432, 3)
    print(type(rose)) #numpy 数组
    print(rose) #三个[三维数组[彩色图片:高度、宽度、像素红绿蓝]]
    #cv2.imshow('rose', rose) #弹出窗口
    #一维:高度
    #二维:宽度
    #三维:颜色

    a = np.array([1,3,5,7])
    print(a,a[::-1], sep='\n')#数组,逆序,换行

    print(rose.dtype)
    print((rose-246).astype(np.uint8).dtype)
    # cv2.imshow((rose-256).astype(np.uint8))
    # cv2.imshow('rose', rose-246)
    # cv2.imshow('rose', rose[:,:,::-1])  # 弹出窗口
    cv2.imshow('rose', rose[:, :, [2,0,1]])  # 弹出窗口
    cv2.waitKey()
    cv2.destroyAllWindows() #消毁内存
