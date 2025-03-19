import datetime

data_oslo = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=2)))
data_sp = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-3)))

print(data_oslo)
print(data_sp)