from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import get
import LCD
from setup import get_setup_info
import relay
import RGB

app = FastAPI()

class LCDMessage(BaseModel):
    message: str

setup_info = get_setup_info()

@app.get("/get-sensor-data")
def get_sensor_data():
    return {
        "temp1": get.temp1(),
        "temp2": get.temp2(),
        "light": get.light(16)
    }
    

@app.get("/get-db-json")
def push_to_pbdb():
    data = {
        "time_frame": setup_info["time_frame"],
        "time_quantum": setup_info["time_quantum"],
        "id": setup_info["user_id"],
        "tank_name": setup_info["tank_name"],
        "tank_id": setup_info["tank_id"],
        "temp_1": get.temp1(),
        "temp_2": get.temp2(),
        "feederpump_status": 1,
        "led_status": 0,
        "led": "255:0:0:0.6",
        "ambient_light": get.light(),
        "lastfeed": [5, 7, 0],
        "timestamp": get.cur_time()
    }
    return data
    
    
@app.post("/update-lcd")
def update_lcd(payload: LCDMessage, row: int = 0):
    LCD.clear()
    msg = payload.message
    
    # check if message can be displayed (LCD limit is 32 characters)
    if len(msg) > 32:
            return {"ERROR": "Message must be between 0-32 characters in length"}
            
    if row == 0:
        if len(msg) > 16:
            LCD.display(msg[:16], 1)
            LCD.display(msg[16:], 2)
        else:
            LCD.display(msg)
    elif row == 1:
        LCD.display(msg, 1)
    elif row == 2:
        LCD.display(msg, 2)
        
    
@app.post("/relay-state/{state}")
def relay_state(state: bool):
    relay.state_change(state)
    return {"relay": state}


@app.post("/update-rgba")
def update_rgba(r: int = 255, g: int = 255, b: int = 255, a: float = 0.5):
    RGB.set_rgba(r,g,b,a)
    return {"red": r, "green": g, "blue": b, "alpha": a}

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import get
import LCD
from setup import get_setup_info
import relay
import RGB

app = FastAPI()

class LCDMessage(BaseModel):
    message: str

setup_info = get_setup_info()

@app.get("/get-sensor-data")
def get_sensor_data():
    return {
        "temp1": get.temp1(),
        "temp2": get.temp2(),
        "light": get.light(16)
    }
    

@app.get("/get-db-json")
def push_to_pbdb():
    data = {
        "time_frame": setup_info["time_frame"],
        "time_quantum": setup_info["time_quantum"],
        "id": setup_info["user_id"],
        "tank_name": setup_info["tank_name"],
        "tank_id": setup_info["tank_id"],
        "temp_1": get.temp1(),
        "temp_2": get.temp2(),
        "feederpump_status": 1,
        "led_status": 0,
        "led": "255:0:0:0.6",
        "ambient_light": get.light(),
        "lastfeed": [5, 7, 0],
        "timestamp": get.cur_time()
    }
    return data
    
    
@app.post("/update-lcd")
def update_lcd(payload: LCDMessage, row: int = 0):
    LCD.clear()
    msg = payload.message
    
    # check if message can be displayed (LCD limit is 32 characters)
    if len(msg) > 32:
            return {"ERROR": "Message must be between 0-32 characters in length"}
            
    if row == 0:
        if len(msg) > 16:
            LCD.display(msg[:16], 1)
            LCD.display(msg[16:], 2)
        else:
            LCD.display(msg)
    elif row == 1:
        LCD.display(msg, 1)
    elif row == 2:
        LCD.display(msg, 2)
        
    
@app.post("/relay-state/{state}")
def relay_state(state: bool):
    relay.state_change(state)
    return {"relay": state}


@app.post("/update-rgba")
def update_rgba(r: int = 255, g: int = 255, b: int = 255, a: float = 0.5):
    RGB.set_rgba(r,g,b,a)
    return {"red": r, "green": g, "blue": b, "alpha": a}
    
    

# demonstration purpose get requests
@app.get("/relay-on")
def relay_on():
    relay.state_change(1)
    return {"relay": 1}
    
@app.get("/relay-off")
def relay_off():
    relay.state_change(0)
    return {"relay": 0}
    
@app.get("/led-red")
def led_red():
    RGB.set_rgba(255,0,0,0.5)
    
@app.get("/led-green")
def led_green():
    RGB.set_rgba(0,255,0,0.5)
    
@app.get("/led-blue")
def led_blue():
    RGB.set_rgba(0,0,255,0.5)
