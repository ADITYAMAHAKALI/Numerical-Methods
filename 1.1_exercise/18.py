import math
import random
#function definition
# --------------1. To change for each question -------------
# to demonstrate 
# def func(x):
#     return  3*x**3 - x + 1

# def phi(x):
#     return (3*x**3 + 1) 

# def dphi(x):
#     return (9*x**2) #/64

def func(x):
    return  3*x**3 - x + 1

def phi(x):
    if (x-1) >0:
        return math.pow(((x-1)/3),float(1)/3)
    elif (x-1) <0:
        return -math.pow((abs(x-1)/3),float(1)/3)
    else:
        return 0

def dphi(x):
    if (x-1)>0 : 
        return (1/9)* math.pow((3/(x-1)),float(2/3))
    elif (x-1) < 0:
        return (-1/9)* math.pow((3/abs(x-1)),float(2/3))
    else:
        return 0

def build_table(range_start,range_end,increment):
    x = range_start
    X=[]
    Y=[] 
    while(x<=range_end):
        X.append(x)
        Y.append(func(x))
        x= x+increment 
    return X,Y 

def find_most_appropriate_points(X,Y):
    l = len(X)
    best_start = 0
    least_magnitude = 1e9
    for i in range(l-1):
        #checking whether value is negative
        if(func(X[i])*func(X[i+1])<0):
            #making_sure that x0, x1 are of least magnitude
            if(abs(X[i]*X[i+1])<= least_magnitude):
                best_start = i
                least_magnitude = abs(X[i]*X[i+1])
    return X[best_start],X[best_start+1]

def printTable(X,Y):
    l = len(X)
    print("Value Table Based on function: ")
    print("X","\t","Y")
    for i in range(l):
        print(X[i],"\t",Y[i])

def check_convergence(a,b):
    i = 0.001
    x = a +i
    while(x<=b):
        if(dphi(x) >= 1):
            print("This phi(x) function will not work for this interval")
            return False
        x+=i
    return True 

def general_iteration(x,p):
    while True:
        prev_x = x
        x = phi(x)
        print(x)
        print(f"for {round(prev_x,p)} phi({round(prev_x,p)}) = {round(x,p)},")
        h = abs(x-prev_x)
        print(f"in this step |{round(prev_x,p)} -{round(x,p)}| = {round(h,p)},")
        print()
        if(h<1e-9):
            return x
        
def main():
    X=[]
    Y=[]
    # --------------2. To change for each question(maybe) ------------- 
    p = 6 # precision
    X,Y = build_table(-10,10,1)
    printTable(X,Y)
    # determining best x0,x1
    x0,x1 = find_most_appropriate_points(X,Y)
    print("Best x0,x1: ")
    print(x0,x1)
    if(check_convergence(x0,x1)):
        # selecting a random initialisng point between 2 and 3
        if( x1 !=0):
            x = random.random()%x1 + x0
        else:
            x= (x1+x0)/2
        print(round(x,p))
       
        root = general_iteration(x,p)
        print("Apporxiamte Root: ",round(root,p))
    else:
        print("!!! Change phi function")
    


if __name__ == "__main__":
    main()
