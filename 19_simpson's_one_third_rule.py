import numpy as np 
import math 

def func(x):
    return 1/(x**2 + 6*x + 10)

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

def simpsonOneThirdByFunction(a,b,N):
    # we need to get h = b-a/2N
    h = (b - a)/(2*N)
    print(h)
    # initailise looping variable with x 
    x = a
    integral = func(a) # f(x0)
    iteration = 1
    while(x<b-h):
        x = x+h
        if(iteration %2 ==1): #i.e. for odd terms of x 
            integral += (4 * func(x))
        else:
            integral += (2 * func(x))
        iteration +=1 
    integral += func(b) 
    integral *= (h/3)
    return integral
    

def byFunctionDriver():
    N= [1,2,4]
    a = 0
    b = 1.0
    for n in N:
        print(f"For N= {n} the value of integral of f(x) from {a} to {b} is : {simpsonOneThirdByFunction(a,b,n)}")

def byTableSimpsoneOneThirdRule():
    X,Y,n = points_input("in.txt")
    h = X[1] - X[0]
    print("h: ",h)
    integral = Y[0] + Y[n-1]
    for i in range(1,n-1):
        if(i%2 ==1): # x1,x3,x5...
            integral += 4 * Y[i]
        else:
            integral += 2 * Y[i]
    integral *= (h/3)
    return integral

        


    

if __name__ == '__main__':
    #byFunctionDriver()
    print(f"Integeration by the table is : {byTableSimpsoneOneThirdRule()} ")