# 1 major flaw, we dont account for the possbility, that a field has to be a specific number because all other possbilities are ruled out
# check heuristics
# Heuristic 1 implemented? 
# max heuristic 2 machen
# https://dingo.sbs.arizona.edu/~sandiway/sudoku/examples.html

import numpy as np

Sudoku = [
    [0, 2, 0, 6, 0, 8, 0, 0, 0],
    [5, 8, 0, 0, 0, 9, 7, 0, 0],
    [0, 0, 0, 0, 4, 0, 0, 0, 0],
    [3, 7, 0, 0, 0, 0, 5, 0, 0],
    [6, 0, 0, 0, 0, 0, 0, 0, 4],
    [0, 0, 0, 0, 0, 0, 0, 0, 4],
    [0, 0, 8, 0, 0, 0, 0, 1, 3],
    [0, 0, 0, 0, 2, 0, 0, 0, 0],
    [0, 0, 0, 3, 0, 6, 0, 9, 0]
]

M = np.array(Sudoku)

#define submatrices
A = M[0:3 , 0:3]
B = M[0:3 , 3:6]
C = M[0:3 , 6:9]
D = M[3:6 , 0:3]
E = M[3:6 , 3:6]
F = M[3:6 , 6:9]
G = M[6:9 , 0:3]
H = M[6:9 , 3:6]
I = M[6:9 , 6:9]

possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9]
given_nr = []
Sudoku_solved = False

while(not Sudoku_solved):
    for i in range(0, 9):
        for j in range(0, 9):
            if M[i][j] == 0:

                #append the corresponding row to the given numbers
                row = M[i]
                for element in row:
                    if element != 0:
                        given_nr.append(element)

                #append the corresponding column to the given numbers
                for x in range(0, 9):
                    if M[x][j] != 0:
                        given_nr.append(M[x][j])

                #determine the corresponding submatrix
                if 0 <= i <3:
                    if 0 <= j <3:
                        submatrix = A
                    elif 3 <= j <6:
                        submatrix = B
                    elif 6 <= j <9:
                        submatrix = C

                if 3 <= i <6:
                    if 0 <= j <3:
                        submatrix = D
                    elif 3 <= j <6:
                        submatrix = E
                    elif 6 <= j <9:
                        submatrix = F

                if 6 <= i <9:
                    if 0 <= j <3:
                        submatrix = G
                    elif 3 <= j <6:
                        submatrix = H
                    elif 6 <= j <9:
                        submatrix = I

                #append the corresponding submatrix to the given numbers
                for k in range(0, 3):
                    for l in range(0, 3):
                        if submatrix[k][l] != 0:
                            given_nr.append(submatrix[k][l])

                for element in given_nr:
                    try:
                        possibilities.remove(element)
                    except ValueError:
                        pass

                if len(possibilities) == 1:
                    M[i][j] = possibilities[0]
                    print(str(i) + ', ' +  str(j))
                    print(M)

#redefine submatrices

                    A = M[0:3 , 0:3]
                    B = M[0:3 , 3:6]
                    C = M[0:3 , 6:9]
                    D = M[3:6 , 0:3]
                    E = M[3:6 , 3:6]
                    F = M[3:6 , 6:9]
                    G = M[6:9 , 0:3]
                    H = M[6:9 , 3:6]
                    I = M[6:9 , 6:9]

                possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                given_nr = []
                
#check if matrix solved

                if np.count_nonzero(M) == 81:
                    Sudoku_solved = True

print('Solved!')
print(M)