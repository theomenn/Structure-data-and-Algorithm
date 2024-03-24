def insertSort(x, N):
    for i in range(1, N):
        y = x[i]
        j = i - 1
        ketemu = False
        
        while(j>=0) and (not ketemu):
            if(y<x[j]):
                x[j+1] = x[j]
                j = j -1
            else:
                ketemu = True
        x[j+1]=y
        
def insSort(x,N,start,step):
    i = start + step
    n = N-1
    
    while(i<=n):
        y = x[i]
        j = i - step
        ketemu = False
        
        while(j>=0) and (not ketemu):
            if(y<x[j]):
                x[j+step] = x[j]
                j = j - step
            else:
                ketemu = True
                
        x[j+step]=y
        i+=step
        
def readArray(x, N):
    for i in range(N):
        read = int(input(f"nilai ke-{i+1} =  "))
        x.append(read)
        
def printArray(x):
    for i in x:
        print(i, end=" ")