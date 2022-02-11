import numpy as np 
def func(x):
    return 1/(5+3*x)

def points_input(filename):
    X = []
    n=0
    file = open(filename,'r+')
    for line in file:
        r =[]
        n+=1
        nums = line.split(' ')
        for num in nums:
            r.append(float(num.strip()))
        X.append(r)
    A = np.array(X,dtype = np.float32)
    A = np.hsplit(A,[1,2])
    return A[0],A[1],n

def IntegrateTrapeziumWithFunction(a,b,n):
    h= (b-a)/n 
    sum = func(a)
    for i in range(0,n-1):
        a +=h 
        print(f"{func(a)}")
        sum += 2 * func(a)
    sum += func(b)
    sum *= h/2 
    return sum  

def IntegrateTrapeziumFromTable(X,Y,n):
    h= (X[n-1]-X[0])/(n-1) 
    print(h)
    sum = Y[0]
    x = X[0]
    for i in range(0,n):
        x +=h 
        sum += 2 * Y[i]
    sum += Y[n-1]
    sum *= h/2 
    return sum  


if __name__ == '__main__':
    # N=[4,8]
    # a = 1
    # b = 2
    # for n in N:
    #     print(f"For n={n} integrat a-> f(x) is {IntegrateTrapeziumWithFunction(a,b,n)}")
    X,Y,n = points_input("in.txt")
    print(f"For n={n} integrat a-> f(x) is {IntegrateTrapeziumFromTable(X,Y,n)}")