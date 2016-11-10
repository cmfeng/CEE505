'''
Created on Apr 24, 2009

@author: Peter
'''
from Vector import *

class Node(object):
    
    def __init__(self, id, v):

        self.id = id
        self.node = Vector(v)
        self.lines = []
        
    def getPosition(self):
        return self.node
    
    def getID(self):
        return self.id
    
    def attach(self, lineID):
        self.lines.append(lineID)
    
    def detach(self, lineID):
        self.lines.remove(lineID)
        
    def __str__(self): 
        return(self.id + str(self.node)+str(self.lines))
    def getAttachedLines(self):
        return self.lines