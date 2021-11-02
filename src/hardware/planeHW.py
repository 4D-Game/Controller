#!/usr/bin/env python3

"""
Created: 11/01/21
by: Sonja Lukas
First plane hardware_implementation
"""
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
import time
import atexit 
import logging

class PlaneHw(MotorHAT): 
    def __init__(self, num, global_addr):
        super()__init__(num)
        """
            I2C implementation
                Arguments:
                    global_addr: I2C address
                    create a default object no changes to I2C address or frequency at addr=0x60
        """ 
        self.global_addr=global_addr 
        if global_addr==0:
            Adafruit_MotorHAT(addr=0x60) 
        elif global_addr!=0:
            pass    
        else:
            logging.info(f"Something went wrong in planeHW__init__")                  

    def trigger(self, global_speed: int=50):
        """
            Trigger Object with specific speed at startup
            Arguments:
                global_speed: Objectspeed between -100 and 100
        """
        logging.info(f"Plane triggered with speed {global_speed} percent at startup")

        def run_start(self):        
            self.setSpeed(int=127) #entspricht 50% der speed range
            
    def close():
        """
            Called when the Interface is not needed anymore
        """
        self.getMotor(num).run(Adafruit_MotorHAT.RELEASE)
        logging.info(f"Plane interface closed")

    # recommended for auto-disabling motors on shutdown    
    def turn_off_motor(self):
        self.getMotor(num).run(Adafruit_MotorHAT.RELEASE)
    
atexit.register(turn_off_motor)          