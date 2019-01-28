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

# get flight data
def getFlightData():
    groundSpeed = vehicle.groundspeed
    roll = vehicle.attitude.roll
    pitch = vehicle.attitude.pitch
    altitude = vehicle.location.global_relative_frame.alt
    if altitude < 0:    # Dont let the dropTime become imaginary
        altitude = 0

    return (groundSpeed, roll, pitch, altitude)

helv46 = tkFont.Font(family='Verdana', size=46)
data_x = 1010
data_y = 165

label_x = 950
label_y = 100


verd24 = tkFont.Font(family='Verdana', size=24)

# gets the altitude information
alt_label = Label(text = "Altitude (ft)", font = verd24, bg = 'black', fg = 'white').place(x=label_x,y=label_y)
alt1 = ''
telem = Label(window, font = helv46, bg = 'black', fg = 'yellow')
telem.pack(fill= BOTH, expand = 1)
telem.place(x=data_x, y=label_y+65)

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
speed_label = Label(text = "Speed (ft/s)", font = verd24 ,bg = 'black', fg = 'white').place(x = label_x+300, y = label_y)
speed1 = ''
speed_text = Label(window, font = helv46, bg = 'black', fg = 'orange')
speed_text.pack(fill= BOTH, expand = 1)
speed_text.place(x=data_x+300, y=label_y+65)

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



# get latitude
lat_label = Label(text = " Latitude", font = verd24, bg = 'black', fg = 'white').place(x = label_x, y=label_y+180)
lat1 = ''
lat_info = Label(window, font = helv46, bg = 'black', fg = 'lime green')
lat_info.pack(fill= BOTH, expand = 1)
lat_info.place(x= data_x-75, y=label_y+180+65)

def getLat():
    global lat1
    lat2 = round(vehicle.location.global_frame.lat, 3)
    if lat2 != lat1:
        lat1 = lat2
        lat_info.config(text = lat2)
    # calls itself every 100 milliseconds
    # to update the speed display as needed
    lat_info.after(100,getLat)
getLat()

# get longitude
long_label = Label(text = " Longitude", font = verd24, bg = 'black', fg = 'white').place(x=label_x + 300, y=label_y+180)
long1 = ''
long_info = Label(window, font = helv46, bg = 'black', fg = 'red2')
long_info.pack(fill= BOTH, expand = 1)
long_info.place(x=data_x+200, y=label_y+180+65)

def getLong():
    global long1
    long2 = round(vehicle.location.global_frame.lon, 3)
    if long2 != long1:
        long1 = long2
        long_info.config(text = long2)
    # calls itself every 100 milliseconds
    # to update the speed display as needed
    long_info.after(200,getLong)
getLong()

# get yaw information
yaw_label = Label(text = "Yaw (deg)", font = verd24, bg = 'black', fg = 'white').place(x=label_x, y = label_y+360)
yaw1 = ''
yaw_info = Label(window, font = helv46, bg = 'black', fg = 'cyan2')
yaw_info.pack(fill= BOTH, expand = 1)
yaw_info.place(x=data_x-75, y=label_y+360+65)

def getYaw():
    global yaw1
    yaw2 = round(vehicle.attitude.yaw*57.2958, 3)
    if yaw2 != yaw1:
        yaw1 = yaw2
        yaw_info.config(text = yaw2)
    # calls itself every 100 milliseconds
    # to update the speed display as needed
    yaw_info.after(100,getYaw)
getYaw()

#this creates label texts for altitude, the date, and speed

# make a time stamp
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

# create the functions that display which payload was dropped
def CDA():    
    CDA_label = Label(text = "CDA", font = ('Verdana', 100), fg = 'white', bg = 'black').place(x=100,y=150)
    return

def supply():
    supply_label = Label(text = "Supplies", font = ('Verdana', 100), fg = 'white', bg = 'black').place(x = 100,y=150)
    return        

def habitat():
    habitat_label = Label(text = altitude, font = ('Verdana', 100), fg = 'white', bg = 'black').place(x=100,y=150)
    return


#If you have a large number of widgets, like it looks like you will for your
#game you can specify the attributes for all widgets simply like this.
window.option_add("*Button.Background", "white")
window.option_add("*Button.Foreground", "red")

# create font size
helv36 = tkFont.Font(family='Verdana', size=16)
btn_x = 150
btn_y = 720

# create buttons for dropping the payloads
CDA_button = Button(window, text = "CDA", command = CDA, font = helv36, height = 2, width = 12, fg = "white", borderwidth = 0, bg = 'grey30').place(x = btn_x, y = btn_y)
supply_button = Button(window, text = "Supplies", command = supply, font = helv36, height = 2, width = 12, fg = "white", borderwidth = 0, bg = 'grey30').place(x = btn_x + 200, y = btn_y)
habitat_button = Button(window, text = "Habitat", command = habitat, font = helv36, height = 2, width = 12, fg = "white", borderwidth = 0, bg = 'grey30').place(x = btn_x + 400, y = btn_y)
stop = Button(window, text = "Quit", command = window.destroy, font = helv36, height = 2, width = 12, fg = "red", borderwidth = 0, bg = 'grey30').place(x = btn_x+600, y = btn_y)

window.mainloop()
