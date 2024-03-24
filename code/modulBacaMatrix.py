def bacaMatrix(matrik,nBar,nKol):
        for i in range(0,nBar):
            for j in range(0,nKol):
                print(f"inputkan larik ke {i}, ke {j}:")
                matrik[i][j]= int(input())


def cetakMatrik(matrik, nBar, Nkol):
    for i in range(0,nBar):
        for j in range(0,Nkol):
            print(matrik[i][j], end=" ")
        print(" ")