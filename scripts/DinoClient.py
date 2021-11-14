#!/usr/bin/env python

import sys
import rospy
import random

from ros_lab_dino.srv import *

family = ['Saurischia','Herrerasauridae','Eoraptor', 'Sauropodomorpha', ' Theropoda',
 'Ornithischia', 'Pisanosaurus','Heterodontosauridae','Thyreophora','Cerapoda']
period = ['Triassic', 'Jurassic', 'Cretaceous']

x = random.randint(0,9)
y = random.randint(0,3)

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

if __name__ == '__main__':
    if len(sys.argv) == 2:
        a = (sys.argv[1])
    else:
        print(usage())
        sys.exit(1)
    print("Requesting facts about %s"%a)
    print("%s belonged to the %s family and lived in the %s"%(dino_facts_client(a),family[x],period[y]))
