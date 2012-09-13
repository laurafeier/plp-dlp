'''
Created on Sep 13, 2012

@author: lfeier
'''
#*******************************
#P1
#*******************************

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

