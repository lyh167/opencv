import cv2
import numpy as np

if __name__ == "__main__":
    lu = cv2.imread("./hui.jpg")
    gray =cv2.cvtColor(lu,code=cv2.COLOR_BGR2GRAY)
    #人脸特征的详细说明，1万多行
    face_detector = cv2.CascadeClassifier("./haarcascade_frontalface_alt.xml")
    #faces = face_detector.detectMultiScale(lu)#坐标x,y,w,h

    faces = face_detector.detectMultiScale(gray,
                                           scaleFactor =1.3, #缩放
                                           minNeighbors=3,  # 坐标x,y,w,h
                                           minSize=(60,60))


    print(faces)

    for x, y, w, h in faces:
        cv2.rectangle(lu,
                      pt1=(x,y),
                      pt2=(x + w, y + h),
                      color = [0,0,255],
                      thickness = 2)

        #cv2.circle(lu, center=(x+w//2, y+h//2), radius=w//2, color=[0,255,0])
    cv2.imshow("lu",lu)
    cv2.waitKey(5000)
    cv2.destroyAllWimdows()