#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT
 
import time
import atexit
#!/usr/bin/python
import time
import RPi.GPIO as GPIO


class Stepper(object):

	def __init__(self, mhat,  motor_id=1):
		self.mhat = mhat
		self.motor_id = motor_id
		self.direction = True
		self._stepper = self.mhat.getStepper(200, self.motor_id)
		atexit.register(self.turnOffMotors)


	def set_speed(self, rpm):
		self._stepper.setSpeed(rpm)
		while (True):
			print("Single coil steps")

			direction = Adafruit_MotorHAT.FORWARD if self.direction else Adafruit_MotorHAT.BACKWARD
			self._stepper.step(1000, direction, Adafruit_MotorHAT.INTERLEAVE)

	def set_direction(self, direction):
		self.direction = direction
		GPIO.output(self.dir_pin, 1 if direction else 0)

	def turnOffMotors():
        	mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
        	mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
        	mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
        	mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

if __name__ == "__main__":
  GPIO.setmode(GPIO.BOARD)
  motor_hat = Adafruit_MotorHAT(addr = 0x60)
  stepper = Stepper(motor_hat)
  stepper.set_speed(30)
  time.sleep(30)
