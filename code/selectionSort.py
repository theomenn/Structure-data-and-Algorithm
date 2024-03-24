def selectionSort(x, N):
    for i in range(N-1, 0, -1):
        imaks = 0
        maks = x[0]

        for j in range(i+1):  
            if x[j] > maks:
                imaks = j
                maks = x[j]

        
        temp = x[i]
        x[i] = maks
        x[imaks] = temp
    
    return x


def readArray(x, N):
    for i in range(N):
        read = int(input(f"nilai ke-{i+1} =  "))
        x.append(read)
