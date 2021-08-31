import math


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


#code
def count_characters(input_string):
	dictionary = {}
	input_string_lower = input_string.lower()
	for letter in input_string_lower:
		if letter not in dictionary:
			dictionary[letter] = 1
		else:
			dictionary[letter] += 1
	return dictionary

#code
def get_first_n_terms_nonrecursive(n):
    terms = []

    for i in range(1, n+1):

        if i == 1:
            newnum = 5
            terms.append(newnum)

        else:
            newnum = 3 * (terms[i-2]) - 4
            terms.append(newnum)

    return terms


def get_nth_term_recursive(n):
	if n == 0:
		return "please choose an integer greater than 0"
	 
	if n == 1:
		return 5

	else:
		#this should? be right
		return 3*get_nth_term_recursive(n-1) -4



def convert_to_base_10(n):
	number = len(str(n)) - 1
	finnum = 0
	for binary in str(n):
		if binary == "0":
			finnum += 0
		else:
			finnum += 2**number
		number -= 1
	return finnum

#code
def convert_to_base_2(n):
    exponent_list = []
    output = 0

    while n > 0:
        n_log_base_2 = math.log(n, 2)
        rounded_log = math.floor(n_log_base_2)
        n = n - 2**rounded_log
        exponent_list.append(rounded_log)

    for exponent in exponent_list:
        output += 10**exponent

    return(output)