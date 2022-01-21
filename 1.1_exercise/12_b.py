import math
import random  
#function definition
p =3

def func(x):
    return x**2 - 142

def dfunc(x):
    return 2*x

def newton_raphson():
    x = 12
    print(x)
    epsilon = 1e-3
    h = (func(x)/dfunc(x))
    print(round(x,p),round(func(x),p),round(dfunc(x),p),round(h,p))
    while(abs(h)>epsilon):
        h = (func(x)/dfunc(x))
        x = x-h
        print(round(x,p),round(func(x),p),round(dfunc(x),p),round(h,p))
    
    print(round(x,3))

    
def main():
    print("Newton Raphson Root Finding Method")
    newton_raphson()

if __name__ == "__main__":
    main()
