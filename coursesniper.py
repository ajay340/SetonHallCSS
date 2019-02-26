from tkinter import *
from datetime import datetime
import time
import pause
import sys
import os
import getpass
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def submission_of_fields():
    term = e0.get()
    input_time = e1.get()
    username = e2.get()
    password = e3.get()
    PIN = e4.get()
    course1 = e5.get()
    course2 = e6.get()
    course3 = e7.get()
    course4 = e8.get()
    course5 = e9.get()
    course6 = e10.get()
    course7 = e11.get()
    course8 = e12.get()
    course9 = e13.get()
    course10 = e14.get()

    courses = [course1, course2, course3, course4, course5, course6, course7, course8, course9, course10]

    dir_path = os.path.dirname(os.path.realpath(__file__))
    driver_location = dir_path.__add__('/lib/chromedriver')
    browser = webdriver.Chrome(driver_location)

    push_info(term, input_time, username, password, PIN, courses, browser)

def push_info(term, input_time, username, password, PIN, courses, browser):

    def get_execution_time(input_time):
        try:
            exec_time = current_time.replace(year = int(input_time[0:4]), month = int(input_time[5:7]), day = int(input_time[8:10]),
                        hour = int(input_time[11:13]), minute = int(input_time[14:16]), second = 00, microsecond = 000000)
            return exec_time

        except:
            print("\nError: Did you type the time in as shown in the format? Remember the is in a 24 hour format.")
   
    def open_loginPage():
        try:
           browser.get('https://myaccount.shu.edu:4446/PROD/bwskrsta.P_RegsStatusDisp')
        except:
           print("\nError: Is the chromedriver in the same folder as this program or Google Chrome installed?")
    
    def enter_login(username, password):
        try:
            userlogin = browser.find_element_by_name('sid')
            userlogin.send_keys(username)

            passlogin = browser.find_element_by_name('PIN')
            passlogin.send_keys(password)

            signin = browser.find_element_by_xpath("//input[@value='Login']")
            signin.click()

            student_link = browser.find_element_by_partial_link_text('Student')
            student_link.click()
        except:
            print("\nError: Did you type your login credentials correctly?")

    def goto_registration():
        regist_link = browser.find_element_by_partial_link_text('Registration')
        regist_link.click()

        adding_link = browser.find_element_by_partial_link_text('Add or Drop')
        adding_link.click()
    
    def enter_semester_and_pin(term, PIN):
        try:
            select = Select(browser.find_element_by_id('term_id'))
            select.select_by_visible_text(term)

            adding_signin = browser.find_element_by_xpath("//input[@value='Submit']")
            adding_signin.click()

            pinlogin = browser.find_element_by_name('pin')
            pinlogin.send_keys(PIN)
        except:
            print("\nError: Did you type in the semester correctly, like the format shows? Check out the registration link to see what options are available.")

    def wait_to_submit_pin(exec_time):
        pin_signin = browser.find_element_by_xpath("//input[@value='Submit']")
        pause.until(exec_time)
        pin_signin.click()
    
    def enter_course(courses):
        course_input1 = browser.find_element_by_id('crn_id1')
        course_input1.send_keys(courses[0])

        course_input2 = browser.find_element_by_id('crn_id2')
        course_input2.send_keys(courses[1])

        course_input3 = browser.find_element_by_id('crn_id3')
        course_input3.send_keys(courses[2])

        course_input4 = browser.find_element_by_id('crn_id4')
        course_input4.send_keys(courses[3])

        course_input5 = browser.find_element_by_id('crn_id5')
        course_input5.send_keys(courses[4])

        course_input6 = browser.find_element_by_id('crn_id6')
        course_input6.send_keys(courses[5])

        course_input7 = browser.find_element_by_id('crn_id7')
        course_input7.send_keys(courses[6])

        course_input8 = browser.find_element_by_id('crn_id8')
        course_input8.send_keys(courses[7])

        course_input9 = browser.find_element_by_id('crn_id9')
        course_input9.send_keys(courses[8])

        course_input10 = browser.find_element_by_id('crn_id10')
        course_input10.send_keys(courses[9])

        course_adding = browser.find_element_by_xpath("//input[@value='Submit Changes']")
        course_adding.click()

        print("Entered all of your classes successfully.")

    def entering_courses(courses):
        try:
            enter_course(courses)
        
        except:
            try:
                count = 1
                while (count < 4):
                    browser.back()
                    print('Retyping the pin, attempt #', count)
                    pinlogin = browser.find_element_by_name('pin')
                    pinlogin.send_keys(PIN)
                    pin_signin = browser.find_element_by_xpath("//input[@value='Submit']")
                    pin_signin.click()
                    try:
                        enter_course(courses)
                    except:
                        count = count + 1
            except:
                print("\nError: Can not perform any more attempts, are you sure you typed your pin correctly?")


    exec_time = get_execution_time(input_time)

    open_loginPage()
    enter_login(username, password)
    goto_registration()
    enter_semester_and_pin(term, PIN)
    wait_to_submit_pin(exec_time)
    entering_courses(courses)


def clear_fields():
    
   e0.delete(0,END)
   e1.delete(0,END)
   e2.delete(0,END)
   e3.delete(0,END)
   e4.delete(0,END)
   e5.delete(0,END)
   e6.delete(0,END)
   e7.delete(0,END)
   e8.delete(0,END)
   e9.delete(0,END)
   e10.delete(0,END)
   e11.delete(0,END)
   e12.delete(0,END)
   e13.delete(0,END)
   e14.delete(0,END)

current_time = (datetime.now())


master = Tk()
master.title("Seton Hall Course Scheduling Sniper")
screen_width = int(master.winfo_screenwidth() / 2)
screen_height = master.winfo_screenheight()
screen_resolution = str(screen_width)+'x'+str(screen_height)
master.geometry(screen_resolution)
master.configure(bg='#34495e')
master.attributes('-topmost', False)
master.iconbitmap('lib/seha-lg.ico')

Label(master, font=("Roboto", 15), fg="white", bg='#34495e', text='Registration Semester: \nFormat: (Season Year) - Example: (Fall 2018)', height=2).grid(row=0)
Label(master, font=("Roboto", 15), fg="white",bg='#34495e', text="Course Scheduling Time: \nFormat: (year-month-day hours:minutes) \nExample: 2018-06-11 15:30\n").grid(row=1)
Label(master, font=("Roboto", 15), fg="white",bg='#34495e', text="Piratenet Username:").grid(row=2)
Label(master, font=("Roboto", 15), fg="white",bg='#34495e', text="Piratenet Password:").grid(row=3)
Label(master, font=("Roboto", 15), fg="white",bg='#34495e', text="Course PIN Number:").grid(row=4)
Label(master, font=("Roboto", 15), fg="white",bg='#34495e', text="Course Number #1:").grid(row=5)
Label(master, font=("Roboto", 15), fg="white",bg='#34495e', text="Course Number #2:").grid(row=6)
Label(master, font=("Roboto", 15), fg="white",bg='#34495e', text="Course Number #3:").grid(row=7)
Label(master, font=("Roboto", 15), fg="white",bg='#34495e', text="Course Number #4:").grid(row=8)
Label(master, font=("Roboto", 15), fg="white",bg='#34495e', text="Course Number #5:").grid(row=9)
Label(master, font=("Roboto", 15), fg="white",bg='#34495e', text="Course Number #6:").grid(row=10)
Label(master, font=("Roboto", 15), fg="white",bg='#34495e', text="Course Number #7:").grid(row=11)
Label(master, font=("Roboto", 15), fg="white",bg='#34495e', text="Course Number #8:").grid(row=12)
Label(master, font=("Roboto", 15), fg="white",bg='#34495e', text="Course Number #9:").grid(row=13)
Label(master, font=("Roboto", 15), fg="white",bg='#34495e', text="Course Number #10:").grid(row=14)

e0 = Entry(master)
e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master, show="*")
e4 = Entry(master, show="*")
e5 = Entry(master)
e6 = Entry(master)
e7 = Entry(master)
e8 = Entry(master)
e9 = Entry(master)
e10 = Entry(master)
e11 = Entry(master)
e12 = Entry(master)
e13 = Entry(master)
e14 = Entry(master)

e0.grid(row=0, column=1)
e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
e3.grid(row=3, column=1)
e4.grid(row=4, column=1)
e5.grid(row=5, column=1)
e6.grid(row=6, column=1)
e7.grid(row=7, column=1)
e8.grid(row=8, column=1)
e9.grid(row=9, column=1)
e10.grid(row=10, column=1)
e11.grid(row=11, column=1)
e12.grid(row=12, column=1)
e13.grid(row=13, column=1)
e14.grid(row=14, column=1)

submit_button = Button(master, text=' Submit ', command=submission_of_fields).grid(row=15, column=1)
clear_button = Button(master, text=' Clear ', command=clear_fields).grid(row=16, column=1)

mainloop()