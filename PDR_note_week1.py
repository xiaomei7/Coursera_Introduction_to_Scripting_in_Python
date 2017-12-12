"""
Python Data Representatives
WEEK ONE

Course Note and Quiz 
"""

name1 = "Pierre"
age1 = 7
name2 = "May"
age2 = 13

# the use of formatters
line1 = "{0:^7} {1:>3}".format(name1, age1)
line2 = "{0:^7} {1:>3}".format(name2, age2)
print(line1)
print(line2)

num = 3.283663293
output = "{0:>10.3f} {0:.2f}".format(num)
print(output)

# the demonstration of string slices 
name = "𝙲𝚊𝚜𝚝𝚕𝚎 𝙰𝚗𝚝𝚑𝚛𝚊𝚡"
print(name[7:])
print(name[7:13])

# the function that required by the by the week one quiz in Python Data RePresentatives 
def count_vowels(word):
	"""
	This function takes a string

	returns the number of vowels in that string
	"""
	vowels = 0
	for count in word:
		if 'a' == count or 'e' == count or 'i' == count or 'o' == count or 'u' == count:
			vowels += 1

	return vowels

# the function that required by the by the week one quiz in Python Data RePresentatives 
def demystify(l1_string):
	"""
	This function takes one string that only contains l or 1
	replace a with l and b with 1

	returns the new string
	"""
	list_string = list(l1_string)

	for idx, char in enumerate(list_string):

		if char == 'l':
			list_string[idx] = 'a'
		elif char == '1':
			list_string[idx] = 'b'
		else:
			pass

	return "".join(list_string)



print(count_vowels("aaassseefffgggiiijjjoOOkkkuuuu"))
print(count_vowels("aovvouOucvicIIOveeOIclOeuvvauouuvciOIsle"))

print(demystify("lll111l1l1l1111lll"))
print(demystify("111l1l11l11lll1lll1lll11111ll11l1ll1l111"))

word = "shrubbery"
print(word[-1])
print(word[len(word) - 1])
print(word[0])
# print(word[len(word)]



		

