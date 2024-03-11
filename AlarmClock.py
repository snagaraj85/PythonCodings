# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 16:29:45 2024

@author: Admin
"""

import winsound
import datetime
import time
dt=datetime.datetime.now()

date=int(dt.strftime("%d"))
mon=int(dt.strftime("%m"))
year=int(dt.strftime("%Y"))
hr=int(dt.strftime("%H"))
mins=int(dt.strftime("%M"))
sec=int(dt.strftime("%S"))
print("Current Date/Time: ",dt.strftime("%d-%b-%Y_%H:%M:%S"))

h1=int(input("Enter the hour [0-24] to set Alarm : "))
m1=int(input("Enter the minutes [0-60] to set Alarm : "))
s1=int(input("Enter the seconds [0-60] to set Alarm : "))

alarmtime = str(datetime.datetime(year, mon, date,h1,m1,s1))
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print("Alarm Time: ",alarmtime)
print("Current Time: ",current_time)

i=0
while i>=0:
    print("Current Time: ",datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    time.sleep(1)
    if alarmtime == datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"):
        print("**** Alarm Triggered ****")
        print("Alarm Time: ",alarmtime)        
        print("Current Time: ",datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        frequency = 2500  # Set Frequency To 2500 Hertz
        duration = 3000  # Set Duration To 1000 ms == 1 second
        winsound.Beep(frequency, duration)
        break
    i+=1

