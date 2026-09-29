def RecursiveCount(ArrayCopy, NumberElements, DataToFind):
    global total
    num = 0
    

    Copy = ArrayCopy.copy()

    if len(Copy) == 0:
        return 0

    if Copy[0] == DataToFind:
        # You are currently overwriting the array with the popped value.
        # The goal is to pop the first value leaving the rest of the array unchanged
        for i in range(1,len(Copy)):
            Copy[i-1] = Copy[i]
        del Copy[-1]
        # Alternatively, think about how you can fill an empty array with the right values using a for loop
        return 1 + RecursiveCount(Copy, NumberElements-1, DataToFind)
    else:
        for i in range(1,len(Copy)):
            Copy[i-1] = Copy[i]
        del Copy[-1]
        return RecursiveCount(Copy, NumberElements-1, DataToFind)

ArrayCopy = [0,5,1,2,5,9,9,6,5,0]
total = 0
print(RecursiveCount(ArrayCopy, 10, 0))