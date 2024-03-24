import insertSort as iss

def main():
    x = []
    N = int(input('masukkan panjang larik = '))   
    
    iss.readArray(x, N)
    n = N - 1
    step = n

    while(step>1):
        step = int((step/3))+1
        for start in range(0, step+1):
            iss.insertSort(x,N)
            # iss.insSort(x,N,start,step)
            
    iss.printArray(x)
    
if __name__ == "__main__":
    main()