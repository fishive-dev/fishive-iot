def get_setup_info():
    with open("setup.txt", "r") as file:
        file_data = file.readlines()
        user_id = file_data[1].replace("\n", "").strip().split("=")[1].strip()
        tank_id = file_data[2].replace("\n", "").strip().split("=")[1].strip()
        tank_name = file_data[3].replace("\n", "").strip().split("=")[1].strip()
        time_frame = int(file_data[4].replace("\n", "").strip().split("=")[1].strip())
        time_quantum = int(file_data[5].replace("\n", "").strip().split("=")[1].strip())
        
        setup_info = {
            "user_id":user_id,
            "tank_id":tank_id,
            "tank_name":tank_name,
            "time_frame":time_frame,
            "time_quantum":time_quantum
        }
        
        return setup_info
        
print(get_setup_info())