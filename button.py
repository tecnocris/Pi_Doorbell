import camera_module
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
ledPin = 12
buttonPin = 16
GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)


while True:
    buttonState = GPIO.input(buttonPin)
    if buttonState == False:
        GPIO.output(ledPin, GPIO.HIGH)
        camera_module.doorbell_clip()
        #print("it's alive")
    else:
        GPIO.output(ledPin, GPIO.LOW)
        #print("she's dead, jim")
        


