import math
import random as rand 
#function definition

# e.g. f(x) = sin(x)
def func(x):
    return x**5 - x**3 - 3*x**2 +20*x - 12

#e.g. f'(x) = cos(x)
def fdfunc(x):
    return 5*x**4 - 3*x**2 - 6* x +20

# second derivative f''x()
def ddfunc(x):
    return 20*x**3 - 6*x - 6  

def chebyshev():
    x = rand.randint(-20,20) 
    print(x)
    epsilon = 1e-15
    h1 = func(x)/fdfunc(x)
    h2 = ddfunc(x)/fdfunc(x)

    print(x,func(x),fdfunc(x),ddfunc(x),h1,h2)
    while(abs(h1)>epsilon):
        h1 = (func(x)/fdfunc(x))
        h2 =  ddfunc(x)/fdfunc(x)
        x = x-h1 - (1/2) * h1**2 *h2
        print(x,func(x),fdfunc(x),ddfunc(x),h1,h2)
    
    print(round(x,3))

    
def main():
    print("Chebyshev Root Finding Method")
    chebyshev()


if __name__ == "__main__":
    main()
