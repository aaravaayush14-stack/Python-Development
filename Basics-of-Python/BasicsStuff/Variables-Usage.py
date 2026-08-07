# Basic Variables usage
'''
# Python already assumes the data type unless you ask it explicitly to define using a type
x=5 
y=str(5) 
print(type(x),type(y)) #  int, string

# Assigning multiple values
a,b,c='Apple','Ball','Car'
print(a,b,c)

# Assigning one value to different variables
p=q=r='777'
print(p,q,r)

# Concept of unpacking of lists, tuples, etc
List=['Aayush','Aarav','Mister']
n1,n2,n3,=List
print(n1,n2,n3)

# Difference between , and + while printing
print("Aayush","Aarav")
print("Aayush"+"Aarav")
'''

# Without use of the global keyword
'''
x="Awesome"
def MyFunction():
   x="Fantastic"
   print(x)
MyFunction()
print(x)
'''
# Use of Global Keyword
'''
x="Awesome"
def MyFunction():
   global x
   x="Fantastic"
   print(x)
MyFunction()
print(x)
'''