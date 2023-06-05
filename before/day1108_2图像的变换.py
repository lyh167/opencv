import numpy as np
import cv2
from matplotlib import pyplot as plt
#傅里叶变换经常被用来分析不同滤波器的频率特性，我们可以用2D离散傅里叶变换(DFT)分析图像的频域特性，实现DFT的一个快速算法被称为快速傅里叶变换(FFT)
if __name__ == "__main__":
    yong = cv2.imread("./hui.jpg")
    img = cv2.cvtColor(yong, code=cv2.COLOR_BGR2GRAY)

    # 进行傅里叶变换(由时域到频域)
    f=np.fft.fft2(img)

    #将频率是0的数据到屏幕中心
    fshift=np.fft.fftshift(f)
    #对数运算，大幅缩小数据
    magnitude_spectrum = 20*np.log(np.abs(fshift))

    #振幅谱图
    plt.subplot(121),plt.imshow(img,cmap = "gray")
    plt.title('Input Image'), plt.xticks([]),plt.yticks([])
    plt.subplot(122),plt.imshow(magnitude_spectrum, cmap ="gray")
    plt.title("Magnitude Spectrum"), plt.xticks([]), plt.yticks([])
    plt.show()
