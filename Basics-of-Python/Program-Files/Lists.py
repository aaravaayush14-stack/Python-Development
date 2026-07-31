# Basics of Lists
'''
list1=list() # or list1=[]
list2=["Apple","Banana","Guava","Peach","Cherry"]
print(len(list2))
print(list2[3])
print(list2[0:3:1]) # Slicing same as String
print('Apple' in list2)
list2[4]="Watermelon" # Changing Elements
print(list2)
list2[-1:-3:-1]=["Blackberry","Strawberry"] # -1 index by 'Blackberry' and -2 by 'Stawberry'
print(list2)
'''

# Operations on list
'''
ls1=[1,2,3,4,5]
ls2=["Apple","Banana","Guava","Peach","Cherry"]
ls2.append("Juice") # Adds an item to the last
print(ls2)
ls2.insert(2,"Cake") # lst.insert(index,item)
print(ls2)
tup=("Mango","Papaya","Cupcake")
ls2.extend(tup)
print(ls2)
ls2.remove("Guava") # If more than one occurence, delete 1st occurence
print(ls2)
ls2.pop(5) # Pops out item at specified index. If nothing is given, pops out last item
print(ls2) # Can also use del lst[5]
ls1.clear()
print(ls1)
print(ls1+ls2) # Same as ls1.extend(ls2) for joining
'''

# Looping in a list (All the various methods)
# L1=[4,6,2,7,8,9,3]

# Using for loop
'''
for i in L1:
    print(i)
'''
#Using while loop
'''
j=0
while j<len(L1):
    print(L1[j]+1)
    j+=1
'''
# Using list comprehension
'''
[print(x) for x in L1]
'''

# Understanding List Comprehensions
'''
# Eg1: 

Lo1=[4,6,2,7,8,9,3]
ls=[]
for i in Lo1: # This is the use using for loop
    if(i%2==0):
        ls.append(i)
print(ls)
newlist=[x for x in Lo1 if x%2==0]
print(newlist)

# Eg2:
tv_shows=["friends","PARKS AND RECREATION","the Office","30 rock","modern FAMILY","Mr BEAst","LaTENT"]
tv_s=[x.title() for x in tv_shows]
print(tv_s)
o_in_word=[x for x in tv_s if (('o' in x) or ('O' in x))]
print(o_in_word)
'''

# Sorting (Basic)
'''
a=[18,60,86,52,9,3,67,74,38]
b=['B','O','R','A','C','Z','K']
a.sort()
print(a)
b.sort(reverse=True)
print(b)
'''

# Sorting (Advanced) // Using keys
'''
# Eg1: Sorting on basis of length of string
fruits=['Guava','Cherry','Banana','Apple','Mango','Kino','Fig'] 
print(sorted(fruits, key=lambda x: (len(x),x))) # Sort using both len(x) and x

# Eg2: Nearness to the number 50
nums=[18,60,86,40,52,9,3,67,74,38]
print(sorted(nums,key=lambda x: (abs(x-50),x))) # Makes sure that 40 isn't printed after 60
'''

# Copying lists
'''
List1=[1,2,3,4,5,6]
List2=List1.copy() # Full Copy
del List2[2]
List3=List1[:] # Full Copy
del List3[0]
List4=list(List1) # Full Copy
del List4[5]
print(List1,List2,List3,List4)

List5=List1 # Shallow copy
del List5[3]
print(List1,List5)
'''

# List Methods
'''
LIST1=[7,4,9,4,5,9,9,3,5]
LIST2=[12,78,96,56,709,54]
LIST1.append(0)
LIST2.clear()
print(LIST1.count(5))
LIST2.extend([1,45,97,56])
print(LIST1.index(3)) # Return first occurence of an index. lst.index(value,start,stop)
LIST1.reverse()
print(LIST1)
'''