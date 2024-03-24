def seqSearch(x, N, searchValue):
    
    i = 0
    
    while (i<(N-1)) and (x[i] != searchValue):
        i+=1
    
    if (x[i] == searchValue):
        return i
    else:
        return -1

def readArray(x, N):
    for i in range(0, N):
        read = int(input(f"nilai ke-{i+1} = "))
        x.append(read)
        
def res(x):
    for i in x:
        print(x)
