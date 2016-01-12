#!/usr/bin/python

import serial
import time
import thread


def monitor_pins(callback_func):
  ser = serial.Serial('/dev/ttyACM0', 9600)
  while True:
    try:
      s = ser.readline().rstrip("\n")
      if ":" in s:
        (pin, val) = s.split(":")
        val = int(val)
        callback_func(pin, val)
    except Exception as e:
      print e


if __name__ == "__main__":
  def callback(pin, val):
    print "pin:%s, val:%s" % (pin, val)
  thread.start_new_thread(monitor_pins, (callback,))
  while 1:
    time.sleep(1000)


