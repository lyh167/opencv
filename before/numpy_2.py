import cv2
import numpy as np
if __name__ == "__main__":
    aa=np.array([[1,2,3],[6,7,8]])
    print(aa)
    print(np.repeat(aa,3)) #reshape
    print(np.repeat(aa, 3,axis =0))  # reshape
    print(np.repeat(aa,3,axis =1))