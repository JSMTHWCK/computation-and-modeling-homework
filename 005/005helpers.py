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