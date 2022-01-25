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
    # A is our augmented matrix
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

def find_inverse(X,n):
    I = np.identity(n)
    print(I)
    A = np.hstack((X,I))           
    # A is our augmented matrix
    # parial pivoting
    for iteration in range(n):
        # first we will perform pivoting procedure
        print("For iteration: ", iteration)
        max_start_row = -1e9
        max_row_index=0
        for row in range(iteration,n):
            if(abs(A[row,iteration])> max_start_row):
                #print("m:", max_start_row)
                max_start_row = abs(A[row,iteration])
                max_row_index = row
        print(f"R{iteration} <--> R{max_row_index}")
        A[[iteration,max_row_index]] = A[[max_row_index,iteration]]
        # making pivot element =1 
        if(A[iteration,iteration] != 0):
            print(f"R{iteration} -> R{iteration} / {A[iteration,iteration]}")
            A[iteration] = A[iteration] / A[iteration,iteration]
            
        for row in range(0,n):
            if(row == iteration):
                #i.e. same row as pivot entry we just continue
                continue
            print(f"R{row} ---> R{row} -  R{iteration} * {A[row,iteration]} ")
            A[row] -= A[iteration] * A[row,iteration] 
        print(A)
        print("\n!------------------------------------------------------!\n")
    print(A)
    return np.hsplit(A,[n,2*n])[1]
        
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
        
def main():
    mat = matrix_input('matrix.txt')
    m,n = mat.shape
    print("Dimensison: ",m,n)
    if(m!=n):
        print("Inverse of non-square matrix is not possible")
    print("\nsolution:\n!------------------------------------------------------!\n")
    X = find_inverse(mat,n)
    print("Inverse of: \n" ,mat,"\nis: \n",X)
    
    
if __name__ == '__main__':
    main()