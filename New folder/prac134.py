import datetime
date= datetime.date(2026, 7, 22)
today = datetime.date.today()
time = datetime.time(12, 30, 0)
now = datetime.datetime.now()
now = now.strftime("%H:%M:%S %m-%d-%Y")
target_datetime = datetime.datetime(2020, 1, 2, 12, 30, 1)
cur_datetime = datetime.datetime.now()
if target_datetime < cur_datetime:
    print("Target date has passed")
else:
    print("Target date has not passed")
#print(now)
#print(date)