# if, else, elif statements
'''
if(4<10):
    print(True)
elif(4==10): # Only the 1st elif prints even though next elif(s) maybe true. 
    print("Equal")
elif(4<=10):
    print("Showing elif")
else:
    print(False)
'''

# Shorthand if, if-else for single statements
'''
if 9>0 : print('9 is greater than 0')
print('Aayush') if 9<0 else print('Aarav')
print('9 less than 0') if 9<0 else print('=') if(9==0) else print('9 greater than 0')
'''

# Nested ifs
'''
# Eg1: 
a=-6
if(a%2==0):
    print('Non-Negative even number') if(a>=0) else print("Negative even number")
else:
    print('Non-Negative odd number') if(a>=0) else print("Negative odd number")

# Eg2:
score=int(input("Enter Your Score: "))
attendance=int(input("Enter Your Attendance: "))
if(attendance>=75):
    print('Pass') if score>=40 else print('Fail')
else:
    print('Fail')
'''

# pass statement is like a null , doing nothing
'''
if(10>6):
    pass
'''
