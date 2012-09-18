'''
Created on Sep 13, 2012

@author: lfeier
'''
#*******************************
#P1
#*******************************
from _pyio import __metaclass__
import __main__
import TYPES
import inspect

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

x5 = X(5).i  
x2 = X(2).i
assert x5 is x2
import ipdb; ipdb.set_trace()
print Y(10).i  
print Y(19).i


#*******************************
#P4
#*******************************
print "**********************"

class DataType():
    STRING =0
    INT = 1

class MyModel():
    
    def __init__(self, **kwargs):
        
        for key in kwargs:
            if key in self.__class__.__dict__:
                if self.__class__.__dict__[key] is DataType.STRING and type(kwargs[key]) is str:
                    self.__dict__[key] = kwargs[key]
                elif self.__class__.__dict__[key] is DataType.INT and type(kwargs[key]) is int:
                    self.__dict__[key] = kwargs[key]
                else:
                    raise Exception("type conversion error")
    
    def save(self):
        all_fields = [f for f in self.__class__.__dict__ if f not in ["__module__", "__doc__"]]
        for f in all_fields:
            if f not in self.__dict__:
                raise Exception("field required to update db")
        print "update table"
        
def model(**options):
    def _model(function):
        def inner():
            model_name = function.__name__
            data = function()
            if options.has_key("name"):
                model_name = options["name"]
            print model_name
            t = type(model_name, (MyModel, ), data)
            globals().update({model_name: t})
        model.all[function.__name__] = inner
        
        return model.all[function.__name__]
    return _model
model.all={}

@model(name="Person")
def some_function():
    return {
            "first_name":DataType.STRING, 
            "last_name": DataType.STRING, 
            "age": DataType.INT
            }

@model(name="Dude")
def asdas():
    return {
            "first_name":DataType.STRING, 
            "last_name": DataType.STRING, 
            "age": DataType.INT
            }
#build all models
print model.all
for k,v in model.all.iteritems():
    v()
    

print MyModel.__subclasses__()

a = Person(first_name="name", last_name="last", age=20)
# todo type conversion error on setters
#a.last_name = 2
a.save() 