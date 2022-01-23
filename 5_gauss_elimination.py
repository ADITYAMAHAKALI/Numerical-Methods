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

def to_echleon(X,m,n):
    # X is our augmented matrix
    # we need to insure that first three columns of X has one leading entry
    
    for iteration in range(m):
        print("\niteration: ", iteration)
        # first we will perform pivoting procedure
        max_start_row = -1e9
        max_row_index=0
        for row in range(iteration,m):
            if(abs(X[row,iteration])> max_start_row):
                #print("m:", max_start_row)
                max_start_row = abs(X[row,iteration])
                max_row_index = row
        print(f"R{iteration} <--> R{max_row_index}")
        X[[iteration,max_row_index]] = X[[max_row_index,iteration]]
        #print("max_pivot form:\n",X)
        # now we will zero the elements below our pivot
        if(X[iteration,iteration] != 0):
            for i in range(iteration+1,m):
                #print(f"Checking {i}th row")
                if(X[i,iteration]==0):
                    continue
                else:
                    print(f"R{i} ---> R{i} + ({X[i,iteration]}) * (R{iteration} / {(X[iteration,iteration])})")
                    X[i] = X[i] - X[i,iteration]*(X[iteration] / (X[iteration,iteration]))
        print("X:\n",X)
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
    print(solution.shape)
    print(solution)
    nullityA = nullity(A)
    # print(n)
    rankA = variables - nullityA 
    nullityB = checkB(B)
    rankAB = max(nullityA,variables - nullityB)
    # homogeneous case
    if(nullityB == variables):
        # we wil get trivial solution i.e. value of all variables is zero 
        return solution
    # non-homogeneous case
    else:
        # if rankA == rankAugmented MAtrix and is equal to number of variables
        # we will get unique solution
        if rankA == rankAB and rankA == variables:
            # we need to loop from backwards
            k=variables-1
            rows = (A.shape)[0] -1
            while(k>=0):
                #
                if(A[rows,k] ==0 ):
                    solution[k,0] =0
                    continue 
                    # here the coeffiecient of variable or the diagonal element is zero 
                    # so the value of this variable can be considered as zero
                solution[k,0] = B[k,0]
                print(f"x{k} = {B[k,0]}")
                j=variables -1 # index start from zero 
                while(j>k):
                    print(f"x{k} = x{k} -  {round(solution[k+1,0],6)} * {A[rows,j]}")
                    solution[k,0]-= solution[j,0] * A[rows,j]
                    j-=1
                
                solution[k,0] =  solution[k,0] / A[rows,k]
                print(f"x{k} =  {solution[k,0]} / {A[rows,k]}")
                #print(solution)
                k-=1
                rows-=1
              
        # infinite solution case
        elif rankA == rankAB and rankA != variables:
            # here we will have some free variables
            # number of free variables = nullityA
            fv = nullityA 
            # for these free variables we need to assign some random value
            k=variables-1
            rows = (A.shape)[0] -1
            while(fv>0):
                solution[k,0] = random.randint(-10,10)
                print(solution[k,0])
                fv-=1
                k-=1
                rows-=1
            while(k>=0):
                #
                if(A[rows,k] ==0 ):
                    solution[k,0] =0
                    continue 
                    # here the coeffiecient of variable or the diagonal element is zero 
                    # so the value of this variable can be considered as zero
                solution[k,0] = B[k,0]
                print(f"x{k} = {B[k,0]}")
                j=variables -1 # index start from zero 
                while(j>k):
                    print(f"x{k} = x{k} -  {round(solution[k+1,0],6)} * {A[rows,j]}")
                    solution[k,0]-= solution[j,0] * A[rows,j]
                    j-=1
                
                solution[k,0] =  solution[k,0] / A[rows,k]
                print(f"x{k} =  {solution[k,0]} / {A[rows,k]}")
                #print(solution)
                k-=1
                rows-=1
            print(f"We have infinite solutions in this case with {int(nullityA)} free variables")
            print("Below is one of the possible solutions of the system")
            return solution
            
        elif rankA < rankAB:
            print("No solution exist rank A < rank Augmented matrix")
         
    return solution

def main():
    mat = matrix_input('matrix.txt')
    print(mat)
    #initialisng dimension of the matrix
    m,n = mat.shape
    print("Dimensison: ",m,n)
    print("solution:\n!------------------------------------------------------!\n")
    X = to_echleon(mat,m,n)
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