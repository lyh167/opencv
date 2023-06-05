import cv2
import numpy as np
if __name__== "__main__":
    yong = cv2.imread("./a3.jpg")
    dog = cv2.imread("./dog.png")

    face_detector = cv2.CascadeClassifier("./haarcascade_frontalface_alt.xml")
    yong_gray = cv2.cvtColor(yong, code=cv2.COLOR_BGR2GRAY)
    dog_gray = cv2.cvtColor(dog, code=cv2.COLOR_BGR2GRAY)

    threshold, dog_binary = cv2.threshold(dog_gray, 100,255,cv2.THRESH_OTSU)
    # threshold, binary = cv2.threshold(gray, 100, 255, cv2.THRESH_MASK)
    # threshold, binary = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
    print(threshold)
    print("================================\n")
    #OpenCV中图片图像轮廓提取-cv2.findContours()讲解
    #原因是 cv2.findContours（）的opencv返回值不一致报错，旧版本返回3个值，而新版本返回2个值，
    #contours, hierarchy = cv2.findContours(dog_binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    im, contours, hierarchy = cv2.findContours(dog_binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    areas = []
    for contour in contours:
        areas.append(cv2.contourArea(contour))
    areas=np.asarray(areas)
    index = areas.argsort()
    mask = np.zeros_like(dog_gray, dtype=np.uint8) #mask 面具
    mask = cv2.drawContours(mask, contours, index[-2], (255,255,255), thickness=-1)
    faces = face_detector.detectMultiScale(yong_gray)
    print("================================\n")
    print(faces)
    for x, y, w, h in faces:
        print(x,y,w,h)
        mask2 = cv2.resize(mask, (w, h))
        mask3 = mask2.copy()
        for i in range(h):
            for j in range(w):
                mask3[i,j] = 255 - mask2[i,j]

        dog2 = cv2.resize(dog, (w, h)) #彩色图片
        cv2.imshow("mask2", mask2)

        dog = yong[y:y+h, x:x+w]
        cv2.imshow("dog", dog)
        print("================================\n")
        print(dog)
        #dog2 = np.zeros_like(dog, dtype=np.uint8)
        print("================================\n")
        print(mask2)
        print("================================\n")

        cv2.imshow("dog2", dog2)


        face = cv2.bitwise_and(dog, dog, mask = mask3)
        face1 = cv2.bitwise_or(dog2, dog2, mask = mask2)
        face2 = cv2.bitwise_or(face, face1)
        yong[y:y+h, x:x+w] = face2

    hui = cv2.resize(yong,(400,600))
    cv2.imshow("yong", hui)
    cv2.waitKey(20000)
    cv2.destroyAllWindows()