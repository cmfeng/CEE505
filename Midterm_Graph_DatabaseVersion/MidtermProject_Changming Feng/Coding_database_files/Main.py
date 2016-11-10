
from Graph import *

g = Graph('Graph.db')
#print g

nodeIDi='SEA'
nodeIDj='MIA'
shortpath=g.findShortestPath( nodeIDj, nodeIDi)
print shortpath
      
