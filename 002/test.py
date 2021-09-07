from code import*
import math
if decode(encode("word",3,7),3,7) != "word":
	print('encode failed on input "word"')
if decode(encode("pinapple",6,10),6,10) != "pinapple":
	print('encode failed on input "pinapple"')

if encode(decode([4,1,8,9],1,2),1,2) != [4,1,8,9]: #4,1,8,9 doesn't translate to anything
	print('decode failed on input "[4,1,8,9]"')
if encode(decode([6,5,4,3,2],8,2),8,2) != [6,5,4,3,2]:
	print('decode failed on input "[6,5,4,3,2]"')

if math.isclose(math.sqrt(3), bisection_search(3,2,5), abs_tol = 0.00001) != True:
	print('bisection_search failed on input "3**1/2"')
if math.isclose(10**(1./3.), bisection_search(10,3,9), abs_tol = 0.5) != True:
	print('bisection_search failed on input "10**1/3"')

n1 = stacks([1,2,3,4,5,6])
if n1.print() != "654321":
	print("stack print failed on n1")
if n1.push(8) != [1,2,3,4,5,6,8]:
	print("stack push failed on n1")
if n1.pop() != 8:
	print("stack pop failed on n1")
	
n2 = queue([1,2,3,4,5,6])
if n2.print() != "654321":
	print("stack print failed on n1")
if n2.enqueue(8) != [1,2,3,4,5,6,8]:
	print("stack push failed on n1")
if n2.dequeue() != 8:
	print("stack pop failed on n1")
	