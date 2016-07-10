import RPi.GPIO as GPIO
from actuators import FlowValve
import time


if __name__ == "__main__":
  GPIO.setmode(GPIO.BOARD)
  fm = FlowValve()
  fm.calibrate()
  while True:
    time.sleep(10)
