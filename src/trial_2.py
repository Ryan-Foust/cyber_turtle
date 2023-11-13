#!/usr/bin/python3
import datetime
import time

target_time = datetime.time(18, 50)
while True:
    current_time = datetime.datetime.now().time()
    print(current_time)
    if current_time == target_time:
        print("time achieved")
        break
    time.sleep(15)
