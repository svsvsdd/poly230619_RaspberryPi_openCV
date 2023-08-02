from gpiozero import Servo
from time import sleep

servo = Servo(17)

while True:
    servo.value = -1.0
    sleep(2)
    servo.value = 0.0
    sleep(2)
    servo.value = 1.0
    sleep(2)


cv2.waitKey(0)    
cv2.destroyAllWindows()    