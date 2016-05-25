import pprint 
import json
filename = "static/temp_logs.txt"

keys = ["temp_0", "temp_1", "temp_2", "temp_3", "temp_4", "temp_5"]
mins = {}
maxs = {}

def raw_values():
  f = open(filename)
  for line in f.readlines():
    data = json.loads(line)
    clean_values = []
    for key in data.keys():
      val = data[key]
      if val != None and key in keys:
        val = sum(val)/len(val)

        # default values
        if key not in mins:
          mins[key] = 10000
        if key not in maxs:
          maxs[key] = 0

        mins[key] = min(mins[key], val)
        maxs[key] = max(maxs[key], val)

  print "MINIMUMS"
  pprint.pprint(mins)

  print "\n\nMAXIMUMS"
  pprint.pprint(maxs)

def observations():
  f = open(filename)
  for line in f.readlines():
    data = json.loads(line)
    if len(data.keys()) == 2:
      print data

raw_values()
observations()
