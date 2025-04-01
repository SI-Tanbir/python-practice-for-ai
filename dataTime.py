import datetime

now=datetime.datetime.now()

today_date=datetime.date.today()
today_time=datetime.datetime.now().time()

print(now)
print(today_date)
print(today_time)


formatted_date = today_date.strftime("%Y-%m-%d")
formatted_time = today_time.strftime("%H:%M:%S")

print("Formatted Date:", formatted_date)
print("Formatted Time:", formatted_time)


