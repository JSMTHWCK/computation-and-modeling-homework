from help import *
def merge_sort(input):
    if len(input) > 1:
        firsthalf,secondhalf = split(input)
        sortfirst = merge_sort(firsthalf)
        sortsecond = merge_sort(secondhalf)
        sortedfirst = merge_sort(firsthalf)
        sortedsecond = merge_sort(secondhalf)
        
        return merge(sortedfirst, sortedsecond)
    else:
        return input

print(merge_sort([2,3,4,1,5,6,7]))