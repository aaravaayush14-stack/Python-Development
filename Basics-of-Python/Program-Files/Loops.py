# Use of for loops
'''
a=[1,2,3,4,5]
b=(1.89,9.76,9.2,7.8,5.6,)
c="Aayush Aarav"
for i in a:
    print(i)
for i in b:
    if i==7.8: continue
    print(i)
for i in c:
    print(i)
    if i=='u': break
for x in range(0,30,2): # Means Starting from 0, ending at 29 with a jump of 2. [0,2,4,6....]
    print(x)
'''

# Demonstrating use of else in for loop
'''
list1=[1,2,3,4,5,6,7,8]

for i in list1:
    print(i)
else: print("Finally Finished") # Executed

for i in list1:
    if i==5: break
    print(i)
else: print("Finally Finished") # Not Executed because encountered break
'''

# Nested loops:
'''
list2=[[1,2,3,4],['Apple','Banana','Cherry','Mango'],['A','B','C','D'],[1.2,2.3,3.4,4.5]]
for i in list2:
    print(i, end=":\n")
    for j in i:
        print(j)
    print('\n')
'''

# while loop is used for unknown number of iterations
'''
sum=0
while (True):
    a=int(input("Enter Number to be added: "))
    sum+=a
    choice=input("Enter whether you want to input more? Y/N: ").upper()
    if choice=='N': break
print(sum)
'''