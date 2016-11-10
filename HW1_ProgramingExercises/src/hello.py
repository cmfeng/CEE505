def hello(n=1):
    #This function only works for integers input n, or without input;
    if 1<=n<5:
        x="Hello, "
        x=x+"hello, "*(n-1)
    else:
        x="Lots of hellos, "
    x=x+"World!"
    return x
print "no input: "+ hello()
print "1 "+ hello(1)
print "2 "+ hello(2)
print "3 "+ hello(3)
print "4 "+ hello(4)
print "5 "+ hello(5)
print "88 "+ hello(88)


