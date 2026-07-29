# To use multi-line strings use: """<String here>"""

# Slicing operation <Indexing starts from 0 from front and -1 from back>
'''
a="Aayush_Aarav"
print(a[:4:1]) # Slicing from the start
print(a[:7:2]) # Starts from index 0 and goes upto 7 (exclusive) with a jump of 2
print(a[::-1]) # Reversing Operation (Pointer sets to end of string when no start index specified)
print(a[0:-4]) # Slicing till the end
print(a[7:0:-1])
print(a[:-7:-1]) # Slicing from the start
'''

# Modifying string
'''
a=" Aayush Aarav "
b="Aayush Aarav"
print(a.upper())
print(a.lower())
print(a.strip())
print(a.replace('y','v'))
print(b.split())
print(a+' '+b) # Concatenation
'''

# Use of format specifier
'''
age=19
print(f"My name is Aayush, and am {age} years old")
print(f"{age} in decimal is {age:.2f}")
'''

# Escape sequences
'''
print("\'Aayush Aarav\'")
print("\\Aayush Aarav\\")
print("Aayush\nAarav")
print("Aayush\tAarav")
print("There are also octal and hexadecimal escape sequences")
'''
# String Methods
a="aaYuSh AaRAv"
print(a.capitalize())
print(a.casefold()) # Similar to a.lower() but more agressive when checking equalities on strings
print("APPLE".center(20,'-')) # txt.centre(length of returned string, character on ends that fills up space)
print(a.count('a')) # txt.count(value,start,stop)