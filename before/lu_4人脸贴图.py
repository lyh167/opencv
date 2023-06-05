import numpy as np
import cv2
if __name__ == "__main__":
    img = cv2.imread("./hui.jpg")
    gray = cv2.cvtColor(img, code = cv2.COLOR_BGR2GRAY)
    face_detector = cv2.CascadeClassifier("./haarcascade_frontalface_alt.xml")
    faces = face_detector.detectMultiScale(gray)
    star = cv2.imread('./star.png')
    for x, y, w, h in faces:
        #cv2.rectangle(img, pt1=(x,y), pt2=(x+w,y+h),color=[0,0,255],thickness = 2) #划红线
        #d=3*w//8+3*w%8//2
        #img[y:y+h//4,x+d:x+w//4+d] = cv2.resize(star,(w // 4,h // 4))

        d = 3 * w // 8 + 3 * w % 8 // 2
        star_s = cv2.resize(star,(w//4, h//4))
        w1 = w//4
        h1 = h//4
        for i in range(h1):
            for j in range(w1):
                if not(star_s[i, j] > 240).all(): #非白色
                    img[i+y,j+x+d] = star_s[i,j]
    cv2.imshow('face', img)
    cv2.waitKey(5000)
    cv2.destroyAllWindows()
