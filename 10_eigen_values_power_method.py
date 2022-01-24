import numpy as np

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



def find_approx_eigen_values(A,solution_vector,n):
    epsilon = 5e-4
    eigen_value = solution_vector[1,0]
    iteration = 0
    while iteration<10:
        print(f"\nfor iteration no: {iteration}\n")
        iteration+=1
        prev_eigen_value = np.copy(eigen_value)
        print(f"taking product of \n{A} and \n{solution_vector}\n")
        solution_vector = np.matmul(A,solution_vector)
        print("New Solution_vector:\n",solution_vector)
        eigen_value = np.copy(np.amax(solution_vector))
        solution_vector = np.copy(solution_vector / eigen_value)
        print("Eigen_value: ",eigen_value)
        
        if(abs(eigen_value-prev_eigen_value)<epsilon):
            print(f"|{eigen_value} - {prev_eigen_value} < {epsilon}")
            return eigen_value,solution_vector

def determineSign(A,eigen_value):
    dim  = A.shape
    I = np.identity(dim[0])
    I*=eigen_value
    magnitude = np.linalg.det(A-I)
    #print(magnitude)
    if(abs(magnitude) < 1):
        print(f"|A- lambda * I| is close to zero so eigenvalue is positive ")
        return '+'
    else:
        print(f"|A- lambda * I| is not close to zero so eigenvalue is negative ")
        return '-'
        
def main():
    mat = matrix_input('matrix.txt')
    print("\n\nAugmented Matrix [A:B]\n",mat)
    #initialisng dimension of the matrix
    m,n = mat.shape
    C = np.hsplit(mat,[n-1,n])
    A = C[0]
    B = C[1]
    print("A:\n",A)
    print("B:\n",B)
    print("Dimensison: ",m,n)
    if(m!=n-1):
        print("Change the matrix, only square matrix have eigen values")
    
    eigen_value,eigen_vector = find_approx_eigen_values(A,B,n)
    print("\n\nLargest Eigen value: ",eigen_value)
    print("\nCorresponding Eigen vector: \n",eigen_vector)
    #--------To obtain the sign of eigen value
    sign = determineSign(A,eigen_value)
    print("\nSign of eigen value is: ",sign)

if __name__ == '__main__':
    main()