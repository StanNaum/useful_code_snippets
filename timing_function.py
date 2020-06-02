import datetime as dt
import time

print(dt.datetime.now().second)

while True:
    print("Update data:", dt.datetime.now())
    sleep = 60 - dt.datetime.now().second
    print(sleep)
    if sleep >= 58 and sleep <=60:
        print("launching script")
        time.sleep(sleep)
    else:
      print("script postphoned by " + str(sleep))
      time.sleep(sleep)


def timeout(minutes):
    print("Update data:", dt.datetime.now())
    sleep = 60 * (minutes - dt.datetime.now().minute%minutes)
    sleep = sleep - dt.datetime.now().second
    print(f"Sleeping for: {sleep} seconds")
    time.sleep(sleep)

timeout(1)
