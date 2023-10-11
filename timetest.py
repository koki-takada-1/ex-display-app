
# coding: utf-8

import datetime
import pytz


now = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))

print(now.year,now.month)
print(type(now.year))

d1 = datetime.datetime(2023, 10, 10)
d2 = datetime.datetime(2023, 8, 1)
diff = d1 - d2
for i in range(diff.days):
    print(d2 + datetime.timedelta(i))
