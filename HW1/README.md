# HW1
## Expectations
Every exercise requires development of a suitable algorithm, which shall be described in your submitted solution.
You need to implement that algorithm in python.  Your code must be documented in the answer (embedded in a single PDF document.  A folder full of files is not acceptable)
You need to demonstrate that your implementation functions according to the requested specifications.  Do this through a series of program calls and copy the respective output as part three of your solution.
 
## Programing exercises
### Problem 1 - A special "Hello, world!" implementation

Write a function (file hello.py)

def hello(n):
...

such that

"hello()" and "hello(1)" returns the string "Hello, world!"
"hello(n)" with n in 1:5 returns the string "Hello, hello, hello, world!" (example shows n=3)
"hello(n)" for n>=5 returns the string "Lots of hellos, world!"

### Problem 2 - The harmonic sequence and the harmonic series

Create a function (file harmonic.py)

def harmonic(n):
...

which prints the elements ai



of the harmonic sequence and the elements bi of the harmonic series for all i<n in the following format (check the print '...{0} ...'.format() statement):

1 1.000000 1.000000
2 0.500000 1.500000
3 0.333333 1.833333
4 0.250000 2.083333
.
.
n ...

### Problem 3: Binary and Hex code converter

Binary, decimal, and hexadecimal numbers are representation of number with respect to a base, b, of 2, 10, and 16, respectively. Each system requires exactly b ordered numerals as follows

binary: b=2 / (0,1)
decimal: b=10 / (0,1,2,3,4,5,6,7,8,9)
hexadecimal: b=16 / (0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f)
A larger number is then represented as

general: "xyz" = x*base^2 + y*base^1 + z*base^0
binary: "101101" = 1*2^5 + 0*2^4 + 1*2^3 + 1*2^2 + 0*2^1 + 1*2^0 = 45
decimal: "139" = 1*10^2 + 3*10^1 + 9*10^0 = 139
hexadecimal: "a7dc" = 10*16^3 + 7*16^2 + 13*16^1 + 12*16^0 = 42972
Create four functions

frombin(s) where s is a string containing a binary number and the function returns a decimal number
fromhex(s) where s is a string containing a hexadecimal number and the function returns a decimal number
tobin(val) where val is an integer value in the decimal system and the function is to return a string containing the binary representation of val
tohex(val) where val is an integer value in the decimal system and the function is to return a string containing the hexadecimal representation of val
Furthermore, develop a test procedure to verify that your implementation is correct and provide a complete (documented) test result - procedure and output from your routines.


## Deliverables
Upload a zip file that contains a single PDF document serving as documentation for ALL questions. Include a src folder containing all code files.