'''
Created on Apr 24, 2009

@author: Peter
'''


import os


from Graph import *
from Line import *
from Node import *
from docutils.parsers.rst.directives import path
from copy import deepcopy

class Graph(object):


    def __init__(self, folder_name):
        '''
        Constructor
        '''
        os.chdir( folder_name )
        self.nodes = dict()
        f = open('nodes.txt', 'r')
        for line in f:
            l=line.rstrip()
            l=l.split('\t')
            id=l[0]
            v=Vector([float(l[1]), float(l[2])])
            self.nodes.setdefault(id, Node(id,v))
        f.close()
        
        self.lines = dict ()
        f = open('lines.txt', 'r')
        for line in f:
            l=line.rstrip()
            l=l.split('\t')
            for n in self.nodes.viewkeys():
                if n==l[1]:
                    self.nodes[n].attach(l[0])
                    p1=self.nodes[n].getPosition()
                elif n==l[2]:
                    self.nodes[n].attach(l[0]);
                    p2=self.nodes[n].getPosition()
            length=(Vector(p1-p2)).length()
            self.lines.setdefault(l[0], Line(l[0], l[1], l[2],length))       
        
        f.close()
        
        
    def __str__(self):  
        nodelist='\n'
        linelist='\n'
        for i in self.nodes.viewvalues():
            nodelist+='NodeId:'+str(i)+'\n'
        for j in self.lines.viewvalues():
            linelist+='LineId:'+str(j)+'\n'
        return nodelist+'\n'+linelist
    
    def findPath(self, startID, endID):
        if startID not in self.nodes.keys() :
            print "unknown nodeid=%s" % startID
        if endID not in self.nodes.keys():
             print "unknown nodeid=%s" % endID
        global pathlist
        (traveledLines, traveledNodes)=([],[])
        path= dict (nodepath=[], linepath=[], length= 0.0)
        pathlist=[]
        startID=str(startID)
        endID=str(endID)
        self.findPathInside(startID,endID, path,traveledNodes, traveledLines)
        return pathlist
         
        
    def findPathInside(self, startID, endID, path,traveledNodes, traveledLines):

        if startID not in traveledNodes:
            traveledNodes=deepcopy(traveledNodes)
            traveledNodes.append(startID)
            traveledLines=deepcopy(traveledLines)
            for l in self.nodes[startID].getAttachedLines():
                if (l not in traveledLines):
                    traveledLines.append(l)
                    for n in self.lines[l].getNodes():
                        if n not in traveledNodes:
                            pathInside=deepcopy(path)
                            pathInside['nodepath'].append(startID)
                            pathInside['linepath'].append(l)
                            pathInside['length']+=self.lines[l].length
                            if n==endID:     
                                pathInside['nodepath'].append(endID)
                                pathlist.append(pathInside)
                            else:
                                self.findPathInside(n, endID, pathInside,traveledNodes, traveledLines)
        
        
    
    def findShortestPath(self, startID, endID):
        allPath=self.findPath(startID, endID)
        shortestLen=allPath[0]['length']
        j=0
        for i in range(1,len(allPath)):
            if allPath[i]['length']<shortestLen:
                j=i
                shortestLen=allPath[i]['length']
        return allPath[j]
    
    def numNodes(self):
        return len(self.nodes)
    
    def numLines(self):
        return len(self.lines)
    