from GenBase import *


x=GenBase(11,22)
y=GenBase(7,36)

print x + y
print x - y
print y - x
print x * y
print x // y
print x % y
print y // x
print y % x
print 'type of x is %s' % type(x)
print 'base of x is %s' % x.Base()
print 'base of y is %s' % y.Base()
x=x.ChangeBase(8)
print 'base of x after change is %s' % x.Base()
print 'x after change is %s'% x

