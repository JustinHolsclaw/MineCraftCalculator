#Simulation of a rocket launch just for fun
import time

def Launch_Countdown(length_of_countdown):
    while(length_of_countdown != 0):
        print (length_of_countdown)
        time.sleep(1)
        length_of_countdown-=1
    print("LIFT OFF")

def Assemble_Rocket():
    current_Configuration = {
        "Propulsion_System": "unknown",
        "Payload_System": "unknown",
        "Structure_System": "unknown",
        "Guidance_System": "unknown"
    }

    

