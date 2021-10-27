def merge(a,b):
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
    first_half = []
    last_half = []
    for i in range(0,int(len(input)/2)):
        first_half.append(input[i])
    for item in range(i+1,len(input)):
        last_half.append(input[item])
    return first_half,last_half
