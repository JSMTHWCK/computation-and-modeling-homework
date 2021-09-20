def rhapson(x, n, precision):
	x_new = None
	x_old = x
	while precision > 0:
		fx = (x_old ** n) - x
		fix = n * (x_old ** (n - 1))
		x_new = x_old - fx/fix
		x_old = x_new

		precision -= 1
		print(precision)
	return x_new 



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

print(rhapson(2,2,5))
print(merge([2,3,4,5,6],[1,9,10,34,21]))
