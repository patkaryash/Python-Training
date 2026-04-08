def binarySearch(array, target):
    start = 0
    end = len(array)-1 
    while start <=end:
        mid = (start+end)//2
        if array[mid] == target:
            return mid
        elif array[mid]< target:
            start = mid+1
        else:
            end= mid-1
    return -1
        
    
sortedArray= [1,2,3,4,5,6,7,8,9]
target = 55
result = binarySearch(sortedArray, target)
if result == -1:
    print("Not found")
else:
    print("Element found at index: ")