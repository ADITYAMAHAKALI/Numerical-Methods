import math
import random  
#function definition
p =3

def func(x):
    return x-1/26

def dfunc(x):
    return 1

def newton_raphson():
    x = 1.9
    print(x)
    epsilon = 1e-3
    h = (func(x)/dfunc(x))
    print(x,func(x),dfunc(x),h)
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
