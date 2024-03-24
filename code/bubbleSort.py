def bubleSort(x, N):
    for i in range(0, N):
        for k in range(N-1, i, -1):
            if (x[k] < x[k-1]):
                temp = x[k]
                x[k] = x[k-1]
                x[k-1] = temp

def readArray(x, N):
    for i in range(0, N):
        read = int(input(f"nilai ke-{i+1} = "))
        x.append(read)




