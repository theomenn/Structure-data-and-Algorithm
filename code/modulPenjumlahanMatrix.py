def bacaMatrikA(A, nBar, nKol):
    for i in range(0, nBar):
        for j in range(0, nKol):
            print(f"inputkan matrik A ke - {i}, {j}:")
            A[i][j] = int(input())

def bacaMatrikB(B, nBar, nKol):
    for i in range(0, nBar):
        for j in range(0, nKol):
            print(f"inputkan matrik B ke - {i}, {j}:")
            B[i][j] = int(input())
            
def cetakMatrikC(C, nBar, nKol):
    for i in range(0, nBar):
        for j in range(0, nKol):
            print(C[i][j], end=" ")
        print(" ")
        
def penjumlahanMatrik(A, B, C,nbar, nKol):
    for i in range(0, nbar):
        for j in range(0, nKol):
            C[i][j]= A[i][j] + B[i][j]
