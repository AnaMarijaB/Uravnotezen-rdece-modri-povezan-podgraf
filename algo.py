import math
import numpy
import random
import itertools

mylist=[1,-1]

def mreza(stol, vrst):
	all_nodes=[]
	for x in range(vrst):
		for y in range(stol):
			all_nodes.append([x,y, random.choice(mylist)])
	return all_nodes

print (mreza(2,3))

# generiranje mreže z verjetnostjo 

def mreza_z_verjetnostjo(stol, vrst, p):
	all_nodes=[]
	for x in range(stol):
		for y in range(vrst):
			all_nodes.append([x,y, random.choices(mylist, weights=[p,1-p])])
	return all_nodes



def partition(a_list):
    yield [[x] for x in a_list]   
    for i in range(1, len(a_list) + 1):
        _l = a_list[:]
        yield [_l.pop(i-1), _l]
    yield a_list



def ujemanje(v1, v2):
    for el in v2:
        if el in v1:
            return True
    return False
