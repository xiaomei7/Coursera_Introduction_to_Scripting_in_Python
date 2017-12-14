"""
Python Data Representatives
WEEK TWO

Course Note and Quiz 
"""

# range(start, end, step)
# this range starts at 4, end at 27 (not included), and increment 5 at a time
# step can be negative
seq = range(4, 27, 5)
print(seq, list(seq))

"""
Solution - Create a list formed by excluding the first and last items of example_list
"""

example_list = [2, 3, 5, 7, 11, 13]
middle_list = example_list[1 : -1]
print(middle_list)

# Output
#[3, 5, 7, 11]

"""
Solution - Create a list formed by 8 copies of True and 8 copies of False
"""

truefalse_list = 8 * [True] + 8 * [False]
print(truefalse_list)

# Output
#[True, True, True, True, True, True, True, True, False, False, False, False, False, False, False, False]

# quiz NO.5
n = 5
test_string = "xxx" + " " * n + "xxx"
split_list = test_string.split(" ")

print(split_list)
print(len(split_list))

# quiz NO.6
# list1 = list(range(1, 10))
# list2 = list1[:]

# list1 = list(range(1, 10))
# list2 = list(list1)

list1 = list(range(1, 10))
list2 = [] + list1

print(list1)
print(list2)

list1[0] = 10

print(list1)
print(list2)

# quiz NO.7
def strange_sum(numbers):
	"""
	Input: list of integer

	Return: sum of those items in the list that are not divisible by 3
	"""
	sum = 0
	for num in numbers:
		if num % 3 != 0:
			sum += num

	return sum

print(strange_sum([1, 2, 3, 4, 5, 1, 2, 3, 4, 5]))
print(strange_sum(list(range(123)) + list(range(77))))




