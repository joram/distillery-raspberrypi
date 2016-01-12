#!/usr/bin/python
from flask import Flask, render_template, request
from stepper import Stepper
import json
import thread 
from arduino_usb import monitor_pins

app = Flask(__name__)
s = Stepper()
pin_values = {}


def pin_value_callback(pin, value):
  pin_values[pin] = value


@app.route("/")
def home():
    return render_template("home.html", stepper=s)


@app.route('/static/<path:path>')
def static2(path):
    return send_from_directory('static', path)


@app.route('/temperature', methods=['GET'])
def tempurature():
    return json.dumps(pin_values)


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
  thread.start_new_thread(monitor_pins, (pin_value_callback,))
  app.run('0.0.0.0')
