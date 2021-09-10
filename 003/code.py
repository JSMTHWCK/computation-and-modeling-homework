#couldn't get import to work
def calc_minimum(numbers):
	a = numbers[0]
	for item in numbers:
		if item < a:
			a = item
	return a
def calc_maximum(numbers):
	a = numbers[0]
	for item in numbers:
		if item > a:
			a = item
	return a

def swap_sort(numbers):
	for a in range (0,len(numbers)):
		for item in range(1,len(numbers) - 1):
			if numbers[item] < numbers [item - 1]:
				numbers[item],numbers[item-1] = numbers[item - 1], numbers[item]
			else:
				continue
	return numbers

def tally_sort(numbers):

	shift = calc_minimum(numbers)
	tally_list = []
	sorted_list = []

	for item in range(0,len(numbers)):

		numbers[item] = numbers[item] - shift

	tally_length = calc_maximum(numbers)

	for item in range(0,tally_length + 1):
		
		tally_list.append(0)

	for item in numbers:

		tally_list[item] += 1 

	for item in range(0,tally_length +1):

		x = [item] * tally_list[item]
		sorted_list.extend(x)

	for item in range(0,len(numbers)):

		sorted_list[item] = sorted_list[item] + shift

	return sorted_list

def card_sort(numbers):
	for n in numbers:
		for item in range(0, len(numbers)):
			if item > 0:
				while numbers[item] < numbers[item - 1]:
					numbers[item], numbers[item - 1] = numbers[item - 1], numbers[item]
	return numbers

	
print(swap_sort([13,7,25,2,105]))
print(tally_sort([13,7,25,2,105]))
print(card_sort([13,7,25,2,105]))
print("hi")