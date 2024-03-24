def binarySearch(x, N, searchValue):
    
    i = 0
    j = N
    found = False
    
    while (not found) and (i <=j):
        k = (int((i + j)/2))
    
        if (x[k] == searchValue):
            found = True
        else:
            if(x[k] > searchValue):
                i = k + 1
            else :
                j = k - 1
    print(i,j,k)
    return found


def readArray(x, N):
    for i in range(0, N):
        read = int(input(f"nilai ke-{i+1} = "))
        x.append(read)
