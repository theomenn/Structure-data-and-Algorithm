def appendElement(x, N, searchValue,idx):
    
    if (idx != -1):
        print('element sudah ada didalam array.')
    else:
        print(f'{searchValue} belum terdapat didalam array, menambahkan {searchValue} pada posisi ke-{N+1}...')
        N = N + 1
        x.append(searchValue)
        print(x)
        print("berhasil menambahkan array!")


def readArray(x, N):
    for i in range(0, N):
        read = int(input(f"nilai ke-{i+1} = "))
        x.append(read)