#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pigpio
import rospy
from std_msgs.msg import Bool

PIN_SWITCH_SIGNAL = 23

rospy.init_node('push_buttun',anonymous=True)

publisher = rospy.Publisher("buttun_pushed", Bool, queue_size=5)

def cb_button_pushed():
    publisher.publish(True)
    rospy.loginfo("pushed")

def cb_button_released():
    publisher.publish(False)
    rospy.loginfo("released")

if __name__ == '__main__':

    gpio = pigpio.pi()

    pin = PIN_SWITCH_SIGNAL

    gpio.set_mode( pin, pigpio.INPUT) 
    gpio.set_pull_up_down( pin, pigpio.PUD_UP )

    gpio.callback( pin, pigpio.RISING_EDGE, cb_button_pushed)
    gpio.callback( pin, pigpio.FALLING_EDGE, cb_button_released)

    try:
        while not rospy.is_shutdown():
            #for now 
            rate.sleep()
    except KeyboardInterrupt:
        pass
    finally:
        pass


