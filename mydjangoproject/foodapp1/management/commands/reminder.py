from foodapp1.management.commands.bot import remind
import datetime
import time

while True:
    now_time = datetime.datetime.now().time()
    time_string = '16:30:00'
    target_time = datetime.datetime.strptime(time_string, "%H:%M:%S").time()
    if now_time == target_time:
        remind(message)
        time.sleep(60)
    else:
        time.sleep(30)
