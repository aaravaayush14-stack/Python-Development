# Range
'''
x=range(0,10,2)
print(x)
print(list(x))
print(list(x[0:3]))
print(len(x))
print(7 in x)
'''

# Treat lists as 'ARRAYS' unless you use NumPy, etc

# Iterators (Just Basic, advanced stuff after learning about classes)
'''
myTuple=('Apple','Banana','Orange')
myIterator=iter(myTuple)
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))
'''

# Using Modules:
'''
import Test_Module as mod
directory=dir(mod) # Lists out all the variable names in the module
print(directory)
'''

# Importing using 'from' keyword
'''
from Test_Module import testModule as tM
tM()
'''

# Math module
'''
import math
print(max(2,3,4))
print(min(2,3,4))
print(abs(-98))
print(pow(3,4))
print(math.sqrt(98))
print(math.floor(1.4))
print(math.ceil(1.4))
print(math.pi)
print(math.gcd(96,60))
print(math.factorial(7))
print(math.sin(math.pi/6))
print(math.cos(math.radians(0)))
print(math.degrees(math.pi/2))
print(math.exp(2))
print(math.perm(7,5))
print(math.prod([1,2,3,4,5,6]))
# And many more functions..........
'''

# Random module
'''
import random
print(random.randrange(1,13,2)) # 13 excluded
print(random.randint(1,5)) # 5 included
print(random.choice(['a','b','c','d','e']))
print(random.random())
# Other methods will be covered with time
'''