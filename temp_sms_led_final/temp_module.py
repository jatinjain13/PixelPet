import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/firebase")
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/temperature_rpi")
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/sms_module")


import firebase_interface as firebase
import temperature_led
import sms 
import temperature_led
from time import sleep
from sense_hat import SenseHat
sleep(10)
while(True):
  sense = SenseHat()
  sense.clear()
  temp = round(sense.get_temperature(),1) #measure temp data using RPI's builtin sensor
  firebase.write_database("Temperature",temp) #write measured data onto fyrebase
  sms.sendSMS("Temperature",temp) #send sms with temp data
  temperature_led.set_led(temp) # indicate temperature on LED
