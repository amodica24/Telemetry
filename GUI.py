import tkinter as tk
from tkinter import *
import sys
import datetime
import time
from pyscreenshot import grab
import pyscreenshot as ImageGrab
import tkFont
from ctypes import windll


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

def startgame():
    pass

# take a screenshot of the altitude at which the payloads were dropped
def CDA():
    CDA_label = Label(text = "CDA", font = ('Verdana', 100), fg = 'white', bg = 'black')
    CDA_label.place(x=100,y=150)
    return

def supply():
    supply_label = Label(text = "Supplies", font = ('Verdana', 100), fg = 'white', bg = 'black')
    supply_label.place(x = 100,y=150)
    return        

def habitat():
    habitat_label = Label(text = "Habitats", font = ('Verdana', 100), fg = 'white', bg = 'black')
    habitat_label.place(x=100,y=150)
    return

# current time
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
    # could use >200 ms, but display gets jerky
    clock.after(200, tick)
 
tick()

# create a font size
helv36 = tkFont.Font(family='Verdana', size=16)


#this creates label texts for altitude, the date, and speed
alt_label = Label(text = "Current Altitude (ft): ", font = ('Verdana', 26 ), bg = 'black', fg = 'white')
alt_label.place(x=900,y=80)
speed_label = Label(text = "Current Speed (m/s):", font = ('Verdana', 26),bg = 'black', fg = 'white')
speed_label.place(x = 900, y = 130)

alt_label1 = Label(text = "78 ft", font = ('Verdana', 120 ), bg = 'black', fg = 'white')
alt_label1.place(x = 100, y = 330)

#If you have a large number of widgets, like it looks like you will for your
#game you can specify the attributes for all widgets simply like this.
window.option_add("*Button.Background", "white")
window.option_add("*Button.Foreground", "red")


# create buttons for choosing which payload dropped, logging data, and stopping the program
CDA_button = Button(window, text = "CDA", command = CDA, font = helv36, height = 2, width = 12, fg = "white", borderwidth = 0, bg = 'grey30')
supply_button = Button(window, text = "Supplies", command = supply, font = helv36, height = 2, width = 12, fg = "white", borderwidth = 0, bg = 'grey30')
habitat_button = Button(window, text = "Habitat", command = habitat, font = helv36, height = 2, width = 12, fg = "white", borderwidth = 0, bg = 'grey30')
log_data = Button(window, text = "Log Data", command = screenshot,font = helv36, height = 2, width = 12, fg = "white", borderwidth = 0, bg = 'grey30')
stop = Button(window, text = "Quit", command = window.destroy, font = helv36, height = 2, width = 12, fg = "red", borderwidth = 0, bg = 'grey30')

CDA_button.place(x = 200, y = 700)
supply_button.place(x = 450, y = 700)
habitat_button.place(x = 700, y = 700)
log_data.place(x = 950, y = 700)
stop.place(x = 1200, y = 700)


window.mainloop()
