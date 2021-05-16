from machine import Pin
from time import sleep

internal_led = Pin(25, Pin.OUT)
while True:
    internal_led.toggle()
    sleep(0.5)