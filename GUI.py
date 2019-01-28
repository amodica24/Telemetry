import tkinter as tk
from tkinter import *
import sys
import datetime
import time
from pyscreenshot import grab
import pyscreenshot as ImageGrab
import tkFont
from ctypes import windll

from dronekit import connect, VehicleMode, Command, LocationGlobal
from pymavlink import mavutil


# Connect to vehicle
connectionString = "com5"
print "Connecting on: ",connectionString
vehicle = connect(connectionString, wait_ready=["groundspeed","attitude","location.global_relative_frame"], baud=57600)

def getFlightData():
    groundSpeed = vehicle.groundspeed
    roll = vehicle.attitude.roll
    pitch = vehicle.attitude.pitch
    altitude = vehicle.location.global_relative_frame.alt
    if altitude < 0:    # Dont let the dropTime become imaginary
        altitude = 0

    return (groundSpeed, roll, pitch, altitude)

window = tk.Tk()

window.title('LMU AirLions')
#You can set the geometry attribute to change the root windows size
window.geometry("1540x840") #You want the size of the app to be 500x500


back = tk.Frame(window,bg='black')
window.configure(background='black')

# create function definitions
# create screenshot definition to save to a file
def screenshot():
    # part of the screen
    img = grab(bbox=(100, 150, 300, 500))
    img.save("screenImage1.jpg")
    img.show()

# gets the altitude information
alt1 = ''
telem = Label(window, font = ('Helvetica',46), bg = 'black', fg = 'yellow')
telem.pack(fill= BOTH, expand = 1)
telem.place(x=950, y=150)

def getAlt():
    global alt1
    (groundSpeed, roll, pitch, altitude) = getFlightData()
    altitude = int(altitude*3.28084)
    if altitude != alt1:
        al1 = altitude
        telem.config(text = altitude)
    telem.after(100,getAlt)
getAlt()

# gets the grounding speed information
speed1 = ''
speed_text = Label(window, font = ('Helvetica',46), bg = 'black', fg = 'orange')
speed_text.pack(fill= BOTH, expand = 1)
speed_text.place(x=1300, y=150)

def getSpeed():
    global speed1
    (groundSpeed, roll, pitch, altitude) = getFlightData()
    groundSpeed = int(groundSpeed*3.28084)
    if groundSpeed != speed1:
        speed1 = groundSpeed
        speed_text.config(text = groundSpeed)
    # calls itself every 100 milliseconds
    # to update the speed display as needed
    speed_text.after(100,getSpeed)
getSpeed()

# make a clock
time1 = ''
clock = Label(window, font=('Verdana', 26), bg='black', fg = 'white')
clock.pack(fill=BOTH, expand=1)
clock.place(x=1100,y=20)

def tick():
    global time1
    # get the current local time from the PC
    time2 = time.strftime('%y-%m-%d %H:%M:%S')
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    clock.after(200, tick)
 
tick()

# get yaw information

yaw1 = ''
yaw_info = Label(window, font = ('Helvetica',46), bg = 'black', fg = 'cyan2')
yaw_info.pack(fill= BOTH, expand = 1)
yaw_info.place(x=1225, y=375)

def getYaw():
    global yaw1
    yaw2 = round(vehicle.attitude.yaw, 3)
    if yaw2 != yaw1:
        yaw1 = yaw2
        yaw_info.config(text = yaw2)
    # calls itself every 100 milliseconds
    # to update the speed display as needed
    speed_text.after(100,getYaw)
getYaw()

    
# create the functions that display which payload was dropped
def CDA():
    CDA_label = Label(text = "CDA", font = ('Verdana', 100), fg = 'white', bg = 'black')
    CDA_label.place(x=100,y=150)
    return

def supply():
    supply_label = Label(text = "Supplies", font = ('Verdana', 100), fg = 'white', bg = 'black')
    supply_label.place(x = 100,y=150)
    return        

def habitat():
    habitat_label = Label(text = altitude, font = ('Verdana', 100), fg = 'white', bg = 'black')
    habitat_label.place(x=100,y=150)
    return


# create a font size
helv36 = tkFont.Font(family='Verdana', size=16)


#this creates label texts for altitude, the date, and speed
alt_label = Label(text = "Altitude (ft)", font = ('Verdana', 24 ), bg = 'black', fg = 'white')
alt_label.place(x=900,y=80)

speed_label = Label(text = "Speed (ft/s)", font = ('Verdana', 24),bg = 'black', fg = 'white')
speed_label.place(x = 1250, y = 80)

gps_label = Label(text = "GPS", font = ('Verdana', 24),bg = 'black', fg = 'white')
gps_label.place(x=900, y=300)

yaw_label = Label(text = "Yaw (deg)", font = ('Verdana', 24),bg = 'black', fg = 'white')
yaw_label.place(x=1250, y=300)

distance_start = Label(text = "Distance from starting location (ft)", font = ('Verdana', 24),bg = 'black', fg = 'white')
distance_start.place(x=900, y = 500)


#If you have a large number of widgets, like it looks like you will for your
#game you can specify the attributes for all widgets simply like this.
window.option_add("*Button.Background", "white")
window.option_add("*Button.Foreground", "red")


# create buttons for choosing which payload dropped, logging data, and stopping the program
CDA_button = Button(window, text = "CDA", command = CDA, font = helv36, height = 2, width = 12, fg = "white", borderwidth = 0, bg = 'grey30')
supply_button = Button(window, text = "Supplies", command = supply, font = helv36, height = 2, width = 12, fg = "white", borderwidth = 0, bg = 'grey30')
habitat_button = Button(window, text = "Habitat", command = habitat, font = helv36, height = 2, width = 12, fg = "white", borderwidth = 0, bg = 'grey30')
stop = Button(window, text = "Quit", command = window.destroy, font = helv36, height = 2, width = 12, fg = "red", borderwidth = 0, bg = 'grey30')

CDA_button.place(x = 350, y = 750)
supply_button.place(x = 550, y = 750)
habitat_button.place(x = 750, y = 750)
stop.place(x = 750, y = 670)


window.mainloop()
