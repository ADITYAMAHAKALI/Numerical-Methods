import numpy as np
import math 
import random

def matrix_input(filename):
    file = open(filename,'r')
    i=0
    mat =[]
    for line in file:
        row =[]
        nums = line.split(' ')
        
        for num in nums:
            row.append(float(num))
        mat.append(row)
    file.close()
    return np.array(mat)

def to_reduced_row_echleon(X,m,n):
    # X is our augmented matrix
    # parial pivoting
    for iteration in range(m):
        # first we will perform pivoting procedure
        print("For iteration: ", iteration)
        max_start_row = -1e9
        max_row_index=0
        for row in range(iteration,m):
            if(abs(X[row,iteration])> max_start_row):
                #print("m:", max_start_row)
                max_start_row = abs(X[row,iteration])
                max_row_index = row
        print(f"R{iteration} <--> R{max_row_index}")
        X[[iteration,max_row_index]] = X[[max_row_index,iteration]]
        
        if(X[iteration,iteration] != 0):
            print(f"R{iteration} -> R{iteration} / {X[iteration,iteration]}")
            X[iteration] = X[iteration] / X[iteration,iteration]
            
        for row in range(0,m):
            if(row == iteration):
                #i.e. same row as pivot entry we just continue
                continue
            print(f"R{row} ---> R{row} -  R{iteration} * {X[row,iteration]} ")
            X[row] -= X[iteration] * X[row,iteration] 
        print(X)
        print("\n!------------------------------------------------------!\n")
    return X
            
def nullity(A):
    iteration = (A.shape)[1] -1
    row = (A.shape)[0] -1
    n =0
    while(iteration>=0):
        if(A[row,iteration] ==0 ): 
            n+=1
        iteration-=1
        row-=1
    return n   

def checkB(B):
    rows = (B.shape)[0] -1
    n=0
    while rows>=0:
        if B[rows,0] ==0:
            n+=1
            rows-=1
        else:
            return n 
    return n
        
def find_solution(A,B):
    # no_of_variables
    variables = (A.shape)[1]
    solution = np.zeros([variables,1])
    nullityA = nullity(A)
    # print(n)
    rankA = variables - nullityA 
    nullityB = checkB(B)
    rankAB = max(rankA,variables - nullityB)
    # homogeneous case
    if(nullityB == variables):
        # we wil get trivial solution i.e. value of all variables is zero 
        return solution
    # non-homogeneous case
    else:
        # if rankA == rankAugmented MAtrix and is equal to number of variables
        # we will get unique solution
        if rankA == rankAB and rankA == variables:
            k=variables-1
            solution = B
        
        # infinite solution case
        elif rankA == rankAB and rankA != variables:
            k=variables-1
            solution = B
            print(f"We have infinite solutions in this case with {int(nullityA)} free variables")
            print("Below is one of the possible solutions of the system")
            return solution
        # no solution case  
        elif rankA < rankAB:
            print("No solution exist rank A < rank Augmented matrix")
    # print(rank_Augmented)
    # if rank == n we will have unique solution
    # elif rank < n        
    return solution

def main():
    mat = matrix_input('matrix.txt')
    print("\n\nAugmented Matrix [A:B]\n",mat)
    #initialisng dimension of the matrix
    m,n = mat.shape
    print("Dimensison: ",m,n)
    print("\nsolution:\n!------------------------------------------------------!\n")
    X = to_reduced_row_echleon(mat,m,n)
    # X is an upper triangular augmented matrix 
    # A is from col 0,m-1;  B is last column 
    C = np.hsplit(X,[n-1,n])
    A = C[0]
    B = C[1]
    print("A:\n",A)
    print("B:\n",B)
    # total variables in solution = n-1 
    print("Solution: \n",find_solution(A,B))    
    
    
if __name__ == '__main__':
    main()