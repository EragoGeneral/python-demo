from datetime import datetime, timedelta, timezone

#获取当前日期和时间
now = datetime.now()

print(now)

print(type(now))

# 获取指定日期和时间
dt = datetime(2018, 8, 13, 16, 51, 33)
print(dt)

#datetime转换为timestamp
ts = dt.timestamp()
print(ts)

# timestamp转换为datetime
t = now.timestamp()
print(datetime.fromtimestamp(t))
print(datetime.utcfromtimestamp(t))

# str转换为datetime
cday = datetime.strptime('2018-8-13 16:58:32', '%Y-%m-%d %H:%M:%S')
print(cday)

# datetime转换为str
now = datetime.now()
print(now.strftime('%a, %b %d %H:%M'))

# datetime加减
now = datetime.now()
print(now)

print(now + timedelta(hours=10))
print(now - timedelta(days=1))
print(now + timedelta(days=2, hours=12))

#本地时间转换为UTC时间
print('本地时间转换为UTC时间')
tz_utc_8 = timezone(timedelta(hours=8))
now = datetime.now()
print(now)

dt = now.replace(tzinfo=tz_utc_8)
print(dt)


#时区转换
print('时区转换')
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)

bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)

tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)

tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt2)





