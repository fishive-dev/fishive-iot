from time import sleep
import LCD
import get

while True:
    sensor_data = [get.temp1(), get.temp2(), get.light(16)]
    LCD.display("Temp 1: " + str(round(sensor_data[0])), 1)
    LCD.display("LDR: " + str(sensor_data[2]) + " Temp 2:" + str(round(sensor_data[1])), 2)
    
