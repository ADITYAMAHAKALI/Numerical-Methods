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
    epsilon = 5e-4
    print(epsilon)
    rows = (A.shape)[0] 
    cols = (A.shape)[1]
    print(cols)
    k=0
    while k<10:
        print(f"\nFor iteration number: {k}")
        k+=1
        prev_solution = np.copy(solution)
        for row in range(0,rows):
            solution[row,0] = B[row,0] 
            #print(solution)
            for col in range(0,cols):
                if(col ==row):
                    continue
                if row<=col:
                    print(f"x{row}-=  {A[row,col]} * {prev_solution[col,0]}#x(k)")
                    solution[row,0]-=  A[row,col] * prev_solution[col,0]
                else:
                    print(f"x{row}-=  {A[row,col]} * {solution[col,0]} #x(k+1)")
                    solution[row,0]-=  A[row,col] * solution[col,0]
            solution[row,0] = solution[row,0] / A[row,row]
            print()
        print(f"x{row}  =  {solution[row,0]}")
        flag= checkDifference(prev_solution,solution,epsilon)
        if(flag):
            return solution 
    return solution

def main():
    mat = matrix_input('matrix.txt')
    print("\n\nAugmented Matrix [A:B]\n",mat)
    #initialisng dimension of the matrix
    m,n = mat.shape
    print("Dimensison: ",m,n)
    C = np.hsplit(mat,[n-1,n])
    A = C[0]
    B = C[1]
    print("A:\n",A)
    print("B:\n",B)
    solution = np.zeros([n-1,1],dtype=np.float32)
    solution  = np.reshape(solution,[n-1,1])
    print(solution)
    print("\nsolution:\n!------------------------------------------------------!\n")
    solution = gauss_jacobi(A,B,solution)
    print(solution)
if __name__ == '__main__':
    main()