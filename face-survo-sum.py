import numpy as np
import cv2
from gpiozero import AngularServo
from time import sleep

# 서브모터 제어 함수
def control_submotor(angle):
    # 서브모터를 해당 각도로 제어하는 코드 작성
    servo.angle = angle
    

servo = AngularServo(17, min_angle=-90, max_angle=90)

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 400)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 400)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    height, width = frame.shape[:2]
    center_x = width // 2  # 화면 중심 x 좌표

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        # 얼굴의 중심 x 좌표 계산
        face_center_x = x + (w // 2)

        # 화면 중심과 얼굴 중심의 차이 계산
        diff_x = face_center_x - center_x
        threshold = 50
        calculate_angle = (180*threshold //(width / 2))
        
        
        # 일정 범위 이상 벗어난 경우 서브모터 제어
        if abs(diff_x) > threshold:    #50픽셀
            angle = calculate_angle(diff_x)  # 각도 계산 함수 호출
            control_submotor(angle)  # 서브모터 제어 함수 호출
            
        
        img = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)   
        

    cv2.imshow('Detect',frame)
    if cv2.waitKey(1) == 27:
        break
    
cap.release()
cv2.destroyAllWindows()

