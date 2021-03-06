#!/usr/bin/env python
# -*- coding: utf-8 -*-  

HOST = "localhost"
PORT = 4223
UID_DC = "9yEBJP3Jnf3" # Change to the UID of your DC Brick
UID_POTI = "2wx" # Change to the UID of your Rotary Poti Bricklet

from tinkerforge.ip_connection import IPConnection
from tinkerforge.brick_dc import DC
from tinkerforge.bricklet_rotary_poti import RotaryPoti

dc = None

# Callback function for position callback (parameter has range -150 to 150)
def cb_position(position):
    velocity = 0xFFFF/2*position/150 # Velocity: -32767/32767
    print('Set Position/Velocity: ' + str(position) + '/' + str(velocity))
    dc.set_velocity(velocity)

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection

    dc = DC(UID_DC, ipcon) # Create DC brick device object
    poti = RotaryPoti(UID_POTI, ipcon) # Create rotary poti device object

    ipcon.connect(HOST, PORT) # Connect to brickd

    poti.set_position_callback_period(50) # set callback period to 50ms
    poti.register_callback(poti.CALLBACK_POSITION, cb_position)

    dc.enable()
    dc.set_acceleration(0xFFFF) # Full acceleration

    raw_input('Press Enter to exit\n') # Use input() in Python 3
    dc.disable()
    ipcon.disconnect()
