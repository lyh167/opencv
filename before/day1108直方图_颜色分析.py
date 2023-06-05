import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import data

if __name__ == "__main__":
    moon = data.moon()
    print(moon)
    print(moon.shape)
    hist = cv2.calcHist(moon, [0], None, [256], [0, 256])
    print(hist)
    print(hist.shape)
    #plt.plot(hist)

    plt.bar(x=np.arange(0,256), height=hist.reshape(-1))
    plt.show()

    # plt.hist(moon.ravel(), bins=256)
    # plt.show()
    #
    #直方图均衡化，可以将图片的明暗对比增强
    # moon2 = cv2.equalizeHist(moon)
    # plt.hist(moon2.reshape(-1), bins =256)
    # plt.show()

    cv2.imshow("moon", moon)
    cv2.waitKey(5000)
    cv2.destroyAllWindows()