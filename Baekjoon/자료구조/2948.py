#%%
from datetime import datetime
d, m = map(int, input().split())
weekday_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print(weekday_list[datetime(year=2009, month=m, day=d).weekday()])
# %%
