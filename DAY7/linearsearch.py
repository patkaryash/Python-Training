def linearSearch(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1

array = [1,2,3,4,5,6,7,8,9]
target = 4
result = linearSearch(array, target)
if result == -1:
    print("Not found")
else:
    print("Element found at index no=",result)