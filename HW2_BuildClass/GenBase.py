'''


@author: Administrator
'''
from docutils.io import InputError
class GenBase(object):
    def __init__(self, baseIn=10, valueIn=0):
        if (baseIn>=2 and baseIn <=16 and type(baseIn)==int and type(valueIn)==int):
            self.value = dict(base=baseIn, value=valueIn)
        elif(type(valueIn)!=int):
            print "Invalid value input"
            raise InputError
        else:
            print "Invalid base input"
            raise InputError
    def toBase(self): #convert a from base 10 to self.base
        x=self.value['value']
        if x<0:
            x=-x
        transdict={0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'a',11:'b',12:'c',13:'d',14:'e',15:'f'}
        j=x % self.value['base']
        s=transdict[j]
        x=x/self.value['base']
        while x!=0:
            j=x%self.value['base']
            s=transdict[j]+s
            x=x/self.value['base']
        if self.value['value']<0:
            s='-'+s
        return s
    def __add__(self, x):
        if type(x) == GenBase:
            sum=self.value['value']+x.value['value']
            return GenBase(self.value['base'], sum)
        else:
            raise TypeError
    
    def __sub__(self, x):
        if type(x) == GenBase:
            s=self.value['value']-x.value['value']
            return GenBase(self.value['base'], s)
        else:
            raise TypeError
        
    def __mul__(self, x):
        if type(x) == GenBase:
            s=self.value['value']*x.value['value']
            return GenBase(self.value['base'], s)
        else:
            raise TypeError
    def __floordiv__(self,x):
        if type(x) == GenBase:
            s=self.value['value']//x.value['value']
            return GenBase(self.value['base'], s)
        else:
            raise TypeError
    def __mod__(self,x):
        if type(x) == GenBase:
            s=self.value['value']%x.value['value']
            return GenBase(self.value['base'], s)
        else:
            raise TypeError
    def __str__(self):
        x=self.toBase()
        return  "%(value)s (base %(base)s)" % {'value':x, 'base': self.value['base']}
    def Base(self):
        return self.value['base']
    def ChangeBase(self,x):
        return GenBase(x,self.value['value'])
        

        
        
        
