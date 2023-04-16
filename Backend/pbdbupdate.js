// import library
import PocketBase from 'pocketbase';


// connect to pocketbase database with admin access
const pb = new PocketBase('http://35.247.142.180');
await pb.admins.authWithPassword('jaigaurav157@gmail.com', 'password123');


// custom sleep function
async function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}


// custum function to update Pi sensor data in database
async function update_record() {
    // get new sensor data
    const new_data_response = await fetch('http://fastapi.fishive.site/get-db-json');
    const new_data = await new_data_response.json();
    
    
    // retrieve list size
    const size = new_data["time_frame"]/new_data["time_quantum"];
    
    // get most recent record
    const tank_id = new_data["tank_id"];
    const latest_record_response = await fetch(`http://35.247.142.180/api/collections/tank_information/records?filter=(tank_id='${tank_id}')`);
    var latest_record = await latest_record_response.json();
    latest_record = latest_record["items"][0];
    
    // retrieve and update list type fields
    var temp_1 = latest_record["temp_1"];
    temp_1.unshift(new_data["temp_1"]);
    temp_1 = temp_1.slice(0, size);
    var temp_2 = latest_record["temp_2"];
    temp_2.unshift(new_data["temp_2"]);
    temp_2 = temp_2.slice(0, size);
    var timestamp = latest_record["timestamp"];
    timestamp.unshift(new_data["timestamp"]);
    timestamp = timestamp.slice(0, size);
    
    // generate updated record
    const updated_record = {
        "tank_name": new_data["tank_name"],
        "tank_id": new_data["tank_id"],
        "user_id": new_data["id"],
        "temp_1": temp_1,
        "temp_2": temp_2,
        "feederpump_status": new_data["feederpump_status"],
        "led_status": new_data["led_status"],
        "led": new_data["led"],
        "ambient_light": new_data["ambient_light"],
        "lastfeed": new_data["lastfeed"],
        "timestamp": timestamp
    }
    
    // update record in database
    const record = await pb.collection('tank_information').update(latest_record["id"], updated_record);
}


// driver code
var delay = await fetch('http://fastapi.fishive.site/get-db-json');
delay = await delay.json();
delay = await delay["time_quantum"] * 1000;

while (true) {
    await update_record();
    await console.log("Updated record!");
    await sleep(delay);

}