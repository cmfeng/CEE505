from string import lowercase
def frombin(s):
    i=0
    a=0
    le=len(s)
    while i<le:
        a=a+int(s[i])*2**(le-i-1)
        i+=1
    return a

def fromhex(s):
    #return int((s), base=16)
    i=0
    a=0
    le=len(s)
    while i<le:
        a=a+fromhexinside(s[i])*16**(le-i-1)
        i+=1
    return a


from __builtin__ import str
def tobin(val):
    j=val%2
    s=str(j)
    val=val/2
    while val >0:
        j=val%2
        s=str(j)+s
        val=val/2
    return s

def tohex(val):
    j=val%16
    s=tohexinside(j)
    val=val/16
    while val >0:
        j=val%16
        s=tohexinside(j)+s
        val=val/16
    return s

def tohexinside(n):
        if n<10:
            return str(n)
        else:
            return chr(n+87)

def fromhexinside(b):
    b=b.lower()
    if ord(b)<97:
        return int(b)
    else:
        return ord(b)-87
    
  
def testfromhex(s):
    return  fromhex(s)==int(s,16)
def testfrombin(s):
    return frombin(s) == int(s,2)
def testtobin(s):
    return tobin(frombin(s))==s
def testtohex(s):
    return tohex(fromhex(s))==s
print frombin('1001')      
print fromhex('1Ab')
print tobin(5)  
print tohex(31) 
print testfrombin('1011001')
print testfromhex('198a8f')
print testfrombin('1001111111000001')
print testfromhex('1b9a8a86fed')
print testtobin('1000111001')
print testtohex('1aa9ccc8a8fddd')
print testtobin('1001111111000001')
print testtohex('1aa9ccc8a8fddd')
