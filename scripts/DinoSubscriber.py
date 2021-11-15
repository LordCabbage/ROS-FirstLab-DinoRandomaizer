#!/usr/bin/env python

import rospy
from ros_lab_dino.srv import *
import random
from std_msgs.msg import String

suffixes = ['saurus', 'raptor', 'pteryx', 'stacator',
'rex', 'ceratops', 'gnathus', 'roides', 'draco', 'dromeus']
family = ['Saurischia','Herrerasauridae','Eoraptor', 'Sauropodomorpha', ' Theropoda',
 'Ornithischia', 'Pisanosaurus','Heterodontosauridae','Thyreophora','Cerapoda']
period = ['Triassic', 'Jurassic', 'Cretaceous']


def return_dino_facts(req):
    print("Returning real name of %s"%(req.a))
    L = list(req.a)
    z = random.randint(0,9)
    L[0] = L[0].upper()
    b = ''.join(L) + suffixes[z]
    return DinoFactsResponse(b)

def factback(data):
    x = random.randint(0,9)
    y = random.randint(0,2)
    print("%s belonged to the %s family and lived in the %s"%(data.data,family[x],period[y]))

def dino_facts_server():
    rospy.init_node('DinoSubscriber',anonymous=True)
    f = rospy.Service('dino_facts', DinoFacts, return_dino_facts)
    print("Ready to give you true facts")
    rospy.Subscriber("fgiver",String,factback)
    rospy.spin()

if __name__ == "__main__":
    dino_facts_server()
