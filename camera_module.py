import picamera
#from time import sleep
import datetime as dt

camera = picamera.PiCamera()
camera.rotation = 270
camera.resolution = (1920, 1080)
camera.framerate = 25
camera.annotate_text_size = 15
camera.annotate_background = picamera.Color('black')

#video preview
camera.start_preview(alpha = 220)
#sleep(5)
#camera.stop_preview()
   
#video recording
def doorbell_clip():
    camera.start_recording('/home/pi/Documents/%s.h264' % dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    start = dt.datetime.now()
    while (dt.datetime.now() - start).seconds < 30:
        camera.annotate_text = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        camera.wait_recording(0.2)
        #sleep(10)
    camera.stop_recording()
    