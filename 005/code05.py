from help import *
def merge_sort(input):
    if len(input) > 1:
        firsthalf,secondhalf = split(input)
        sortfirst = merge_sort(firsthalf)
        sortsecond = merge_sort(secondhalf)

    else:
        print(input)

print(merge_sort([1,2,3,4,5,6,7]))