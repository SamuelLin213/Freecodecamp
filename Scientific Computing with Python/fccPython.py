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
dictVar.get(key, defaultVal) # returns value of key, if key doesn't exist create one w/ defaultVal
    # useful in counting
    for name in names:
        counts[name] = counts.get(name, 0) + 1
# loop through keys in dictionary
for key in dictVar:
    print(key, counts[key])
# Retrieving keys and value of dictionarys
dictVar.keys() # returns keys
dictVar.values() # returns values
dictVar.items() # returns a "tuple" of both keys and values
# Iterating through dictionary using key-value pairs
for keyVal, valVal in dictVar.items():
    print(keyVal, valVal)

# Tuples
# are like lists, however, they're immutable
# cannot append, sort or reverse
# more efficient then lists; use for temp variables
# can even use left-hand assignment
(x, y) = (4, 'fred')
print(x) # 4
print(y) # fred
# dictVar.items() returns list of tuples
for (k, v) in d.items():
    print(k, v)
# comparison operators compare elements from left to right
# Sorted tuple
sorted(d.items()) # returns tuple of sorted dictionary items
for k, v in sorted(d.items()):
    print(k, v)
# can also sort by value instead
tmp = list()
for k, v in c.items():
    tmp.append( (v, k) )
tmp = sorted(tmp, reverse=True) # returns list of tuples sorted by value

# regex
import re
re.search(regex, stringVar) # see if string matches regex
re.findall() # extracts portions of string that match

# SQL
CREATE TABLE "Users" ("name" TEXT, "email" TEXT)
INSERT INTO Users (name, email) VALUES ('Kristin', 'kf@umich.edu')
DELETE FROM Users WHERE email='ted@umich.edu'
UPDATE Users SET name='Charles' WHERE email='csev@umich.edu'
SELECT * FROM Users WHERE email='csev@umich.edu'
SELECT * FROM Users ORDER BY name DESC
# Types of keys
#   -primary: integer auto-increment field
#   -logical: what outside world uses for lookup, never use as primary
#   -foreign: integer key pointing to row in another table, stores primary key of another table
CREATE TABLE "Artist" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
    "name" TEXT
)
# Joining tables together with Join
select Album.title, Artist.name from Album join Artist on Album.artist_id = Artist.id
# Joining without using on gives all possible combos of rows
select Track.title, Track.genre_id, Genre.id, Genre.name FROM Track JOIN Genre
