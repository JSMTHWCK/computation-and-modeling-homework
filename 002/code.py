#repurposing at it's finest
def encode(string,a,b):
	string_lowercase = string.lower()
	alphabet = ' abcdefghijklmnopqrstuvwxyz'
	numstring = []

	for lttr in string_lowercase :
		new_number = alphabet.find(lttr)
		encoded_number = a*new_number + b
		numstring.append(encoded_number)
	return numstring

#now we reverse it
def decode(numbers,a,b):
	alphabet = ' abcdefghijklmnopqrstuvwxyz'
	result = ''

	for encoded in numbers :
		decoded_number = (encoded - b)/a
		decoded_letter = alphabet[int(decoded_number)]
		result += decoded_letter
	return result

#unoptimized
'''
def bruteforce(numbers):
	for a in range(1,101):
		for b in range (1,101):
			for nums in numbers:
				
'''

def bisection_search(number,power,precision):
	lower = 0
	upper = number + 1
	while (upper - lower) >= 1/(10**(precision)):
		if ((lower + upper)/2)**(power) > number:
			upper = (lower + upper)/2
		elif ((lower + upper)/2)**(power) < number:
			lower = (lower+upper)/2
		elif ((lower + upper)/2)**(power) == number:
			return ((lower + upper)/2)
	return ((lower + upper)/2)

print(bisection_search(2,2,5))
