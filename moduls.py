# date time module

# from datetime import datetime,timedelta

import time



# now = datetime.datetime.now()
# # print("current time :", date)

# print("year :" ,  now.year)
# print(" month :" , now.month)
# print(" Day :" , now.day)
# print(" hours :" , now.hour)
# print(" minuts :" , now.minute)
# print(" second :" , now.second)

# custom date and time

# now = datetime.datetime(2021,5,2,3,5,1)
# print(now)

#  gatting date and time
 
# time() funcation
#date() function
  
# variblename.time()

# now = datetime.datetime.now()

# print(" only time :" , now.time())
# print(" only date :" , now.date())
 
#formating dates()

# strftime()
# strptime()

# now = datetime.datetime.now()

# now = now.strftime("%Y - %m - %d - %H - %M - %S - %A - %B")
# print(now)


# strptime()

# date_string = "16-2-2026 10:26:5"

# now = datetime.datetime.strptime(date_string, "%d-%m-%Y %H:%M:%S")

# print(now)

# date arithmatic

# now = datetime.now()
# new = now + timedelta(days=5, hours=10)
# print(new)

# sleeping 

# time.sleep()

# print("hello")
# time.sleep(2)
# print("and")

# for i in range(13):
#     print(i)
#     time.sleep(1)

# time.perf_counter

# Stime = time.perf_counter()

# time.sleep(2)

# Etime = time.perf_counter()

# print(Etime - Stime)