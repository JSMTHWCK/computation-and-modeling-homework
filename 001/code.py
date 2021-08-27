#code
def sum_of_first_n_numbers(n):
	sum = 0
	while (n > 0):
		sum += n 
		n -= 1
	return sum

#code
def check_for_symmetry(input_string):
	return input_string[::-1] == input_string


#code
def convert_to_numbers(string):
	stringlowercase = string.lower()
	alphabet = ' abcdefghijklmnopqrstuvwxyz'
	numstring = []

	for lttr in stringlowercase :
		newnumber = alphabet.find(lttr)
		numstring.append(newnumber)
	return numstring


#code
def is_prime(n):

	for numbers in range(2,n):
		if n % numbers == 0:
			return False
			
		elif n == numbers + 1:
			return True	

#code
def get_intersection(list1, list2):
	intersectlist = []
	for item in list1:
		if item in list2:
			intersectlist.append(item)
	return intersectlist

#code
def get_union(list1, list2):
		unionlist = list1
		for term in list2:
			if term not in unionlist:
				unionlist.append(term)
		return unionlist


#def
def count_characters(input_string):
	dictionary = {}
	input_string_lower = input_string.lower()
	for letter in input_string_lower:
		if letter not in dictionary:
			dictionary[letter] = 1
		else:
			dictionary[letter] += 1
	return dictionary

