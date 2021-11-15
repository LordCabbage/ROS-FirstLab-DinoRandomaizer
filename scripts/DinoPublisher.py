#!/usr/bin/env python

import sys
import rospy

from ros_lab_dino.srv import *
from std_msgs.msg import String

def dino_facts_client(a):
    rospy.wait_for_service('dino_facts')
    try:
        dino_facts = rospy.ServiceProxy('dino_facts',DinoFacts)
        resp = dino_facts(a)
        return resp.b
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def usage():
    return "%s"%sys.argv[0]

def dino_publisher():
    if len(sys.argv) == 2:
        a = (sys.argv[1])
    else:
        print(usage())
        sys.exit(1)
    pub = rospy.Publisher('fgiver', String, queue_size=10)
    rospy.init_node('DinoPublisher', anonymous=True)
    name = dino_facts_client(a)
    print("Requesting facts about %s"%name)
    print("Fact about %s is ready"%name)
    pub.publish(name)

if __name__ == '__main__':
    dino_publisher()
