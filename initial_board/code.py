"""
This demo code for Adafruit's CircuitPlayground Express (CPX) is
compatible with the Device Simulator Express Visual Studio Code extension.

The extension allows you to code CircuitPython for your
CircuitPlayground Express (CPX) by testing and debugging on
the device simulator, before running your code on the actual
device. The serial monitor easily allows you to
observe device output.

Download the extension here:
https://marketplace.visualstudio.com/items?itemName=ms-python.devicesimulatorexpress

To view printed output when the device is running,
use the the following command in Visual Studio Code:
"Device Simulator Express: Open Serial Monitor"

Copyright (c) 2019 Microsoft
"""

import random
import time

from adafruit_circuitplayground.express import cpx

# Set this to False to turn on off the capacitive touch tones
TOUCH_PIANO = True

# NeoPixel color names
WHITE = (50, 50, 50)
DARK_ORANGE = (80, 44, 0)
ORANGE = (244, 117, 33)
YELLOW_ORANGE = (216, 59, 1)
BLACK = (0, 0, 0)

# Dim the lights a bit, they're bright
cpx.pixels.brightness = 0.3

# SPEAKER - Play startup noise on boot
cpx.play_file("Fanfare.wav")


def wheel(position):
    # Return color value for position
    if position < 0 or position > 255:
        return BLACK
    if position < 85:
        return ORANGE
    elif position < 170:
        position -= 85
        return YELLOW_ORANGE
    else:
        position -= 170
    return WHITE


lights_on = True  # Lights on or off
led_on = False  # LED on or off
current_pixel = 0  # Counter for all 10 pixels
last_switch = cpx.switch  # Last position of the switch

while True:
    # LIGHTS - This  makes a swirling pattern of orange colors!
    if lights_on:
        for pixel_pos in range(10):
            color = wheel(25 * ((current_pixel + pixel_pos) % 10))
            cpx.pixels[pixel_pos] = [int(c * ((10 - (current_pixel + pixel_pos) % 10)) / 10.0) for c in color]

        # Each time around we tick off one pixel at a time
        if cpx.switch:  # depending on the switch we'll go clockwise
            current_pixel += 1
            if current_pixel > 9:
                current_pixel = 0
        else:  # or counter clockwise, flip the switch to change direction
            current_pixel -= 1
            if current_pixel < 0:
                current_pixel = 9

        # BUTTONS - Press and hold to make the lights temporarily dimmer or brighter
        if cpx.button_a:
            print("Button A pressed - make lights dimmer")
            cpx.pixels.brightness = 0.1
        if cpx.button_b:
            print("Button B pressed - make lights brighter")
            cpx.pixels.brightness = 0.5
        if not cpx.button_a and not cpx.button_b:
            # Go back to default brightness if neither button is pressed
            cpx.pixels.brightness = 0.3

    # SWITCH - Check the switch
    if cpx.switch:
        if last_switch != cpx.switch:
            print("Switch moved left")
    else:
        if last_switch != cpx.switch:
            print("Switch moved right")
    last_switch = cpx.switch

    # CAPACITIVE TOUCH - Touch A1 - A7 on the device to play music
    if TOUCH_PIANO:
        if cpx.touch_A4:
            cpx.play_tone(524, 0.25)
        elif cpx.touch_A5:
            cpx.play_tone(588, 0.25)
        elif cpx.touch_A6:
            cpx.play_tone(660, 0.25)
        elif cpx.touch_A7:
            cpx.play_tone(698, 0.25)
        elif cpx.touch_A1:
            cpx.play_tone(784, 0.25)
        elif cpx.touch_A2:
            cpx.play_tone(880, 0.25)
        elif cpx.touch_A3:
            cpx.play_tone(988, 0.25)

    # SENSORS - Print sensor data every time the lights go around
    if current_pixel == 0:
        x, y, z = cpx.acceleration
        print("Temperature: %0.1f *C" % cpx.temperature)
        print("Light Level: %d" % cpx.light)
        print("Accelerometer: (%0.1f, %0.1f, %0.1f) m/s^2" % (x, y, z))
        print("-" * 40)

    # SHAKE - Look for a shake with the given threshold
    if cpx.shake(shake_threshold=20):
        # Turn off lights and pause sensor reporting
        cpx.pixels.fill(BLACK)

        # Switch the neopixels on and off
        lights_on = not lights_on

        # Switch the red LED on and off
        led_on = not led_on
        time.sleep(0.02)

    # LED - Turns on and off the little LED next to USB on
    cpx.red_led = led_on

    # Go back to the beginning of the while True loop!