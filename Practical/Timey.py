# ------------------------
# Date & Time #
# ------------------------

import datetime

# print(dir(datetime))

print(datetime.datetime.now())
print(datetime.datetime.now().year)
print(datetime.datetime.today())

print("=" * 50)

print(datetime.datetime.min)
print(datetime.datetime.max)

print("=" * 50)

print(datetime.date.today())

print("=" * 50)

print(datetime.datetime.now().time())
print(datetime.datetime.now().date())

print("=" * 50)

print(datetime.datetime.now().time().hour)
print(datetime.datetime.now().time().minute)

print(datetime.time.min)
print(datetime.time.max)

print( (datetime.datetime.now() - datetime.datetime(2002, 9, 12, 0,0,0)).days )