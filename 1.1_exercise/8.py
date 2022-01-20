import math
import random  
#function definition
def func(x):
    return x**3 - 6*x + 4

def dfunc(x):
    return 3* x**2 - 6 

def newton_raphson():
    x = random.randrange(0,1)
    print(x)
    epsilon = 1e-3
    h = (func(x)/dfunc(x))
    print(x,func(x),dfunc(x),h)
    while(abs(h)>epsilon):
        h = (func(x)/dfunc(x))
        x = x-h
        print(x,func(x),dfunc(x),h)
    
    print(round(x,3))

    
def main():
    print("Newton Raphson Root Finding Method")
    newton_raphson()

if __name__ == "__main__":
    main()
