#!/usr/bin/env python3

import time
import rospy
from std_msgs.msg import String

import my_library

rospy.init_node("my_importer")

publisher = rospy.Publisher("/the_answer", String, queue_size=1)

while not rospy.is_shutdown():
    publisher.publish(f"The answer is {my_library.what_is_the_answer()}")
    time.sleep(1)
