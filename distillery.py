#!/usr/bin/python
from flask import Flask, render_template, request
from stepper import Stepper
from sensor.float import FloatSensor
from sensor.temperature import TemperatureSensorController, TemperatureSensor
import json
import thread 
import RPi.GPIO as GPIO
from arduino_usb import monitor_pins

app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
controller = TemperatureSensorController()

sensors = {
  'float_0': FloatSensor(pin=20, name="float0"),
  'float_1': FloatSensor(pin=21, name="float1"),
  'temp_0': TemperatureSensor(controller, "A0"),
  'temp_1': TemperatureSensor(controller, "A1"),
  'temp_2': TemperatureSensor(controller, "A2"),
  'temp_3': TemperatureSensor(controller, "A3"),
  'temp_4': TemperatureSensor(controller, "A4"),
  'temp_5': TemperatureSensor(controller, "A5"),
}

def sensor_values():
  d = {}
  names = sensors.keys()
  names.sort()
  for name in names:
    d[name] = sensors[name].values
  return d


@app.route("/")
def home():
  s = None
  return render_template("home.html", stepper=s)


@app.route('/static/<path:path>')
def static2(path):
    return send_from_directory('static', path)


@app.route('/temperature', methods=['GET'])
def tempurature():
    return json.dumps(sensor_values())


@app.route('/stepper', methods=['POST'])
def stepper():
	try:
		name = request.form.get('name')
		value = request.form.get('value')

		if name == "stepper_frequency":
			s.set_speed(int(value))

		if name == "stepper_direction":
			if value in ["1", "2"]:
				direction = {'1': True, '2': False}[value]
				s.set_direction(direction)


	except Exception as e:
		print e
		pass
	return "thanks"

if __name__ == "__main__":
  app.run('0.0.0.0', 80)
