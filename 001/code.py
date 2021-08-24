def sum_of_first_n_numbers(n):
	sum = 0
	while (n > 0):
		sum += n 
		n -= 1
	return sum


def check_for_symmetry(input_string):
	return input_string[::-1] == input_string

#test
print(check_for_symmetry('tacocat'))

def convert_to_numbers(string):
	strng = string.lower()
	alphabet = ' abcdefghijklmnopqrstuvwxyz'
	numstring = []

	for lttr in strng :
		newnumber = (alphabet.find(lttr))
		numstring.append(newnumber)
	return numstring

#test 
print(convert_to_numbers('a cat'))

#test
def is_prime(n):

	for numbers in range(2,n):
		if n % numbers == 0:
			return False
			
		else:
			return True	

#code
print(is_prime(13))

