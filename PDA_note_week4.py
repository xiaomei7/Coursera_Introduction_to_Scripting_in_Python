"""
Python Data Analysis
WEEK THREE

Course Note and Quiz 
"""

SPLIT = "====================================="

print(SPLIT)
"""
Example code to sort sequences.
"""

import random

# Easily create a list of numbers
data = list(range(10))
print("range data:", data)

# Randomly shuffle those numbers
random.shuffle(data)
print("shuffled data:", data)

# Sort the list of numbers
data.sort()
print("sorted data:", data)

# Shuffle it again
random.shuffle(data)
print("shuffled data:", data)

# Use sorted to sort the list
newdata = sorted(data)
print("data after sorted:", data) # the sorted() does not change the original data
print("returned from sorted:", newdata)

# Convert to a tuple
datatup = tuple(data)
print("data tuple:", datatup)

# Sort the tuple of numbers
# datatup.sort(); does not work because tuple is unmutable 
print("tuple after sort:", datatup)

# Use sorted to sort the tuple
newdatatup = sorted(datatup) # sorted will take anything that is iteratable 
print("returned from sorted:", newdatatup)

# Create a dictionary of squares (dictionary comprehension)
datamap = {key: key ** 2 for key in datatup}
print("data dictionary:", datamap)

# Use sorted to sort the dictionary
sortmap = sorted(datamap) # will only sort the keys, sorted() will always return a list!
print("returned from sorted:", sortmap)

print(SPLIT)

"""
Examples of creating and using anonymous functions.
"""

# Easily create a list of numbers
data = list(range(10))
print("range data:", data)

def square(val):
    return val ** 2

# Square all numbers in the list
squares = list(map(square, data)) # map(function, iterable, ...)
print("squares:", squares)

# Double all numbers in the list
doubles = list(map(lambda num: num * 2, data))
print("doubles:", doubles)

# Create a list of random numbers (list comprehension)
randnums = [random.randrange(2, num+3) for num in range(10)]
print("random numbers:", randnums)

# Create a list of tuples
tups = list(map(lambda num1, num2: (num1, num2), data, randnums))
print("tuples:", tups)

# Create a list of the min values in the tuples
mins = list(map(lambda pair: min(pair[0], pair[1]), tups))
print("minimums:", mins)

# Create a list only of tuples where the second item is less than the first
newtups = list(filter(lambda pair: pair[1] < pair[0], tups))
print("filtered:", newtups)

print(SPLIT)

"""
More advanced sorting examples.
"""

# Easily create a shuffled list of numbers
data = list(range(10))
random.shuffle(data)
print("shuffled data:", data)

# Sort the list of numbers
data.sort()
print("ascending sort:", data)
data.sort(reverse=True)
print("descending sort:", data)

# Create a list of tuples
datatups = [(item, random.randrange(3, 15)) for item in data]
print("data tuples:", datatups)

# Sort the list
datatups.sort()
print("sorted data tuples:", datatups)

datatups.sort(key=lambda pair: pair[1])
print("sorted by second item:", datatups)

datatups.sort(key=lambda pair: pair[0] * pair[1], reverse=True)
print("sorted by product:", datatups)

# Shuffle it again
random.shuffle(datatups)
print("shuffled tuples:", datatups)

# Use sorted to sort the list
newdata = sorted(datatups, key=lambda pair: pair[1], reverse=True)
print("tuples after sorted:", datatups)
print("returned from sorted:", newdata)

print(SPLIT)
