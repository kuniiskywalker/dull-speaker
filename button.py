import RPi.GPIO as GPIO
import time
import jtalk 
import speech 

GPIO_BTN=14

def btn_callback(gpio_no):
	# speech.run()
	jtalk.run('たまき')
	print(gpio_no)

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_BTN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(GPIO_BTN, GPIO.FALLING, bouncetime=300)
GPIO.add_event_callback(GPIO_BTN, btn_callback)

try:
	while True:
		time.sleep(1.5)
except KeyboardInterrupt:
	GPIO.cleanup()
