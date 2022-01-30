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
    return np.array(mat,dtype=np.float32)

def checkDifference(A,B,epsilon):
    len = (A.shape)[1]
    error_sum = 0 
    
    for i in range(0,len):
        if(abs(A[i,0] - B[i,0])>epsilon):
            return False
    for i in range(0,len):
        print(f"|{A[i,0]}- {B[i,0]}| < {epsilon}\n")
    
    return True
        
def gauss_jacobi(A,B,solution):
    epsilon = 5e-3
    print(epsilon)
    rows = (A.shape)[0] 
    cols = (A.shape)[1]
    print(cols)
    k=0
    while k<10:
        print(f"\nFor iteration number: {k}")
        k+=1 #number of iterative loops
        prev_solution = np.copy(solution)
        for row in range(0,rows):
            solution[row,0] = B[row,0] 
            #print(solution)
            for col in range(0,cols):
                if(col ==row):
                    continue
                print(f"x{row}-=  {A[row,col]} * {prev_solution[col,0]}")
                solution[row,0]-=  A[row,col] * prev_solution[col,0]
            solution[row,0] = solution[row,0] / A[row,row]
            print()
        #print(f"x{row}  =  {solution[row,0]}")
        print(np.reshape(solution,[1,rows]))
        if( checkDifference(prev_solution,solution,epsilon)):
            return solution 
    return solution

def DiagonallyDominant(A):
    [rows,cols] = A.shape
    for iteration in range(rows):
        #print(iteration)
        max_pivot = -1e9
        max_row_index=0
        for row in range(iteration,rows):
            if(abs(A[row,iteration])> max_pivot):
                #print("m:", max_start_row)
                max_pivot = abs(A[row,iteration])
                max_row_index = row
        if(iteration != max_row_index):
            #print(f"R{iteration} <--> R{max_row_index}")
            A[[iteration,max_row_index]] = A[[max_row_index,iteration]]
        
        #print(A)
    return A
            
        
    
def main():
    mat = matrix_input('matrix.txt')
    print("\n\nAugmented Matrix [A:B]\n",mat)
    #initialisng dimension of the matrix
    m,n = mat.shape
    mat = DiagonallyDominant(mat)
    print("Diagonally Dominant Matrix: \n",mat)
    C = np.hsplit(mat,[n-1,n])
    A = C[0]
    B = C[1]
    print("A:\n",A)
    print("B:\n",B)
    solution = np.zeros([n-1,1],dtype=np.float32)
    print("Initial Solution Vector")
    print(solution)
    print("\nsolution:\n!------------------------------------------------------!\n")
    solution = gauss_jacobi(A,B,solution)
    print(solution)
if __name__ == '__main__':
    main()