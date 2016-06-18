#!/usr/bin/python
from flask import Flask, render_template, request, url_for
from actuators import Pump, BildgePump, FlowValve
from sensors import FloatSensor, FlowMeter, TemperatureSensor
import json
import thread 
import RPi.GPIO as GPIO
from arduino_usb import monitor_pins

app = Flask(__name__)
GPIO.setmode(GPIO.BOARD)

sensors = {
  'temp_0': TemperatureSensor("A0", calib=[(612, 23.2), (953, 76.1)]),
  'temp_1': TemperatureSensor("A1", calib=[(606, 21.8), (943, 76.1)]),
  'temp_2': TemperatureSensor("A2", calib=[(605, 22.5), (946, 75.0)]),
  'temp_3': TemperatureSensor("A3", calib=[(609, 22.5), (942, 72.4)]),
  'temp_4': TemperatureSensor("A4", calib=[(608, 21.0), (970, 72.0)]),
  'temp_5': TemperatureSensor("A5", calib=[(619, 22.4), (959, 80.5)]),
}

actuators = {
  'bildge_in': BildgePump(
    name="Input Bildge",
    float_pin=29,
    pump_pin=36,
    on_when_floating=False),
  'bildge_waste': BildgePump(
    name="Waste Bildge",
    float_pin=11,
    pump_pin=38,
    on_when_floating=True),
  'wash_input': FlowValve(),
}
bildges = [actuators['bildge_in'], actuators['bildge_waste']]
valves = [actuators['wash_input']]
#bildges = [actuators['bildge_in']]


def sensor_values():
  d = {}
  names = sensors.keys()
  names.sort()
  for name in names:
    values = sensors[name].values
    d[name] = None
    if values:
      d[name] = values # sum(values)/len(values)
  return d


@app.route("/", methods=["GET", "POST"])
def home():
  s = None
  if request.method == 'POST':
    write_logs(json.dumps(request.form))	
  return render_template("home.html", stepper=s, bildges=bildges, flow_valves=valves)


@app.route('/static/<path:path>')
def static2(path):
  return send_from_directory('static', path)

@app.route('/temperature', methods=['GET'])
def tempurature():
  try:
    context = json.dumps(sensor_values())
    return context
  except Exception as e:
    print e
  return "{}"

@app.route('/actuators', methods=['GET'])
def actuators():
  try:
    context = {
      'bildges': [],
      'flow_valves': []
    }

    for bildge in bildges:
      context['bildges'].append({
        'name': bildge.name,
        'uid': bildge.uid,
        'float_state': bildge.float_state,
        'pump_state': bildge.pump_state,
      })

    for valve in valves:
      context['flow_valves'].append({
        'uid': valve.uid,
        'name': valve.name,
        'valve_setting': valve.stepper_setting,
        'flow_rate': valve.flow_rate,
      })
    return json.dumps(context)
  except Exception as e:
    print e

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
  return "thanks"

if __name__ == "__main__":
  app.run('0.0.0.0', 80)
