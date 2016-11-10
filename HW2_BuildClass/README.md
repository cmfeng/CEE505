# HW2
### 1 Expand Assignment #1 (problem #3) into a class  
 
class GeneralBase (object):  

which holds the internal variables in a dictionary as   

    self.value = dict(base=…, value=‘…’)  

Use the procedures developed under problem #3 through  

   import problem3 as p  

where problem3 needs to be replaced by your filename.
### 2 overload the operators add (+), subtract (-), multiply (*), integer divide (floordiv, //), and modulo (rest of integer division, %). Assume the second value can be given in any general base (2-16), possibly different from the first object base.

### 3 Provide a suitable implementation of __str__(self) , to be tested via the print statement  
>>> x = GenBase( 16, 255 )  
>>> print x  
ff (base 16)  

### 4 Add a method which returns the base of an instance of the class as an integer:  

>>> x = GenBase( 4, 237 )  
>>> x.Base()  
4  

### 5 Add a method ChangeBase(base) to convert an instance of the class to a different base:  

>>> x = GenBase( 4, 237 )  
>>> x.Base()  
4  
>>> x.ChangeBase( 7 )  
>>> x.Base()  
7  

### 6 All functions shall accept numbers in any arbitrary base and return an object of type GeneralBase()  

### 7 Provide reliable error recognition and handling (warning, feedback)  

### 8 Develop a test procedure which generates alternative representation of a series of different decimal values and performs the following operations on them:  

x = GenBase( some_base, some_value)  
y = GenBase( other_base, other_value )  
x + y   
x - y  
y - x  
x * y  
x // y  
x % y  
y // x  
y % x  

### 9 Provide a report which describes the implementation details, the class interface, the testing procedure, and its outcome.