# Sets are unordered and un-indexed. You can add and remove items but not change them
'''
set1={'apple','banana','cherry','orange','apple'}
print(set1) # apple is shown only once ((True and 1) and (False and 0) are treated as duplicates)
print(len(set1)) 
set2=set([1,5,8,3,6,9,2])
'''

# You can't access set members using indices as they are unindexed
'''
for i in set1:
    print(i)
print('\n',7 in set2,sep='')
'''

# Adding items
'''
set1.add('melon')
print(set1)
set2.update({10,13,18,21})
print(set2)
set1.update(['fig','resin'])
print(set1)
'''

# Removing Items
'''
set1.remove('banana') 
print(set1)
set1.discard('dumfries') # remove() will cause an error but discard() won't if item doesn't exist
print(set1)
set1.pop() # Removes a random item
print(set1)
set2.clear() # del deletes the entire set
print(set2)
'''

# Join methods
'''
A={1,2,3,4}
B={3,4,5,6,7}
C=A.union(B) # Same as A.update(B); but this changes set A completely. 
print(C) # Also, instead of A.union(B) you can use A|B. To join multiple use set_req=A|B|C|D|.....
D=A.intersection(B) # You can also use D=A&B for intersection purpose
print(D)
E=A.difference(B) # All elements in set A that are not in set B
print(E)
F=A.symmetric_difference(B) # You can also use A^B for symmetric difference
print(F)
# Just like update, there also exists intersection_update and difference_update that changes set A completely
'''

# Frozensets (Items can't be removed or added)
'''
A_set=frozenset({1,2,3,4,5}) 
B_set=frozenset({3,4,5,6,7,8}) # Adding or removing any item causes error
print(A_set.union(B_set))
print(A_set.intersection(B_set))
print(A_set.difference(B_set))
print(A_set.issubset(B_set))
print(A_set.issuperset(B_set))
print(A_set.isdisjoint(B_set))
print(A_set.symmetric_difference(B_set))
'''

# All set methods have already  been covered up