#!/usr/bin/env python3

"""
Created: 11/10/21
by: Sonja Lukas
First spaceobject hardware code
"""

from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor

import time
import atexit 
import logging

class Spaceship_DC_HW(Adafruit_MotorHAT): 
    def __init__(self, controller, num, global_addr):
        super()__init__(controller, num)
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
            pass #todo   
        else:
            logging.info(f"Something went wrong in Spaceship_DC_HW__init__")                  

    def trigger(self, global_speed):
        """
            Trigger Object with specific speed at startup
            Arguments:
                global_speed: Objectspeed between -100 and 100
        """
        logging.info(f"Spaceship triggered with speed {global_speed} percent at startup")

        def run_start(self):        
            self.setSpeed(int=127) #entspricht 50% der speed range #todo:set global_speed
            
    def close():
        """
            Called when the Interface is not needed anymore
        """
        self.getMotor(num).run(Adafruit_MotorHAT.RELEASE)
        logging.info(f"Spaceship interface closed")

    # recommended for auto-disabling motors on shutdown    
    def turn_off_motor(self):
        self.getMotor(num).run(Adafruit_MotorHAT.RELEASE)
    
atexit.register(turn_off_motor)      