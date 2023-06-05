import cv2
import numpy as np
if __name__== "__main__":
    yong = cv2.imread("./yong.jpg")
    dog = cv2.imread("./dog.png")

    face_detector = cv2.CascadeClassifier("./haarcascade_frontalface_alt.xml")
    yong_gray = cv2.cvtColor(yong, code=cv2.COLOR_BGR2GRAY)
    dog_gray = cv2.cvtColor(dog, code=cv2.COLOR_BGR2GRAY)

    threshold, dog_binary = cv2.threshold(dog_gray, 100,255,cv2.THRESH_OTSU)
    # threshold, binary = cv2.threshold(gray, 100, 255, cv2.THRESH_MASK)
    # threshold, binary = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
    print(threshold)

    # contours, hierarchy = cv2.findContours(dog_binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    im, contours, hierarchy = cv2.findContours(dog_binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    areas = []
    for contour in contours:
        areas.append(cv2.contourArea(contour))
    areas=np.asarray(areas)
    index = areas.argsort()
    mask = np.zeros_like(dog_gray, dtype=np.uint8) #mask 面具
    mask = cv2.drawContours(mask, contours, index[-2], (255,255,255), thickness=-1)

    faces = face_detector.detectMultiScale(yong_gray)
    for x, y, w, h in faces:
        mask2 = cv2.resize(mask, (w, h))
        dog2 = cv2.resize(dog, (w, h))
        cv2.imshow("dog2", dog2)
        for i in range(h):
            for j in range(w):
                if(mask2[i, j] == 255).all():
                    yong[i+y, j+x] = dog2[i, j]

    cv2.imshow("yong", yong)
    cv2.waitKey(5000)
    cv2.destroyAllWindows()