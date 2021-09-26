# HackerRank-3D-Surface-Area
I want to add my comment at discussion tab:

"""

This question looks really hard at first but when you realise that you need to think from bottom to up, it gets really easy.Let me tell you about my solution and give code of it.

![](https://prnt.sc/1tpx631)

At first let's just build our toy from bottom to up and let's consent surface area of each block as 6.
And you can see that I omit 1 from every cell if it's not 0, basically i am spending my blocks to build 3d toy.

What now ? We will omit the adjacent surfaces and we will do it in 3 parts!
First adjacent rows at the same layer(area -= 2 if both adjacent(horizantally) cell bigger than 0(not empty)).
2-Adjacent columns at the same layer.
3-Adjacent tops between layers.



```python
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
		
````

"""
