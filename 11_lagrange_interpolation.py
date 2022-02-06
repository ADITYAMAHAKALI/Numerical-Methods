import numpy as np 
from numpy.polynomial import polynomial as P
import math 

def ddfunc(x):
    return -1 * math.sin(x)

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

def lagranges_solution(X,Y,n):
    # number of polynomials = n-1 
    polynomial_terms = []
    for polys in range(0,n):
        # to obtain l(x)
        # In Num we need (x-x1)*(x-x2)...
        # so we nedd a list of these roots 
        # for den we just need (x1-x0) * (x1-x2) 
        x = X[polys]
        y = Y[polys] # this will give f(x){i}
        if(x==0):
            continue 
        Num =[]
        Den = 1
        for root in range(0,n):
            if polys == root :
                continue 
            Num.append(X[root])
            Den*=(x-X[root])
        # calculating lix 
        lx = P.polyfromroots(roots = Num)
        lx = lx / Den 
        lx = lx * y 
        polynomial_terms.append(lx)
    
    px = polynomial_terms[0]
    for i in range(1,len(polynomial_terms)):
        px = px + polynomial_terms[i]
    print(np.poly1d(px))
    return px

# to obtain truncation error we need f''(e)
def max_epsilon(f,range_start,range_end,inc):
    m = -1e9 
    a = range_start
    while(a<=range_end):
        t=f(a)
        if(t>m):
            m = t 
        a+= inc 
    return m 

def truncation_error(roots,e,x):
    px = P.polyfromroots(roots)
    value = P.polyval(x,px)
    value *=e /2
    return value # truncation error   
    
if __name__ == '__main__':
    X,Y,n = points_input("in.txt")
    X = X.flatten()
    Y = Y.flatten()
    print("X: ",X)
    print("Y: ",Y)
    
    p = lagranges_solution(X,Y,n)
    x= 1
    print("Solution of Lagrange's interpolation at {} is {:.5} ".format(x,P.polyval(x,p)))
    e = round(max_epsilon(ddfunc,0.1,0.2,0.0001),5)
    TE = round(truncation_error(X,e,x),5)
    print("Truncation Error is: ",TE)
            
            