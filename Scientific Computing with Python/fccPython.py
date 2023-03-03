# Reading files
fileVar = open(filename, mode) # returns "file handle"; variable used to perform operations on file
    # mode: 'r' for reading and 'w' for writing, not required
for line in fileVar:
    print(line)
# store whole file into single string
str = fileVar.read()

# lists
# same as "arrays", are mutable
len(listVar) # returns length
range() # returns list of numbers from 0 to n-1
# concatonate with +
# can be sliced, like strings, using []
list() # initializes list
listVar.append(n) # appends n to end of list
# Use in and not in to check if element exists in list
listVar.sort() # sorts list
# some built-in functions
len(listVar)
max(listVar)
min(listVar)
sum(listVar)
strVar.split(ch) # breaks string into parts by optional ch(default is space) and produces list of strings

# dictionaries
# same as "mapls"
dict() # initialize dictionary
# to add to dictionary, index a new key, instead of doing .append()
# Dictionary constant
dictVar = { 'key1': val, 'key2': val2}
# use in operator to check if key exists in dictionarys
