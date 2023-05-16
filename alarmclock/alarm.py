import time
from playsound import playsound as pg
CLEAR = "\33[2J"
CLEAR_RETURN = "\33[H"

def alarm_clock(seconds):
    time_elapsed = 0
    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed +=1
        time_left = seconds- time_elapsed
        minute_left = time_left//60
        seconds_left = time_left%60
        print(f"{CLEAR_RETURN}Alarm will goes off in: {minute_left:02d}:{seconds_left:02d}")
    pg("alarm-clock-short-6402.mp3")
minutes = int(input("how  much minutes u want: "))
seconds = int(input("how much seconds u want:"))
total_time = (minutes*60) + seconds
alarm_clock(total_time)