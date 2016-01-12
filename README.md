# distillery
<p>
It's intent is to have a continuous running distillation process with 6 temperature sensors along the fractionating column, two servo controlled valves, one for liquid input (wash), and one for the desired collected liquid's output valve. It will also have 2 pumps, one continuously running for the wash input, while the other will be turned on periodically as a bildge system to remove the undesired waste liquid.
</p>
<p>
The distillery code is split up into several repos:
</p>
* <a href="https://github.com/joram/distillery-raspberrypi">raspberrypi</a>
* <a href="https://github.com/joram/distillery-arduino">arduino</a>
* <a href="https://github.com/joram/distillery-parts">parts (physical 3D parts)</a>

## arduino
<p>
The arduino continuously polls the 6 temperature sensors, and stores the last 100 raw values. It will provide the raw data as json over serial when it receives the command `values`. It will provide the average values with the command `averages`.
</p>

## raspberrypi
<p>
The raspberrypi provides a web interface to monitor the sensors and control the actuators. While it plugged in to the arduino it gets the temperature values from it over the serial connection.
</p>

## parts
<p>
The physical parts to be 3D printed for the nema17 stepper motors to connect to the needle valves.
</p>