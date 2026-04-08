def Findbiggestnumber(Array):     
    firstvalue = Array[0]
    for i in range(1,len(Array)):
        if Array[i] > firstvalue:
            firstvalue = Array[i]
    return firstvalue

Array = [1,2,3,4,5,6,99,8,9,10]
print(Findbiggestnumber(Array))