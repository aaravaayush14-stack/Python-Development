thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
# Dictionaries can't have duplicate key
print(len(thisdict))

# Accesing items
'''
print(thisdict.get('brand'))
print(thisdict['model'])
print(thisdict.keys())
print(thisdict.values())
print(thisdict) # Before Change
thisdict['year']=2026
print(thisdict) # After Change
thisdict.update({'year'=2025}) # Also used to change a value / Add new values
thisdict['color']='black'
print(thisdict) # Added an item
print(thisdict.items()) # Returns Key-Value List of Tuples
print('model' in thisdict)
'''

# Removing Items
'''
thisdict.pop('year')
print(thisdict)
thisdict.popitem() # Removes Last inserted item
print(thisdict)
# Use del to delete keys and values and clear() to empty it
'''

# Looping in dictionary
'''
for x in thisdict:
    print(x, end=":")
    print(thisdict[x])

for x,y in thisdict.items():
    print(x,y)
'''

# Dict1=Dict2 does shallow copy. For true copy, use Dict2=Dict1.copy()

# Nested Dictionaries
'''
myfamily = {
  "child1" : {
    "name" : "Aayush",
    "year" : 2004
  },
  "child2" : {
    "name" : "Aarav",
    "year" : 2007
  },
  "child3" : {
    "name" : "Aayushi",
    "year" : 2011
  }
}
for i in myfamily:
    print(i, ':')
    print(myfamily[i]['name'], end='---')
    print(myfamily[i]['year'], '\n', sep='')
'''

# Dictionary methods
'''
x=("Grade_of_A","Grade_of_B","Grade_of_C")
y=10
z=dict.fromkeys(x,y) # To assign same value to multiple keys dict.fromkeys(iterable, value)
print(z)

val1=z.setdefault("Grade_of_A",9) # Pretty shit method
print(val1) # Since Grade_of_A already exists as 10, it returns 10
val2=z.setdefault("Grade_of_D",9) # Inserts This key-value pair and returns value i.e. 9
print(val2)
print(z)

# All other methods have been covered in the above section"
'''