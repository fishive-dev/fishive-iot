import PocketBase from "pocketbase";

const pb = new PocketBase('http://35.247.142.180');

async function get_values() {
    // get tank_id
    var tank_id = await fetch('http://fastapi.fishive.site/get-db-json');
    tank_id = await tank_id.json();
    tank_id = tank_id["tank_id"];

    // get list values
    const latest_record_response = await fetch(`http://35.247.142.180/api/collections/tank_information/records?filter=(tank_id='${tank_id}')`);
    var latest_record = await latest_record_response.json();
    latest_record = latest_record["items"][0];
    const temp_1 = latest_record["temp_1"];
    const temp_2 = latest_record["temp_2"];
    var timestamp = latest_record["timestamp"];
    for (let i = 0; i < timestamp.length; i++) {
        timestamp[i] = (timestamp[i][0]*24*60*60) + (timestamp[i][1]*60*60) + (timestamp[i][2]*60) + timestamp[i][3];
    }
    return [temp_1, temp_2, timestamp];
}

const [y1, y2, x] = await get_values();
console.log(y1);
console.log(y2);
console.log(x);