import camera_module
from gpiozero import MotionSensor, Button, LED
from time import sleep


# Create object for button
# Button is on GPIO-2 (Pin 3)
button = Button(2)
# Create object for led
# LED is on GPIO-3 (Pin 5)
led = LED(3)
# Create object for PIR Sensor
#PIR Sensor is on GPIO-4 (Pin 7)
pir = MotionSensor(4)

while True:
    if button.is_pressed:
        print("button pressed")
        led.on()
        sleep(1)
        led.off()
        camera_module.doorbell_clip()
    elif pir.motion_detected == True:
        print("Heat Detected")
        led.on()
        sleep(1)
        led.off()
        camera_module.doorbell_clip()
