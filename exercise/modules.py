# import datetime
# import time 

# print("Hello")
# time.sleep(5)
# print("This is python date modules")

# b_date ="1993-05-10"
# date = datetime.datetime.strptime(b_date, "%Y-%m-%d")
# print(date)

# jobs=[
#     {'title':'python developer', 'exp_date': '2024-12-31'},
#     {'title':'data scientist', 'exp_date': '2026-11-30'},
#     {'title':'web developer', 'exp_date': '2025-01-15'},
# ]

# for job in jobs:
#     exp_date = datetime.datetime.strptime(job['exp_date'], "%Y-%m-%d")
#     today = datetime.datetime.now()
#     if exp_date > today:
#         print(f"Job '{job['title']}' is still valid.")
#     else:
#         print(f"Job '{job['title']}' has expired.")
   
# today = datetime.date.today()
# print(today.strftime("%d/%m/%Y"))

# b_date =datetime.date(1993, 5, 10)
# today = datetime.date.today()
# dd = today - b_date
# print(dd.days)

# print(datetime.datetime.now())

# print(dir(datetime))
# print(datetime.MAXYEAR)
# print(datetime.MINYEAR)


# import datetime
# from zoneinfo import ZoneInfo


# dt = datetime.datetime(2026, 2, 5, 12, tzinfo=ZoneInfo("America/Los_Angeles"))

# print(dt)