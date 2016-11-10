from GenBase import *

x=GenBase(16,255)
y=GenBase(8,255)

z=x+y
a=y+x
b=z+a

print 'type of z: %s' % type(z)     
print 'type of z: %s' % type(a)     
print 'type of z: %s' % type(b)     
print 'base of z is %s' % z.Base()    
print 'base of a is %s' % a.Base()  
print 'z is %s' % z     
print 'a is %s' % a      
print 'b is %s' % b      
