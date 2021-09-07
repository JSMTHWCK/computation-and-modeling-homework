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
							decoded_string += ' ' + str(int(letter))
							print(b)
							print(a)
						return decoded_string
						break
				else:
					x = 0
					fin_answer = []

	

print(bruteforce([377, 717, 71, 513, 105, 921, 581, 547, 547, 105, 377, 717, 241, 71, 105, 547, 71,377, 547, 717, 751, 683, 785, 513, 241, 547, 751]))

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



def calc_minimum(numbers):
	a = numbers[0]
	for item in numbers:
		if item < a:
			a = item
	return a

print(calc_minimum([7,3,6,1,8]))