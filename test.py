import random
import datetime
import time
from dronekit import connect, VehicleMode, Command, LocationGlobal
from pymavlink import mavutil

connectionString = "com5"
print "Connecting on: ",connectionString
vehicle = connect(connectionString, wait_ready=["groundspeed","attitude","location.global_relative_frame"], baud=57600)


def getFlightData():
    groundSpeed = vehicle.groundspeed
    roll = vehicle.attitude.roll
    pitch = vehicle.attitude.pitch
    altitude = vehicle.location.global_relative_frame.alt
    if altitude < 0:    
        altitude = 0

    return (groundSpeed, roll, pitch, altitude)


while(True):

    # Get real time info from plane and process it
    # converts from m to ft
    (groundSpeed, roll, pitch, altitude) = getFlightData()
    altitude = int(altitude*3.28084)
    groundSpeed = int(groundSpeed*3.28084)    
    print altitude
    print groundSpeed
    
    # get GPS satellite information to test if the GPS is working
    print vehicle.gps_0
