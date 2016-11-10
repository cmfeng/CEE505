'''
Created on Apr 19, 2009

@author: Peter Mackenzie
'''
import math

class Vector(object):

    def __init__(self, data):
        self.v = data
    
    def __getitem__(self, i):
        return self.v[i]
    
    def __setitem__(self, i, val):
        self.v[i] = val
    
    def __len__(self):
        return len(self.v)
        
    def __add__(self, x):
        if type(x) == Vector:
            w = self.v[:]
            for i in range(0,len(self)):
                w[i] += x[i]
            return w
        else:
            raise TypeError
        
    def __sub__(self, x):
        if type(x) == Vector:
            w = self.v[:]
            for i in range(0,len(self)):
                w[i] -= x[i]
            return w
        else:
            raise TypeError
        
    def __mul__(self, x):
        if type(x) == Vector:
            w = 0.0
            for i in range(0,len(self)):
                w += self.v[i] * x[i]
            return w
        else:
            raise TypeError

    def __div__(self, x):
        raise NotImplemented
    
    def __str__(self):
        return str( self.v )
    
    def __repr__(self):
        return self.__str__()
    
    def length(self):
        sum=0.0
        for i in self.v:
            sum+=i**2
        return math.sqrt(sum)
    
        