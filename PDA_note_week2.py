"""
Python Data Analysis
WEEK TWO

Course Note and Quiz 
"""
SPLIT = "====================================="
"""
Iterating over dictionaries.
"""

# Mapping from various cities to their country
capitals = {'USA': 'Washington, D.C.',
            'China': 'Beijing',
            'France': 'Paris',
            'England': 'London',
            'Italy': 'Rome',
            'Russia': 'Moscow',
            'Australia': 'Canberra',
            'Peru': 'Lima',
            'Japan': 'Tokyo'}

print("Direct Iteration")
print("================")

for country in capitals:
    print("{}, {}".format(capitals[country], country))

print("")

print("Iteration over Keys")
print("===================")

for country in capitals.keys():
    print("{}, {}".format(capitals[country], country))

print("")

print("Iteration over Values")
print("=====================")

for city in capitals.values():
    print("Capital city: {}".format(city))

print("")

print("Iteration over Items")
print("===================")

for country, city in capitals.items():
    print("{}, {}".format(city, country))

print("")

print("Checking Membership")
print("===================")

print('England' in capitals)
print('Lima' in capitals)

print('Moscow' in capitals.keys())
print('Italy' in capitals.keys())

print('Houston' in capitals.values())
print('Beijing' in capitals.values())


"""
Tabular data as a nested list.
"""

# Programming language popularity, from www.tiobe.com/tiobe-index
popularity = [["Language", 2017, 2012, 2007, 2002, 1997, 1992, 1987],
              ["Java", 1, 2, 1, 1, 15, 0, 0],
              ["C", 2, 1, 2, 2, 1, 1, 1],
              ["C++", 3, 3, 3, 3, 2, 2, 5],
              ["C#", 4, 4, 7, 13, 0, 0, 0],
              ["Python", 5, 7, 6, 11, 27, 0, 0],
              ["Visual Basic .NET", 6, 17, 0, 0, 0, 0, 0],
              ["PHP", 7, 6, 4, 5, 0, 0, 0],
              ["JavaScript", 8, 9, 8, 7, 23, 0, 0],
              ["Perl", 9, 8, 5, 4, 4, 10, 0]]

# :< align left
# :> align right 
# :^ align center
# :(_)< align left with white space stuffed with what's inside the ()
# the number represents the length of the total string (including both paddings and contents)
format_string = "{:<20}  {:>4}  {:>4}  {:>4}  {:>4}  {:>4}  {:>4}  {:>4}"

# Display langauges table
headers = popularity[0]
# the * split the list into individual item
header_row = format_string.format(*headers)
print(header_row)
print("-" * len(header_row))

for language in popularity[1:]:
    print(format_string.format(*language))

print("")
    
# Finding/selecting items

# What was Python's popularity in 1997?
print("Python's popularity in 1997:", popularity[5][5])

def find_col(table, col):
    """
    Return column index with col header in table
    or -1 if col is not in table
    """
    return table[0].index(col)

def find_row(table, row):
    """
    Return row index with row header in table
    or -1 if row is not in table
    """
    for idx in range(len(table)):
        if table[idx][0] == row:
            return idx
    return -1
    
idx1997 = find_col(popularity, 1997)
idxpython = find_row(popularity, "Python")
print("Python's popularity in 1997:", popularity[idxpython][idx1997])


"""
Tabular data as nested dictionaries.
"""

# Top 10 software products with the most vulnerabilities in 2017
# (through August).  From www.cvedetails.com.
vulnerabilities2017 = {
    'Android': {'vendor': 'Google',
                'type': 'Operating System',
                'number': 564},
    'Linux Kernel': {'vendor': 'Linux',
                     'type': 'Operating System',
                     'number': 367},
    'Imagemagick': {'vendor': 'Imagemagick',
                    'type': 'Application',
                    'number': 307},
    'IPhone OS': {'vendor': 'Apple',
                  'type': 'Operating System',
                  'number': 290},
    'Mac OS X': {'vendor': 'Apple',
                 'type': 'Operating System',
                 'number': 210},
    'Windows 10': {'vendor': 'Microsoft',
                   'type': 'Operating System',
                   'number': 195},
    'Windows Server 2008': {'vendor': 'Microsoft',
                            'type': 'Operating System',
                            'number': 187},
    'Windows Server 2016': {'vendor': 'Microsoft',
                            'type': 'Operating System',
                            'number': 183},
    'Windows Server 2012': {'vendor': 'Microsoft',
                            'type': 'Operating System',
                            'number': 176},
    'Windows 7': {'vendor': 'Microsoft',
                  'type': 'Operating System',
                  'number': 174}
}

# Display vulnerabilities table
print("Product               Vendor        Type               Vulnerabilities")
print("----------------------------------------------------------------------")

for product, values in vulnerabilities2017.items():
    row = "{:21} {:13} {:18} {:8}".format(product, values['vendor'], values['type'], values['number'])
    print(row)

print("")

# Finding/selecting items

# How many vulnerabilites does Windows 7 have?
print(vulnerabilities2017['Windows 7']['number'])

# What product had the most vulnerabilities?
maxproduct = None
maxnumber = -1

for product, values in vulnerabilities2017.items():
    if values['number'] > maxnumber:
        maxproduct = product
        maxnumber = values['number']

print(maxproduct, maxnumber)



"""
Example code for printing the contents of a dictionary to the console
"""

print(SPLIT)

NAME_DICT = {"Warren" : "Joe", "Rixner" : "Scott", "Greiner" : "John"}

def run_dict_methods():
    """
    Run some simple examples of calls to dictionary methods
    """
    
    # Note that these methods return an iterable object (similar to range())
    print(NAME_DICT.keys())
    print(NAME_DICT.values())
    print(NAME_DICT.items())
    print()
    
    # These objects can be converted to lists
    print(list(NAME_DICT.keys()))
    print(list(NAME_DICT.values()))
    print(list(NAME_DICT.items()))

run_dict_methods()




def print_dict_keys(my_dict):
    """
    Print the contents of a dictionary to the console
    in a readable form using the keys() method
    """
    print("Printing dictionary", my_dict, "in readable form")
    for key in my_dict:                                # note my_dict.keys() works here too
        print("Key =", key, "has value =", my_dict[key])
        
        
def print_dict_items(my_dict):
    """
    Print the contents of a dictionary to the console
    in a readable form using the items() method
    """
    print("Printing dictionary", my_dict, "in readable form")
    for (key, value) in my_dict.items():
        print("Key =", key, "has value =", value)


def run_print_dict_examples():
    """
    Run some examples of printing dictionaries to the console
    """
    print()
    print_dict_keys(NAME_DICT)
    print()
    print_dict_items(NAME_DICT)
    
#run_print_dict_examples()

print(SPLIT)

"""
Template- Create a list zero_list consisting of 3 zeroes using a list comprehension
https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions

As a challenge, redo the previous problem using a nested list comprehension
https://docs.python.org/3/tutorial/datastructures.html#nested-list-comprehensions
"""

# Add code here for a list comprehension
zero_list = [0 for idx in range(3)]

# Add code here for nested list comprehension
nested_list = [zero_list for idx in range(5)]


# Tests
print(zero_list)
print(nested_list)

# Output
#[0, 0, 0]
#[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

"""
Solution - Analyze a reference issue involving a nested list
"""

# Create a nested list
zero_list = [0, 2, 0]
nested_list = []
for dummy_idx in range(5):
    # nested_list.append(zero_list)
    nested_list.append(list(zero_list))    # Corrected code
print(nested_list)
    
# Update an entry to be non-zero
nested_list[2][1] = 7
print(nested_list)


# Erroneous output
#[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
#[[0, 7, 0], [0, 7, 0], [0, 7, 0], [0, 7, 0], [0, 7, 0]]

# Desired output
# [[0, 2, 0], [0, 2, 0], [0, 2, 0], [0, 2, 0], [0, 2, 0]]
# [[0, 2, 0], [0, 2, 0], [0, 7, 0], [0, 2, 0], [0, 2, 0]]


# Explanation

# Line 13 is unintentionally updating all 5 entries in nested_list due to a referencing issue.

# Line 9 is creating five references to the SAME onject (the list zero_list) in nested_list.
# Thus, updating one reference to zero_list in nested_list in line 13 updates 
# the other four references to zero_list in nested_list simultaneously. 

# To visualize this reference issue in Python Tutor, visit the URL https://goo.gl/hT4MM3.
# Note the entries in nested_list all refer to SAME list.  

# The solution to this problem is to make a NEW copy of zero_list each  time append()
# is executed. To do this, simply replace zero_list by list(zero_list) in line 9

# To visualize corrected code in Python Tutor, visit the URL https://goo.gl/4nifEg.
# Note that each entry in nested_list now refers to a DISTINCT list.  As a result,
# updates to one item in nested_list do not affect any other part of nested_list.

print(SPLIT)

"""
Template - Create a function make_grade_table(name_list, grades_list) 
whose keys are the names in names and whose values are the
lists of grades in grades
"""


# Add code here

def make_grade_table(name_list, grades_list):
    """
    Given a list of name_list (as strings) and a list of grades
    for each name, return a dictionary whose keys are
    the names and whose associated values are the lists of grades
    """
    
    return dict(zip(name_list, grades_list))
        

# Tests
print(make_grade_table([], []))

name_list = ["Joe", "Scott", "John"]
grades_list = [100, 98, 100, 13], [75, 59, 89, 77],[86, 84, 91, 78] 
print(make_grade_table(name_list, grades_list))


# Output
#{}
#{'Scott': [75, 59, 89, 77], 'John': [86, 84, 91, 78], 'Joe': [100, 98, 100, 13]}


"""
QUIZ
"""
print(SPLIT)

# Question 4 - 5
NUM_ROWS = 5
NUM_COLS = 5

# construct a matrix
my_matrix = []
for row in range(NUM_ROWS):
    new_row = []
    for col in range(NUM_COLS):
        new_row.append(row * col)
    my_matrix.append(new_row)
 
# print the matrix
for row in my_matrix:
    print(row)

def trace(matrix):
	trace_total = 0
	for row_idx, row in enumerate(matrix):
		for col_idx, col in enumerate(row):
			if row_idx == col_idx:
				trace_total += col
	return trace_total

print(trace(my_matrix))
print(SPLIT)

# Question 7
NUM_ROWS = 5
NUM_COLS = 9

# construct a matrix
my_matrix = {}
for row in range(NUM_ROWS):
    row_dict = {}
    for col in range(NUM_COLS):
        row_dict[col] = row * col
    my_matrix[row] = row_dict
    
print(my_matrix)

# print the matrix
for row in range(NUM_ROWS):
    for col in range(NUM_COLS):
        print(my_matrix[row][col], end = " ")
    print()

my_option1 = {2: {6: 12, 2: 4, 0: 0, 7: 14, 5: 10, 3: 6, 8: 16, 4: 8, 1: 2}, 4: {0: 0, 3: 12, 2: 8, 6: 24, 4: 16, 5: 20, 8: 32, 7: 28, 1: 4}, 1: {2: 2, 5: 5, 3: 3, 8: 8, 4: 4, 1: 1, 7: 7, 0: 0, 6: 6}, 3: {4: 12, 0: 0, 8: 24, 6: 18, 7: 21, 3: 9, 5: 15, 1: 3, 2: 6}, 0: {8: 0, 1: 0, 6: 0, 2: 0, 4: 0, 5: 0, 3: 0, 0: 0, 7: 0}}
print(my_option1 == my_matrix)
