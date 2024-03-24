def matrikA(A, m, p):
    for i in range(m):
        for j in range(p):
            print(f"inputkan matrik A ke - {i}, {j}:")
            A[i][j] = int(input())

def matrikB(B, m, p):
    for i in range(m):
        for j in range(p):
            print(f"inputkan matrik B ke - {i}, {j}:")
            B[i][j] = int(input())
            
def initElemen(C,m,p):
    for i in range(m):
        for j in range(p):
            C[i][j] =  0
            
                
def perkalianMatrik(A, B, C, m, p, n):    
    for i in range(0, m):
        for j in range(0, p):
            for k in range(0, n):
                C[i][j] += A[i][k] * B[k][j] 
                
def matrikC(C, m, p):
    for i in range(0, m):
        for j in range(0, p):
            print(C[i][j], end=" ")
        print(" ")