import cv2
import numpy as np
if __name__ == '__main__':
    a=np.array([1,2,3,4,5])
    print(a)
    b=np.array([1,4,5,7,5])
    print(b)
    c=np.bitwise_and(a,b) #&运算
    #print(bin(2),bin(4),sep = '\n')
    print(c)


    print("==============================", sep='\n')
    print("=============aa===============", sep='\n')
    aa=np.random.randint(0,10,size=(20,20,3))
    print(aa)

    print("=============bb===============", sep='\n')
    bb=np.random.randint(0,10,size=(20,20,3))
    print(bb)
    print("=============mask===============", sep='\n')
    mask= cv2.inRange(bb, np.array([2,3,5]), np.array([4,10,10]))
    print(mask.dtype, mask.shape)
    print("=============rult===============", sep='\n')
    rult=cv2.bitwise_and(aa, bb, mask = mask)
    print(rult)
    print("=============aaa===============", sep='\n')
    aaa = np.random.randint(0, 10, size=(3, 3, 3))
    print(aaa)
    print("=============bbb===============", sep='\n')
    bbb = np.random.randint(0, 10, size=(3, 3, 3))
    print(bbb)
    print("=============lu1===============", sep='\n')
    lu1 = cv2.bitwise_and(aaa, bbb)
    print(lu1)
    print("=============lu2===============", sep='\n')
    lu2 = cv2.bitwise_and(aaa,bbb, mask=np.array([[1,0,1],[1,0,0],[0,1,0]],dtype=np.uint8))
    print(lu2)