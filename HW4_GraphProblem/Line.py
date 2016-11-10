'''
Created on Apr 24, 2009

@author: Peter
'''
from enable.savage.svg.css.values import length

class Line(object):


    def __init__(self, id, nodeIid, nodeJid, length):
        
        self.id = id
        self.nodes = [nodeIid, nodeJid]
        self.nodes.sort()
        self.length=length
        
    def __len__(self):
        return self.length
    
    def getID(self):
        return self.id
    
    def getNodes(self):
        return self.nodes
    
    def attach(self, nodeID):
        self.nodes.append(nodeID)
    
    def detach(self, nodeID):
        self.nodes.remove(nodeID)
        
    def __str__(self): 
        return (self.id+str(self.nodes))
    def length(self):
        return self.length
    
     