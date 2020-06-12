import datetime as dt
import time as tm

print(tm.time()) # time returns the current time in seconds since the Epoch. (January 1st, 1970)

# Convert the timestamp to datetime.
dtnow = dt.datetime.fromtimestamp(tm.time()) 
print(dtnow)

# Handy datetime attributes:
print(dtnow.year, dtnow.month, dtnow.day, dtnow.hour, dtnow.minute, dtnow.second) # get year, month, day, etc.from a datetime

# timedelta is a duration expressing the difference between two dates.
delta = dt.timedelta(days = 100) # create a timedelta of 100 days
print(delta)

# date.today returns the current local date
today = dt.date.today()
print(today)
print(today - delta) # the date 100 days ago
print(today > today-delta) # compare dates