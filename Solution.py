
def surfaceArea(A):
    # Write your code here
    matrices = []
    B = []
    area = 0
    for idx,row in enumerate(A):
        B.append([])
        for idx2,col in enumerate(row):
            B[idx].append(col)
    matrices.append(B)
    
    while(not allzero(A)):
        for idx,row in enumerate(A):
            for idx2,col in enumerate(row):
                if A[idx][idx2] != 0:
                    A[idx][idx2] = A[idx][idx2] - 1
        B = []
        for idx,row in enumerate(A):
            B.append([])
            for idx2,col in enumerate(row):
                B[idx].append(col)
        matrices.append(B)
    
    for matrix in matrices:
        for row in matrix:
            for col in row:
                if col > 0:
                    area = area + 6
    
    print(area)
    
    for matrix in matrices:
        for row in matrix:
            for idx,_ in enumerate(row):
                if idx < len(row) -1:
                    if row[idx] > 0 and row[idx+1] > 0:
                        area = area - 2
    
    print(area)
    
    rowlen = len(A)
    collen = len(A[0])
    for matrix in matrices:
        for rowi,row in enumerate(matrix):
            for coli,item in enumerate(row):
                if rowi < len(matrix) - 1:
                    if matrix[rowi][coli] > 0 and matrix[rowi+1][coli]>0:
                        area = area - 2
        
    print(area)
    
    rowlen = len(A)
    collen = len(A[0])
    
    for idx,_ in enumerate(matrices):
        if idx < len(matrices)-1:
            for row in range(rowlen):
                for col in range(collen):
                    if matrices[idx][row][col] > 0 and matrices[idx+1][row][col] > 0:
                        area = area - 2
    print(area)
    print(matrices)
    
    return area

def allzero(A):
    result = True
    for row in A:
        for item in row:
            if item != 0:
                result = False
                break
    
    return result
