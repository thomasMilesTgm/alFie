import RPi.GPIO as GPIO
import ControlSystems.py
import time

GPIO.setmode(GPIO.BCM)

driveMotor = Motor(27,22)
steeringServo = Servo(12)

# drive in circles for a bit
steeringServo.setAngle(20)
driveMotor.forward(100)
time.sleep(5)
driveMotor.stop()

# wiggle while they throw their hands up
for i in range (0,10,1):
    for angle in range(20, 200, 10):
        steeringServo.setAngle(angle)
        time.sleep(0.001)

# and they stay there!
driveMotor.forward(100)
for i in range (0,10,1):
    for angle in range(20, 200, 10):
        steeringServo.setAngle(angle)
        time.sleep(0.001)
driveMotor.stop()

GPIO.cleanup()
