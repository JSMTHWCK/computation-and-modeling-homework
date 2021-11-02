def merge(a,b):
	if a == None:
		return b
	if b == None:
		return a
	andx = 0 
	bndx = 0 
	final_array = []
	while andx <= len(a) - 1 and bndx <= len(b) - 1:
		if a[andx] <= b[bndx]:
			final_array.append(a[andx])
			andx += 1
		elif a[andx] > b[bndx]:
			final_array.append(b[bndx])
			bndx += 1

	if andx > bndx :
		final_array.extend(b[bndx:len(b)])
	elif bndx < andx:
		final_array.extend(a[andx:len(a)])
	return final_array

def split(input):
	halfpoint = int(len(input)/2)
	first_half = input[:halfpoint]
	second_half = input[halfpoint:]
	print(first_half)
	print(second_half)
split([1,2,3,4,5,6,7,8])
