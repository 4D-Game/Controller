#!/usr/bin/env python3

"""
Created: 11/01/21
by: Sonja Lukas
First plane coding 
"""
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor #noch nicht eingebunden
import time
import atexit
import logging

class Plane(MotorHAT):
    """
    MotorHAT lib contains MotorHAT class which is the main PWM controller
    Arguments:
        num: 1 - 4 for terminal number that the motor is attached to
    """
    def __init__(self, num, global_player_points, global_speed):
        super().__init__(num)
        self.global_player_points = global_player_points
        self.global_speed = global_speed
        self.dc_motor = getMotor(num)

    def motor_run(self, global_speed):
        """
        Function for directions: FORWARD, BACKWARD, RELEASE
        maps the percentage range -100 to -1 or 1 to 100  to speedrange 0 - 255

        """            
        def local_map(x, in_min, in_max, out_min, out_max):
                return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)
        if (global_speed>0) and (global_speed<101):  
            speed = local_map(global_speed, 1,100,1,255)
            self.setSpeed(speed)            
            run(Adafruit_MotorHAT.FORWARD)
        elif global_speed==0:
            self.setSpeed(0)
            run(Adafruit_MotorHAT.RELEASE) #lässt motorspannung los, wird noch auf stillstand geändert 
        elif (global_speed<0) and (global_speed>-101):
            speed = local_map(global_speed,-100,-1,1,255)
            self.setSpeed(speed)
        else:
            logging.info(f"Something went wrong in motor_run")            

    # recommended for auto-disabling motors on shutdown   
    def turn_off_motor(self):
        self.getMotor(num).run(Adafruit_MotorHAT.RELEASE)
    
atexit.register(turn_off_motor)   

