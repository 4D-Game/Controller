#!/usr/bin/env python3

"""
Created: 11/22/21
by: Sonja Lukas
Tower control with 2 stepper
Hardware part
"""

import time
import atexit 
import logging
#dont work: 
from ...lib.Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor


class TowerHAL():
    """
        Hardware interface of tower
        Attributes:
            station1: port M1_M2
            station2: port M3_M4
            power1: rotate
            power2: flip
    """ 
    def __init__(self, station=1, power=rotation, global_addr=0):
        """
            I2C implementation
            Arguments:
                global_addr: I2C address
                create a default object no changes to I2C address or frequency at addr=0x60
        """ 
        self.station=station
        self.global_addr=global_addr

        if global_addr==0:
            Adafruit_MotorHAT(addr=0x60) 
        elif global_addr!=0:
            pass #todo for station 1 and 2 
        else:
            logging.info(f"Something went wrong in tower_stepHW __init__")

async def get_position(self, pos:int) -> int: 
    """
        Stepper positions for point system
    """
    return 0 #todo

async def set_position(self): 

    pass

async def turn_off_motor():
    """
        Auto-disabling motors on shutdown   
    """
    self.getMotor(1).run(Adafruit_MotorHAT.RELEASE) 
    self.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    self.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    self.getMotor(4).run(Adafruit_MotorHAT.RELEASE) 

async def on_exit():

    mqtt.client.disconnect() #close tower mqtt connection #doto:connection    

atexit.register(turn_off_motor)



#if __name__ == "__main__": #called as program not as module #only for testing
#