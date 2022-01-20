import math
#function definition
def func(x):
    return x**4 - x - 10
def dfunc(x):
    return 4* x**3 - 1 

def newton_raphson():
    x = 10
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
