'''
Created on Apr 24, 2009

@author: Peter
'''

from Graph import *

g = Graph('Example_Input\Graph2')
print g
for nodeIDi in g.nodes.keys():
    for nodeIDj in g.nodes.keys():
        if nodeIDi!=nodeIDj:
            pathlist=g.findPath(nodeIDi, nodeIDj)
            for path in pathlist:
                print "The path from %s to %s goes through %s, travel lines %s and has a length of %s"  \
                % ( nodeIDi, nodeIDj, path['nodepath'], path['linepath'],path['length'] )
            shortpath=g.findShortestPath( nodeIDi, nodeIDj)
            print "The shortest path from %s to %s goes through %s, travel lines %s and has a length of %s \n"  \
                % ( nodeIDi, nodeIDj, shortpath['nodepath'], shortpath['linepath'], shortpath['length'] )

            
'''
path=g.findShortestPath('Oakland','San Francisco')
print path['nodepath'], path['length']
    
print g
pathlist=g.findPath('Oakland','San Francisco')
for path in pathlist:
    print path['nodepath'], path['length']

for nodeID in range(1,g.numNodes()): 
    pathlist = g.findPath(0, nodeID)    # path is a structure {nodepath:[], length: float}
    for path in pathlist:
        print "The path to %s goes through %s and has a length of %s"  \
           % ( nodeID, path['nodepath'], path['length'] )
'''