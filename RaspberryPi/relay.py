import RPi.GPIO as GPIO

pump_GPIO = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(pump_GPIO, GPIO.OUT)
GPIO.output(pump_GPIO, GPIO.HIGH)
    
def state_change(state):
    GPIO.output(pump_GPIO, state)