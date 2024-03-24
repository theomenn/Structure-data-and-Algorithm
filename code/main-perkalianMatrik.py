import modulPerkalianMatrik as mpk

def main():
    m = int(input("inputkan jumlah baris A =  "))
    n = int(input("inputkan jumlah kolom A dan baris B =  "))
    p = int(input("inputkan jumlah kolom B = "))
    
    A = [[0 for col in range(n)] for row in range(m)]
    B = [[0 for col in range(p)] for row in range(n)]
    C = [[0 for col in range(p)] for row in range(m)]
    
    mpk.matrikA(A, m, n)  
    mpk.matrikB(B, n, p)  
    mpk.initElemen(C, m, p)
    mpk.perkalianMatrik(A, B, C, m, p, n)
    
    print("hasil perkalian matrik A  dan B adalah: ")
    mpk.matrikC(C, m, p)

if __name__ == "__main__":
    main()
