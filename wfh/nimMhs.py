def nimSearch(nims, n, searchValue):
    i = 0
    found = False
    while(i <= n) and (not found):
        if nims[i] == searchValue :
            found = True
            return i
            
        else:
            return -1


def readArray(x, N):
    for i in range(0, N):
        read = int(input(f"nilai ke-{i+1} = "))
        x.append(read)
