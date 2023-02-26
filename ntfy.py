import time
import subprocess
from functions import mainFunc

last_time = ''
last_day = ''
i = 0

while True:
    current_time = time.strftime("%H:%M")
    current_day = time.strftime("%A")
    courses_list, times_list, notifications_list = mainFunc(current_day)
    print(current_time)
    if current_time == notifications_list[i]:
        if current_time != last_time:
            message = f"{times_list} {courses_list[i]}"
            topic = "ntfy.sh/lextest"
            ntfy = ['curl', '-d', message, topic]
            subprocess.run(ntfy)
            last_time = current_time
            last_day = current_day
            if i < len(courses_list):
                i += 1
            if current_day != last_day:
                i = 0
