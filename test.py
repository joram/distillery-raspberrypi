import RPi.GPIO as GPIO
from actuators import BildgePump
import time


if __name__ == "__main__":
  GPIO.setmode(GPIO.BOARD)
  bildge_in = BildgePump(float_pin=29, pump_pin=36)
  bildge_waste = BildgePump(float_pin=13, pump_pin=38)
  while True:
    time.sleep(10)
