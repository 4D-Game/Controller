#!/usr/bin/env python3

"""
Created: 11/10/21
by: Sonja Lukas
First spaceobject code 
"""
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor #todo: library noch nicht eingebunden
import time
import atexit
import logging

class Spaceship(Adafruit_MotorHAT):
    """
    MotorHAT lib contains MotorHAT class which is the main PWM controller
    Arguments:
        num: 1 - 4 for terminal number that the motor is attached to
    """
    def __init__(self, controller, num, name):
        super().__init__(controller, num)
        self.dc_motor = getMotor(num)
        self.name = name

    def local_map(x, in_min, in_max, out_min, out_max):
        """
        maps the percentage range -100 to -1 or 1 to 100  to speedrange 0 - 255

        """         
        return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)    

    def motor_run(self, global_speed):
        """
        Function for directions: FORWARD, BACKWARD, STOP
        """ 
        #case FORWARD          
        if (global_speed>0) and (global_speed<101):  
            speed = local_map(global_speed, 1,100,1,255)
            self.setSpeed(speed)            
            run(Adafruit_MotorHAT.FORWARD)
        #case STOP
        elif global_speed==0:
            self.setSpeed(0)
            run(Adafruit_MotorHAT.RELEASE) #todo: lässt motorspannung los, wird noch auf stillstand geändert
        #case BACKWARD     
        elif (global_speed<0) and (global_speed>-101):
            speed = local_map(global_speed,-100,-1,1,255)
            self.setSpeed(speed)
        else:
            logging.info(f"Something went wrong in motor_run")            
  

