def merge(a,b):

	andx = 0 
	bndx = 0 
	final_array = []
	while len(final_array) < (len(a) + len(b)):

		if andx == len(a) :
			final_array.extend(b[bndx:len(b)])
		elif bndx == len(b):
			final_array.extend(a[andx:len(a)])

		elif a[andx] <= b[bndx]:
			final_array.append(a[andx])
			andx += 1
		else:
			final_array.append(b[bndx])
			bndx += 1
	return final_array




def split(input):
	halfpoint = int(len(input)/2)
	first_half = input[:halfpoint]
	second_half = input[halfpoint:]
	return first_half,second_half

print(merge([2,3,4,5,6],[1,9,10,21,34]))
print("hi")
print("hi")