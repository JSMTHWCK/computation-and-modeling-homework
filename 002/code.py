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
