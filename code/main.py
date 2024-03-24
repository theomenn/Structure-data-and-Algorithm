# MAIN PROGRAM

# import addElement as ae
# import seqSearch as qs
# import binarySearch as bs
# import bubbleSort as bbs
# import selectionSort as ss 

import insertSort as iss


def main():
    x = []
    N = int(input('masukkan panjang larik = '))    


    # selection sort
    # ss.readArray(x, N)
    # print(ss.selectionSort(x,N))
    
    
    # add element to array 
    # searchValue = int(input('masukkan nilai yang ingin dicari = '))
    # idx = qs.seqSearch(x,N,searchValue)
    # ss.appendElement(x, N, searchValue, idx)
    
    
    # insertSort
    iss.readArray(x, N)
    n = N - 1
    step = n

    while(step>1):
        step = int((step/3))+1
        for start in range(0, step+1):
            iss.insertSort(x,N)


    print(x)
if __name__ == "__main__":
    main()