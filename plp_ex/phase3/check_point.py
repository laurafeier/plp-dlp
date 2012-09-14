'''
Created on Sep 13, 2012

@author: lfeier
'''
#*******************************
#P1
#*******************************
from _pyio import __metaclass__

tree = ("b", ("a", None, None), ("z", ("c", None, None), ("zz", None, None)))

def do(tree):
    yield tree[0]
    if tree[1] is not None:
        for el in do(tree[1]):
            yield el
    if tree[2] is not None:
        for el in do(tree[2]):
            yield el
            
print [el for el in do(tree)]
#*******************************
#P2
#*******************************

data = set([1, 2, 3])

from itertools import combinations

print [ set(el) for r in range(len(data)+1) for el in combinations(data, r) ] 

#*******************************
#P3
#*******************************
class   Singleton( type ):
    _all_instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._all_instances:
            print "create instance for ", cls
            cls._all_instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._all_instances[cls]
    
class X:
    __metaclass__ = Singleton
    def __init__(self, i):
        self.i = i

class Y:
    __metaclass__ = Singleton
    def __init__(self, i):
        self.i = i

print X(5).i  
print X(2).i
print Y(10).i  
print Y(19).i
