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


