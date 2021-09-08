#repurposing at it's finest
def encode(string,a,b):
	string_lowercase = string.lower()
	alphabet = ' abcdefghijklmnopqrstuvwxyz'
	numstring = []

	for lttr in string_lowercase :
		new_number = alphabet.find(lttr)
		encoded_number = a * new_number + b
		numstring.append(encoded_number)
	return numstring


def decode(numbers,a,b):
	alphabet = ' abcdefghijklmnopqrstuvwxyz'
	result = ''

	for encoded in numbers :
		decoded_number = (encoded - b) / a
		if decoded_number.is_integer() == False or decoded_number < 0:
			return "error, values are incorrect"
		decoded_letter = alphabet[int(decoded_number)]
		result += decoded_letter
	return result


def bruteforce(numbers):
	alphabet_w_cap = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	for a in range(1, 100):

		for b in range(1, 100):
			decoded_string = ''
			fin_answer = []
			x = 0
			for item in numbers:
				decoded_number = (item - b)/a
				if decoded_number.is_integer() == True and decoded_number >= 0 and decoded_number <=52:
					fin_answer.append(decoded_number)
					x +=1
					if x == len(numbers):
						for letter in fin_answer:
							decoded_string += alphabet_w_cap[int(letter)]
						print(decoded_string)
						
				else:
					x = 0
					fin_answer = []

	
bruteforce([377, 717, 71, 513, 105, 921, 581, 547, 547, 105, 377, 717, 241, 71, 105, 547, 71,377, 547, 717, 751, 683, 785, 513, 241, 547, 751])
	



def bisection_search(number,power,precision):
	lower = 0
	upper = number + 1
	while (upper - lower) >= 1 / (10 **(precision)):
		if ((lower + upper) / 2) ** (power) > number:
			upper = (lower + upper) / 2
		elif ((lower + upper) / 2) ** (power) < number:
			lower = (lower + upper) / 2
		elif ((lower + upper)/2) ** (power) == number:
			return ((lower + upper) / 2)
	return ((lower + upper)/2)



class Stacks:


	def __init__(self,numbers):
		self.numbers = numbers


	def print(self):
		final = ''
		numbers_reversed = self.numbers[::-1]
		for item in numbers_reversed:
			final += str(item)
		return final


	def push(self,new_number):
		self.numbers.append(new_number)
		return self.numbers


	def pop(self):
		x = self.numbers[-1]
		self.numbers = self.numbers[0 : len(self.numbers) - 1]
		print("new array is " + str(self.numbers))
		return x


class Queue:


	def __init__(self,numbers):
		self.numbers = numbers


	def print(self):
		final = ''
		numbers_reversed = self.numbers[::-1]
		for item in numbers_reversed:
			final += str(item)
		return final


	def enqueue(self,new_number):
		self.numbers.append(new_number)
		return self.numbers


	def dequeue(self):
		x = self.numbers[-1]
		self.numbers = self.numbers[0:len(self.numbers)-1]
		print("new array is " + str(self.numbers))
		return x
		



def calc_minimum(numbers):
	a = numbers[0]
	for item in numbers:
		if item < a:
			a = item
	return a



def simple_sort(numbers):
	fin_list = []
	while len(numbers) != 0:
		fin_list.append(calc_minimum(numbers))
		numbers.remove(calc_minimum(numbers))
	return fin_list
