import modulBacaMatrix as mbm

def main():
    nBar = int(input("inputkan nilai N baris: "))
    nKol = int(input("inputkan nilai N kolom: "))
    
    matrik =[[0 for row in range(0,nBar)] for col in range(0,nKol)]
    
    mbm.bacaMatrix(matrik, nBar, nKol)
    mbm.cetakMatrik(matrik, nBar, nKol)
    
if __name__ == "__main__":
    main()