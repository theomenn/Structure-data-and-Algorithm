import modulPenjumlahanMatrix as mpm

def main():
    nBar = int(input("inputkan nilai N Baris=  "))
    nKol = int(input("inputkan nilai N Kolom=  "))
    
    A= [[0 for row in range(0,nBar)] for col in range(0,nKol)]
    B= [[0 for row in range(0,nBar)] for col in range(0,nKol)]
    C= [[0 for row in range(0,nBar)] for col in range(0,nKol)]
    
    mpm.bacaMatrikA(A, nBar, nKol)
    mpm.bacaMatrikB(B, nBar, nKol)
    mpm.penjumlahanMatrik(A,B,C,nBar,nKol)
    print("hasil penjumlahan adalah matrik C: ")
    mpm.cetakMatrikC(C, nBar, nKol)
    
if __name__ == "__main__":
    main()