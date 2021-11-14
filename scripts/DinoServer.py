#!/usr/bin/env python

import rospy
from ros_lab_dino.srv import *
import random

suffixes = ['saurus', 'raptor', 'pteryx', 'stacator',
'rex', 'ceratops', 'gnathus', 'roides', 'draco', 'dromeus']


def return_dino_facts(req):
    print("Returning fact about %s"%(req.a))
    L = list(req.a)
    z = random.randint(0,9)
    L[0] = L[0].upper()
    b = ''.join(L) + suffixes[z]
    return DinoFactsResponse(b)

def dino_facts_server():
    rospy.init_node('dino_facts_server')
    f = rospy.Service('dino_facts', DinoFacts, return_dino_facts)
    print("Ready to give you true facts")
    rospy.spin()
if __name__ == "__main__":
    dino_facts_server()
