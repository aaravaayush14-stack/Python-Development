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