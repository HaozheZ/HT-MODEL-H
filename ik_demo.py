#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
print("Python version:", sys.version)

import numpy as np
sys.path.append('./walking_packet')
from model_h_kinematics import *
from model_h_motors_control import *
from time import sleep
import time

if __name__ == '__main__':
    leg = ModelHLegIK()
    leg_r_ang = leg.LegIKMove("right",[0, 0, -0.30, 0, 0, 0])
    arm_r_ang = [0,-0.1,0]
    leg_l_ang = leg.LegIKMove("left",[0, 0, -0.30, 0, 0, 0])
    arm_l_ang = [0,0.1,0]
    command_list = leg_r_ang + arm_r_ang + leg_l_ang + arm_l_ang
    print(command_list)
    mctl = ModelHCtl()
    ang_move = mctl.MotorCall()
    print(mctl.MotorCall())
    mctl.MotorMove(ang_move)      

