# Anything except empty strings, list, 0, etc are evaluated as true
'''
print(bool('a'))
print(bool(''))
print(bool([1,2,3,4]))
print(bool([]))
'''

# Arithmetic Operators
'''
x=11
y=2
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x//y)
print(x%y)
print(x**y)
'''

# Assignment Operator
'''
Use of X=, where X is [+, -, *, **, /, //, %, &(and), |(or), ^(xor), >>, <<]
'''

# Use of Walrus (:=) Operator 
'''
x=[1,2,3,4,5]
if(count:=len(x))>3:
    print("Good")
print(count)
'''

# Ternary operator
'''
print("Good" if (3>4) else "Bad")
x=2
print("One" if x==1 else "Two" if x==2 else "Three" if x==3 else "No") # Replaces elif
'''

# Comparison Operator
'''
x,y,z=3,5,6
print(x==y)
print(x>=y)
print(x<=y)
print(x>y)
print(x<y)
print(x!=y) 
print(1<y<10) # Same as y>1 and y<10
'''

# Logical Operators
'''
x,y,z=1,2,3
print(x>y and y>z)
print(x<=1 or y>z)
print(not(x==23))
'''

# is/is not , in/not in
'''
x=[1,2,3]
y,z=[1,2,3],x
print(x is y)
print(x==y)
print(x is z)
print(x is not y)
print(1 in x)
print(2 not in z)
'''

# Bitwise operators
'''
x=25
print(x&5) # 1
print(x|5) # 29
print(x^5) # 28
print(~5) # -6 {Formula is -x-1}
print(x<<3) # 200
print(x>>1) # 12
'''