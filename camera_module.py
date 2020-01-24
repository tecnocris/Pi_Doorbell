import picamera
import datetime as dt

# Create camera object
camera = picamera.PiCamera()
# Camera settings
camera.rotation = 270
camera.resolution = (1920, 1080)
camera.framerate = 25
# Output text overlay for date/time stamp
camera.annotate_text_size = 30
camera.annotate_background = picamera.Color('black')

#video preview
camera.start_preview(alpha = 220)
#camera.stop_preview()
   
#video recording
def doorbell_clip():
    camera.start_recording('/home/pi/Desktop/Video/%s.h264' % dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    start = dt.datetime.now()
    # Numerical value on line below determines recording time
    while (dt.datetime.now() - start).seconds < 10:
        camera.annotate_text = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        camera.wait_recording(0.2)
    camera.stop_recording()
    
