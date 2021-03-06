from code import*
import math
if decode(encode("word",3,7),3,7) != "word":
	print('encode or decode failed on input "word"')
if decode(encode("pinapple",6,10),6,10) != "pinapple":
	print('encode or decode on input "pinapple"')


bruteforce([377, 717, 71, 513, 105, 921, 581, 547, 547, 105, 377, 717, 241, 71, 105, 547, 71,377, 547, 717, 751, 683, 785, 513, 241, 547, 751])



if math.isclose(math.sqrt(3), bisection_search(3,2,5), abs_tol = 0.00001) != True:
	print('bisection_search failed on input "3**1/2"')
if math.isclose(10**(1./3.), bisection_search(10,3,9), abs_tol = 0.5) != True:
	print('bisection_search failed on input "10**1/3"')

n1 = Stacks([1,2,3,4,5,6])
if n1.print() != "654321":
	print("stack print failed on n1")
if n1.push(8) != [1,2,3,4,5,6,8]:
	print("stack push failed on n1")
if n1.pop() != 8:
	print("stack pop failed on n1")
	
n2 = Queue([1,2,3,4,5,6])
if n2.print() != "654321":
	print("stack print failed on n1")
if n2.enqueue(8) != [1,2,3,4,5,6,8]:
	print("stack push failed on n1")
if n2.dequeue() != 8:
	print("stack pop failed on n1")
	
if calc_minimum([1,2,3,4,5,6]) != 1:
	print('calc_minimum failed on "[1,2,3,4,5,6]"')
if calc_minimum([100,254,3,489,183]) != 3:
	print('calc_minimum failed on "[100,254,3,489,183]"')

if simple_sort([1,2,3,4,5,6]) != [1,2,3,4,5,6]:
	print('simple_sort failed on "[1,2,3,4,5,6]"')
if simple_sort([100,254,3,489,183]) != [3,100,183,254,489]:
	print('simple_sort failed on "[100,254,3,489,183]"')