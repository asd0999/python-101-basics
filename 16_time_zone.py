#pip3 install pytz (in terminal)
from datetime import datetime

import pytz

utc = pytz.utc # utc is Coordinated Universal Time
ist = pytz.timezone('Asia/Kolkata') #IST is Indian Standard Time

now = datetime.now(tz=utc) # this is the current time in UTC
ist_now = now.astimezone(ist) # this is the current time in IST.

print(ist_now)