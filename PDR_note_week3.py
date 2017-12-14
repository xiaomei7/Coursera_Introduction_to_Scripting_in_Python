"""
Python Data Representatives
WEEK THREE

Course Note and Quiz 
"""

"""
Solution - Update a slice of a list
"""

example_list = [2, 3, 5, 7, 11, 13]
print(example_list)

# Enter update code here
example_list[1 : 3] = [0, 0, 0]
print(example_list)

# Output
#[2, 3, 5, 7, 11, 13]
#[2, 0, 0, 0, 7, 11, 13]


"""
Solution - Extend a list with another list
"""

example_list = [2, 3, 5, 7, 11, 13]
print(example_list)

# Enter update code here
example_list.extend([0, 0, 0])
print(example_list)

# Output
#[2, 3, 5, 7, 11, 13]
#[2, 3, 5, 7, 11, 13, 0, 0, 0]


"""
Solution - Shuffle the items in a list
"""

import random

example_list = [2, 3, 5, 7, 11, 13]
print(example_list)

# Enter update code here

random.shuffle(example_list)    
print(example_list)


# Output - note that order of second list may vary due to randomness
#[2, 3, 5, 7, 11, 13]
#[11, 2, 7, 5, 13, 3]

# the reverse() does not return any value, it just alter the orginal list
# so the second print gives NONE
my_list = [1, 3, 5, 7, 9]
my_list.reverse()
print(my_list)
print(my_list.reverse())

# quiz NO.6
def fib(input_list):
	"""
	Input: a list contains [𝟶, 𝟷]

	Return: the value of the last item in 𝚏𝚒𝚋 after twenty iterations
	"""
	out_list = list(input_list)
	for i in range(20):
		out_list.append(out_list[-1] + out_list[-2])
	return out_list[-1]

print(fib([0, 1]))


"""
Implement the Sieve of Eratosthenes
https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
"""

# quiz NO.7
def compute_primes(bound):
    """
    Return a list of the prime numbers in range(2, bound)
    """
    
    # answer = list(range(2, bound))
    # for divisor in range(2, bound):
    #     # Remove appropriate multiples of divisor from answer
    #     for num in range(2, bound):
    #     	try:
    #     		answer.remove(divisor * num)
    #     	except ValueError:
    #     		pass
    # print(answer)
    # return answer

    answer = list(range(2, bound))
    for divisor in range(2, bound):
        for stride in range(2 * divisor, bound, divisor):
            if stride in answer:
                answer.remove(stride)
    return answer

print(len(compute_primes(200)))
print(len(compute_primes(2000)))

