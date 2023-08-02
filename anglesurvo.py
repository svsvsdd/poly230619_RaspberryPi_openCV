from gpiozero import AngularServo
from time import sleep

servo = AngularServo(17, min_angle=0, max_angle=430)

while True:
    servo.angle(0)
    sleep(2)
    servo.angle(40)
    sleep(2)
    servo.angle(90)
    sleep(2)
    
cv2.waitKey(0)    
cv2.destroyAllWindows()    