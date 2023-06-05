import cv2
import numpy as np
if __name__ != "__mian__":
    lu = cv2.imread('./lu.png')
    #cv2.imshow('lu',lu)
    #[111,137] [167,197]
    #切片获取人脸
    face = lu[137:197, 111:167]
    #cv2.imshow('face', face)

    face = face[::5, ::5]
    face = np.repeat(face,5,axis = 0)
    face = np.repeat(face, 5, axis=1)
    lu[137:197, 111:167] = face[:60, :56] #填充，尺寸一致
    #lu[137:197, 111:167] = face[:,:,::-1]
    cv2.imshow('lu',lu)
    cv2.waitKey(0)
    cv2.destroyAllWindows()