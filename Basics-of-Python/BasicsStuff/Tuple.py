# Tuple have an unchangeable order (immutable btw)
tup1=tuple()
tup2=('Apple','Banana','Mango','Sal','Zirconium','Peach')
tup3=(6,) # To create one member tuple don't forget the ','
print(tup2[3], len(tup2))
print(tup3*4)

# Same Slicing, Indexing, in/not in, etc like the lists

# To add items convert tuple into list and then add, also us ethe same for changing/removing any element
list1=list(tup1)
list1.extend([6,8,20,78,54,98,32])
print(tuple(list1))
print(tup1+(98,76,)) # Never forget the ',' while adding two tuples

# Concept of Unpacking
fruits=('Cherry','Mango','Peach','Muskmelon','Watermelon','Fig')
(a,b,c,d,e,f)=fruits
print(a,b,c,d,e,f)
(a1,a2,*a3)=fruits
print(a1,a2,a3)

# Looping the same way through tuples except the list comprehensions

# Tuple methods
tup4=(1,5,5,6,7,6,6,9,5,5,7,5)
print(tup4.count(5))
print(tup4.index(5,3,9)) # (value,start,stop)