def swap_sort(numbers):
	old_numbers = []
	forever = 1
	cashe_num = 0
	while forever == 1:
		print(old_numbers)
		for item in range(0,len(numbers) - 1):
			print(str(item) + " item")
			print(numbers[item])
			if numbers[item] > numbers[item + 1]:
				numbers[item] = cashe_num
				
		if old_numbers == numbers:
			return numbers
			break
		else:
			old_numbers = numbers

print(swap_sort([1,3,5,6,7,3,2]))
