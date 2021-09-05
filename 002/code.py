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



class stacks:
	def __init__(self,numbers):
		self.numbers = numbers

	
	def print(self):
		numbers_reversed = self.numbers[::-1]
		print(*numbers_reversed, sep = ' ')

	def push(self,new_number):
		self.numbers.append(new_number)
		return self.numbers

	def pop(self):
		x = self.numbers[-1]
		self.numbers = self.numbers[0:len(self.numbers)-1]
		print("new array is " + str(self.numbers))
		return x
n1 = stacks([1,2,3,4,5,6])

class queue:
	def __init__(self,numbers):
		self.numbers = numbers
		
	def print(self):
		numbers_reversed = self.numbers[::-1]
		print(*numbers_reversed, sep = ' ')

	def enqueue(self,new_number):
		self.numbers.append(new_number)
		return self.numbers

	def dequeue(self):
		x = self.numbers[-1]
		self.numbers = self.numbers[0:len(self.numbers)-1]
		print("new array is " + str(self.numbers))
		return x
n2 = queue([1,2,3,4,5,6])

n1.print()
print(n1.push(8))
#it's popping out the 8 from last question
print(n1.pop())

n2.print()
print(n2.enqueue(8))
#it's popping out the 8 from last question
print(n2.dequeue())