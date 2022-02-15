import math

#function definition
def func(x):
    return  x**4 - x -10

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

def find_root_false_position_with_iterations(x0,x1,iteration):
    new_mid_x = 0 
    prev_x =x1 
    while(iteration>0):
        print(f"\n\nfor: x0={round(x0,7)}, x1={round(x1,7)}")
        print(f"fx0={round(func(x0),7)}, fx1={round(func(x1),7)}")
        new_mid_x = ((x0 * func(x1) )-( x1 * func(x0) ))/(func(x1)-func(x0))
        f_new = func(new_mid_x)
        print(f"new_x = {new_mid_x}")
        
        if(f_new == 0 ):
            print("We some how have found exact root")
            return new_mid_x
        
        #if root liews between x0 and new_mid_x
        if(func(x0)*f_new<0):
            print(f"Since, f({x0}) f({new_mid_x}) < 0, the root lies in the interval ({x0}, {new_mid_x})")
            prev_x = x1
            x1 = new_mid_x
             
        elif(func(x1)*f_new<0):
            print(f"Since, f({new_mid_x}) f({x1}) < 0, the root lies in the interval ({new_mid_x}, {x1})")
            prev_x = x0 
            x0 = new_mid_x
        else:
            print("intermediate value theorem failed!! Possible wrong range of values")
        
        iteration = iteration - 1 
        if(abs(new_mid_x - prev_x)< 1e-6):
            print(f"|{new_mid_x}| - {prev_x}|<{1e-6}")
            return new_mid_x
    return new_mid_x

def printTable(X,Y):
    l = len(X)
    print("Value Table Based on function: ")
    print("X","\t","Y")
    for i in range(l):
        print(X[i],"\t",Y[i])

def main():
    X=[]
    Y=[]
    X,Y = build_table(0,3,0.2)
    printTable(X,Y)
    # determining best x0,x1
    x0,x1 = find_most_appropriate_points(X,Y)
    print("Best x0,x1: ")
    print(x0,x1)
    # now initiating false position method
    root = find_root_false_position_with_iterations(x0,x1,20)
    print("Required value of root: ",root)


if __name__ == "__main__":
    main()