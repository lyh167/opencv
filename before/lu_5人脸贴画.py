import numpy as np
import cv2
if __name__ == "__main__":
    img = cv2.imread("./yong.jpg")
    gray = cv2.cvtColor(img, code=cv2.COLOR_BGR2GRAY)
    face_detector = cv2.CascadeClassifier("./haarcascade_frontalface_alt.xml")
    faces=face_detector.detectMultiScale(gray)
    head=cv2.imread("./dog.png")
    for x, y, w, h in faces:
        head2 = cv2.resize(head,(w,h))
        for i in range(h):
            for j in range(w):
                if not (head2[i, j] > 220).all():  # 非白色
                    img[i+y,j+x]=head2[i,j]
    cv2.imshow("head", img)
    cv2.waitKey(5000)
    cv2.destroyAllWindows()