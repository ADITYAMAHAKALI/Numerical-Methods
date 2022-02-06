import numpy as np 
from numpy.polynomial import polynomial as Pn
import math 

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

DividedDifferences = []

def obtainNthDividedDifference(k,X,Y):
    kthdd = []
    print("\n\n\nFor k= ",k)
    if(k>=len(X)):
        print(f"{k}th divided difference not required")
        return 
    for i in range(0,len(Y)-1):
        Num = Y[i+1] - Y[i]
        print("Num = {} - {} = {} ".format(Y[i+1],Y[i],Num))
        Den = X[i+k] - X[i]
        print("Den = {} - {} = {} ".format(X[i+k],X[i],Den))
        t = Num /Den 
        print(t)
        kthdd.append(t)
    print(kthdd)
    DividedDifferences.append({k : kthdd})
    k+=1
    obtainNthDividedDifference(k,X,kthdd)
    
def find_interpolation_polynomial(X,Y,DividedDifferences):
    px =  Pn.Polynomial(0.0)
    px+=float(Y[0])
    print("f(x0): ",px)
    n = len(DividedDifferences)
    for i in range(0,n-1):
        roots = []
        for j in range(0,i+1):
            roots.append(X[j])
        tx = Pn.polyfromroots(roots)
        #print(roots)
        print("\n{} {}\n".format(tx,DividedDifferences[i][i+1][0]))
        tx *= DividedDifferences[i][i+1][0]
        px+=tx 
        #print(px)
    return px

if __name__ == '__main__':
    X,Y,n = points_input('in.txt')
    X = X.flatten()
    Y = Y.flatten()
    print("X: ",X)
    print("Y: ",Y)
    print(n)
    obtainNthDividedDifference(1,X,Y)
    print("Divided differences: ",DividedDifferences)
    px = find_interpolation_polynomial(X,Y,DividedDifferences)
    print(px)
    x = 8.0
    
    roots = px.roots()
    tx = Pn.polyfromroots(roots)
    value = Pn.polyval(x,tx)
    print(value)