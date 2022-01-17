from help import *
def merge_sort(input):
    #print("input list is ", input)
    if len(input) > 1:
        firsthalf,secondhalf = split(input)
        sortfirst = merge_sort(firsthalf)
        sortsecond = merge_sort(secondhalf)
        print("sortfirst is ", sortfirst)
        print("sortsecond is ", sortsecond)
        #print("merge between {} and {} is {} ".format(sortfirst,sortsecond,merge(sortfirst,sortsecond)))
        return merge(sortfirst, sortsecond)
    else:
        #print("input is ", input)
        return input

a = [55,80,100,75,67,89,24,71,32,42]
merge_sort(a)