# Creating your own function:
'''
def MyFunc():
    print("Hello, you!")
MyFunc()
'''

# Deep Use of function and returning values 
# (If you use keywords while using arguments order doesn't matter)
'''
def Celsius():
    return float(input("Enter the temperature in celsius: "))
def Farenheit(x):
    return (9*x/5)+32.0
def printing(x,y):
    print(x,"Degrees Celsius to Degrees Farenheit is: ",y)
a=Celsius()
b=Farenheit(a)
printing(a,b)
'''

# Using Function by specifying parameter but not using any argument
'''
def Func(x=10):
    print(x)
Func(89) # Calling with an argument
Func() # Calling without an argument
'''

# Unknown number of arguments
'''
def Fruits(*Fruits_list): # Use * if you don't know how many arguments are going to be used
    for i in Fruits_list:
        print(i)
Fruits('apple','banana','orange','cherry') # The arguments are sent to function as tuple
Fruits('Raspberry','Kino','Grapefruit')

def names(**name): # Use ** for named arguments
    print(name['fname'],name['lname'])
names(fname='Aayush',lname='Aarav',oname='BYUSDUGYGU')
'''

# Unpacking using * and **
'''
def summation(a,b,c):
    return a+b+c
nos=[7,8,5]
result=summation(*nos) # Same as summation(7,8,5)
print(result)

def printing_name(fname, lname):
    print("Hello,",fname,lname,'!')
name_id_1={'fname':'Aayush','lname':'Aarav'}
printing_name(**name_id_1) # Same as printing_name(fname='Aayush',lname='Aarav')
'''

# Scope of Variables
'''
# Global x in local space
x=300
def Loc():
    print(x,'Accesing global x in local space')
print(x,'Accesing global x in global space')
Loc()

# Using global keyword, vs non-global variable
a=100
b=300
def ChangingGlobal():
    global a
    b=200
    a=200
    print(a,'Local Space for a')
    print(b,'Local Space for b')
print(a,'Global Space 1 for a ')
print(b,'Global Space 1 for b')
ChangingGlobal()
print(a,'Global Space 2 for a')
print(b,'Global Space 2 for b')

# Using nonlocal keyword
def Func1():
    x0='Hello!'
    print(x0,'Before using the nonlocal keyword')
    def Func2():
        nonlocal x0 # This upgrades the scope to outer function
        x0='Good, Morning!'
        print(x0,'Using nonlocal keyword to upgrade scope')
    Func2()
    return x0
print(Func1(),'After Using nonlocal keyword')
# Always follow the scope in LEGB Rule
'''

# Use of decorators: They input a function and outputs a new function
'''
def decorator(func): # Decorates original function
    def wrapper():
        print("Starting Sum...")
        func()
        print("Ending Sum...")
    return wrapper
@decorator
def func(): # Original Function
    a=int(input('Enter 1st Number: '))
    b=int(input("Enter 2nd number: "))
    print(a+b)
func()
'''

# Arguments in dceorators
'''
def changeCase(name):
    def wrapper(x): # Always include arguments here which you use in 'to-be-decorated' function
        print("Starting Swap-Case procedure...")
        print(name(x).swapcase())
        print('Ending Swap-Case Procedure...')
    return wrapper
@changeCase
def name(x):
    return x
name('AaYuSh')
'''

# To use multiple decorators, remember that the it is executed in reverse order. (starting from closest to func)
# Learn about meta-data later.

# Using Decorator Factory "Follows [Factory{Decorator Function(Wrapper Function)}]"
'''
def Factory(n):
    def Decorator_Names(func):
        def Wrapper(*names):
            list_names=[]
            for i in range (1,n+1):
                list_names.append(input(f"Enter name {i}: "))
            func(*list_names)
        return Wrapper
    return Decorator_Names
@ Factory(6)
def print_names(*names):
    for i in names:
        print(f'Hello, {i}!')
print_names()
'''

# Lambda Functions [lambda arguments: expression] (Can be used with map(), sorted(), filter(), etc)
'''
exp=lambda a,b: a**b
print(exp(9,3))
'''

# Recursion: A function calls itself (Base+Recursion)
'''
# Eg 1:
def countdown(n):
    if n<=0: print('Done!')
    else:
        print(n)
        countdown(n-1)
countdown(7)

# Eg 2:
fac=1
def Factorial(n):
    global fac
    if n==0: print(f'Factorial: {fac}')
    else:
        fac*=n
        Factorial(n-1)
Factorial(5)

# Eg 3: (Fibonacci Sequence)
def Fibonacci(n):
    if n<=1: return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
print(Fibonacci(7))
'''
