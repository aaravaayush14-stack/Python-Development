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

# Use of formatting strings
'''
age=19
print(f"My name is Aayush, and am {age} years old")
print(f"{age} in decimal is {age:.2f}")

dictionary={"name":"Aayush", "age":19}
desc="My name is {name}, and am {age} years old"
print(desc.format_map(dictionary))
'''

# Escape sequences
'''
print("\'Aayush Aarav\'")
print("\\Aayush Aarav\\")
print("Aayush\nAarav")
print("Aayush\tAarav")
print("There are also octal and hexadecimal escape sequences")
'''

# String Methods (Part 1)
'''
a="aaYuSh AaRAv"
print(a.capitalize()) # Prints 1st letter capital
print(a.casefold()) # Similar to a.lower() but more agressive when checking equalities on strings
print("APPLE".center(20,'-')) # txt.centre(length of returned string, character on ends that fills up space)
print(a.count('A')) # txt.count(value,start,stop)
print(a.endswith(("RAv","rav"))) # txt.endswith(value,start,stop) <Values could be in a tuple>
print(a.startswith("YUSH",2,6))
print(a.find("u",0,8)) # Raises -1 if string not found ; rfind() returns last position
print(a.index("u",0,8)) # Raises exception when string not found ; rindex() returns last position
print("banana".ljust(10,"-")) 
print("banana".rjust(10,"-"))
print(a.lower())
print(a.upper())
print(" Sir ".lstrip())
print(" Sir ".rstrip())
print(" Sir ".strip())
print(a.replace('a','A',2))
print(a.swapcase())
print(a.title())
print(a.zfill(30))
'''

# String Methods (string.isX)
'''
b="Aayush .123. Aarav"
print(b.isalnum())
print(b.isalpha())
print(b.isascii())
print(b.isdecimal())
print(b[8].isdigit())
print(b[7].isidentifier())
print(b[0:4].islower())
print(b.isnumeric())
print(b[6].isspace())
print(b[0:5].istitle())
print(b[0].isupper())
'''

# String Methods (Reurning or being Used on Iterables)
'''
tup=("Aayush","Aarav","Bellingham","Haaland")
print(' $ '.join(tup))
print("xyz@gamil@com".partition('@'))
print("xyz@gamil@com".rpartition('@')) # Partitions from the last index
print("ABC,XYZ,PQR,IJK,NOP".split(',')) # txt.split(character(s),maximumsplit)
print("ABC,XYZ,PQR,IJK,NOP".rsplit(',',2)) 
print("Monkey climbs\nthe tress".splitlines()) # Specify 'True' if you want to keep the '\n' 
'''