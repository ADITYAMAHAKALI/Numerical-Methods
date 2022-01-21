import math
import random  
#function definition
p =5

def func(x):
    return 3*x - math.cos(x) -1

def dfunc(x):
    return 3 + math.sin(x)

def newton_raphson():
    x = random.random()
    print(x)
    epsilon = 1e-4
    h = (func(x)/dfunc(x))
    print(round(x,p),round(func(x),p),round(dfunc(x),p),round(h,p))
    while(abs(h)>epsilon):
        h = (func(x)/dfunc(x))
        x = x-h
        print(round(x,p),round(func(x),p),round(dfunc(x),p),round(h,p))
    
    print(round(x,p))

    
def main():
    print("Newton Raphson Root Finding Method")
    newton_raphson()

if __name__ == "__main__":
    main()
