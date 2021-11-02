from code05 import *

a = [55,80,100,75,67,89,24,71,32,42]
b = [7,50,99,70,84,42,61,56,24,73]
c = [89,77,77,100,90,3,52,68,34,83]

if merge_sort(a) != [24, 32, 42, 55, 67, 71, 75, 80, 89, 100]:
    print("merge sort failed on ", a)
    print(merge_sort(a))
if merge_sort(b) != [7, 24, 42, 50, 56, 61, 70, 73, 84, 99]:
    print('merge sort failed on ', b)
if merge_sort(c) != [3, 34, 52, 68, 77, 77, 83, 89, 90, 100]:
    print("merge sort failed on ", c)

print('hi')