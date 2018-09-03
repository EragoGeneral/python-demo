import psutil

c = psutil.cpu_count()
print(c)

cl = psutil.cpu_count(logical=False)
print(cl)

ti = psutil.cpu_times()
print(ti)

for x in range(10):
    print(psutil.cpu_percent(interval=1, percpu=True))