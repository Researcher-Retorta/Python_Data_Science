# 1st example
def add_numbers(x, y):
    return x + y

print(type('This is a string'))

print(type(None))

print(type(1))

print(type(1.0))

print(type(add_numbers))

# Tuples are an immutable data structure (cannot be altered).
x = (1, 'a', 2, 'b')
print(type(x))

# Lists are a mutable data structure.
x = [1, 'a', 2, 'b']
print(type(x))

# Use append to append an object to a list.
x.append(3.3)
print(x)

# This is an example of how to loop through each item in the list.
for item in x:
    print(item)

# Or using the index operator
i=0
while( i != len(x) ):
    print(x[i])
    i = i + 1

# Use + to concatenate lists.
print([1,2] + [3,4])

# Use * to repeat lists.
print([1]*3)

# Use the in operator to check if something is inside a list.
print( 1 in [1, 2, 3])

# Now let's look at strings. Use bracket notation to slice a string.
x = 'This is a string'
print(x[0]) #first character
print(x[0:1]) #first character, but we have explicitly set the end character
print(x[0:2]) #first two characters
print(x[-1]) #This will return the last element of the string.
print(x[-4:-2]) #This will return the slice starting from the 4th element from the end and stopping before the 2nd element from the end.
print(x[:3]) #This is a slice from the beginning of the string and stopping before the 3rd element.
print(x[3:]) #And this is a slice starting from the 4th element of the string and going all the way to the end.

# split returns a list of all the words in a string, or a list split on a specific character.
firstname = 'Christopher Arthur Hansen Brooks'.split(' ')[0] # [0] selects the first element of the list
lastname = 'Christopher Arthur Hansen Brooks'.split(' ')[-1] # [-1] selects the last element of the list
print(firstname)
print(lastname)
# Make sure you convert objects to strings before concatenating.
'Chris' + str(2)


## Dictionaries associate keys with values.
x = {'Christopher Brooks': 'brooksch@umich.edu', 'Bill Gates': 'billg@microsoft.com'}
x['Christopher Brooks'] # Retrieve a value by using the indexing operator
x['Kevyn Collins-Thompson'] = 'kevyn@gmail.com'

# Iterate over all of the keys:
for name in x:
    print(x[name])

# Iterate over all of the values:
for email in x.values():
    print(email)

# Iterate over all of the items in the list
for name, email in x.items():
    print(name)
    print(email)

# You can unpack a sequence into different variables:
x = ('Christopher', 'Brooks', 'brooksch@umich.edu')
fname, lname, email = x
print(fname)
print(lname)
print(email)
# Make sure the number of values you are unpacking matches the number of variables being assigned.

