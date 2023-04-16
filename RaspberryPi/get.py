'''
This custom library contains functions to simulate 
data retrieval from sensors on the Raspberry Pi
'''
import random
import time
import json
import os
import glob
import RPi.GPIO as GPIO

#GPIO Initializer Code:
GPIO.setmode(GPIO.BCM)
GPIO.setup(16,GPIO.IN) #Pin for Ldr Sensor


# set gpio pin settings so temperature sensor works
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

# retrive base directory for temperature sensor
base_therm_dir = '/sys/bus/w1/devices/'
therm_folder = glob.glob(base_therm_dir + '28*')
print(therm_folder)
therm_file1 = therm_folder[0] + '/w1_slave'
therm_file2 = therm_folder[1] + '/w1_slave'

# global variables
feed_times = [                  # fish are fed thrice a day at these specific times [Hrs,Min,Sec]
    [22,0,0], 
    [14,0,0], 
    [6,0,0]
]


'''
methods to retrieve data selectively - 
sensors only
status only
all data
'''
# Get all data in json format
def json_all():
    out = json.dumps(indent = 4, obj = {
        'temp1':temp1(),
        'temp2':temp2(),
        'light':light(),
        'cur_time':cur_time(),
        'last_feed':last_feed(),
        'filter_status':filter_status(),
        'pump_status':pump_status(),
        'light_status':light_status(),
        'rgba_val':rgba_val()
    })
    return out

# Get only sensor data in json format
def json_sensor():
    out = json.dumps(indent = 4, obj = {
        'temp1':temp1(),
        'temp2':temp2(),
        'light':light()
    })
    return out

# Get only device status in json format
def json_status():
    out = json.dumps(indent = 4, obj = {
        'filter_status':filter_status(),
        'pump_status':pump_status(),
        'light_status':light_status()
    })
    return out


'''
Display printing functions
'''


'''
Sensor data retrieval functions
'''
# Temperature sensor 1 (Celsius)
def temp1():
    with open(therm_file1, 'r') as f:
        therm_data = f.readlines()[1]                                                   # get all temperature data
        therm_data = int(therm_data.split("t=")[1].replace('\n', ''))/1000              # slice to obtain data in Celcius    
    return therm_data

# Temperature sensor 2 (Celsius)
def temp2():
    with open(therm_file2, 'r') as f:
        therm_data = f.readlines()[1]                                                   # get all temperature data
        therm_data = int(therm_data.split("t=")[1].replace('\n', ''))/1000              # slice to obtain data in Celcius
    return therm_data

# Ambient light sensor (Lumen)
def light(gpio_pin_number = 16):
    return GPIO.input(gpio_pin_number);


'''
Time retrieval functions
'''
# Current system time
def cur_time():
    t = time.localtime()
    out = [t.tm_mday, t.tm_hour, t.tm_min, t.tm_sec]
    return out

# Time since last feed
def last_feed():
    global feed_times 
    t = time.localtime()
    if t.tm_hour >= 22:
        out = [
            t.tm_hour - feed_times[0][0],
            t.tm_min - feed_times[0][1],
            t.tm_sec - feed_times[0][2]
        ]
    elif t.tm_hour >= 14:
        out = [
            t.tm_hour - feed_times[1][0],
            t.tm_min - feed_times[1][1],
            t.tm_sec - feed_times[1][2]
        ]
    elif t.tm_hour >= 6:
        out = [
            t.tm_hour - feed_times[2][0],
            t.tm_min - feed_times[2][1],
            t.tm_sec - feed_times[2][2]
        ]
    else:
        out = [
            t.tm_hour + (24 - feed_times[0][0]),
            t.tm_min + (60 - feed_times[0][1]),
            t.tm_sec + (60 - feed_times[0][2])
        ]
    return out


'''
Device status functions
'''
# Filter status (ON/OFF)
def filter_status():
    out = random.choice([0,1])
    return out

# Pump status (ON/OFF)
def pump_status():                              
    out = random.choice([0,1])
    return out

# Lights status
def light_status():
    out = random.choice([0,1])
    return out


'''
Miscellaneous functions
'''
# Light RGB color
def rgba_val():
    hex = "".join(random.choices("ABCDEF0123456789", k = 6))
    alpha = round(random.random(),2)
    out = [hex, alpha]
    return out