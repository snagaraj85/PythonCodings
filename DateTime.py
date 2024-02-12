"""
Author: Nagarajan S
Course: Python-AI
FileName: DateTime
Batch: 3.30 PM - 5.30 PM
"""
import datetime
from datetime import *
today = datetime.today()
time=datetime.now()
print("Today's date is", today.date())

print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)

print("Current Day No: ",today.isoweekday())
print("Current Week Day: ",today.strftime("%A"))

t=time.strftime("%H:%M:%S")
print("Current Time: ",t)
print("Current Hour: ",time.strftime("%H"))
print("Current Minute: ",time.strftime("%M"))
print("Current Second: ",time.strftime("%S"))

print("Current Date/Time: ",today.strftime("%d-%b-%Y %H:%M:%S"))
