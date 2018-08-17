from datetime import datetime
import time
import pause
import sys
import os
import getpass
from selenium import webdriver

print(' _______           _______  _______  _______\n')
print('(  ____ \|\     /|(  ____ \(  ____ \(  ____ \ \n')
print('| (    \/| )   ( || (    \/| (    \/| (    \/\n')
print('| (_____ | (___) || |      | (_____ | (_____ \n')
print('(_____  )|  ___  || |      (_____  )(_____  )\n')
print('      ) || (   ) || |            ) |      ) |\n')
print('/\____) || )   ( || (____/\/\____) |/\____) |\n')
print('\_______)|/     \|(_______/\_______)\_______)')
print('Welcome to the Seton Hall Course Sheduling Sniper')
print('Created by Ajay Shah. For any questions email me at ajay.shah@student.shu.edu\n')
time.sleep(1.5)

current_time = (datetime.now())
print ('The current time is')
print (current_time)
print('\n')
input_time = input('Please input the date and time for your scheduling. \nThe format should be: (year-month-day hour:minute:second) \nExample: 2018-06-11 15:30:00\n')
exec_time = current_time.replace(year = int(input_time[0:4]), month = int(input_time[5:7]), day = int(input_time[8:10]),
                                hour = int(input_time[11:13]), minute = int(input_time[14:16]), second = int(input_time[17:19]), microsecond = 000000)

print('The date and time for your course scheduling is ')
print(exec_time)
print('\n')

username = input('What is your Piratenet Login?\n')
password = getpass.getpass('\nWhat is your Piratenet Password?\n')

pin = input('What is your pin to register for classes?\n')

print('Time to get started\n')
print('Opening Piratenet in chrome\n')

dir_path = os.path.dirname(os.path.realpath(__file__))
driver_location = dir_path.__add__('/chromedriver')

browser = webdriver.Chrome(driver_location)
browser.get('https://portal.shu.edu/web/home-community/academics')

userlogin = browser.find_element_by_name('username')
userlogin.send_keys(username)

passlogin = browser.find_element_by_name('password')
passlogin.send_keys(password)

signin = browser.find_element_by_class_name('btn-submit')
signin.click()

print('Entering registration portal...\n')
register_link = browser.find_element_by_partial_link_text('Regist')
register_link.click()

print('Now waiting for time for scheduling to enter in pin and enter in course...')

pause.until(exec_time)

sys.exit()
