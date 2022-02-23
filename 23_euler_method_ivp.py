def func(x,y): # this is y' = f(x,y)
    return x/y 

def eulerMethodDiffEqn(a,b,h,x0,y0):
    x =a 
    y = y0 
    while(round(x,3)< round(b ,3)):
        print(f"y({round(x+h,5)}) = {round(y,5)} + {h} * f({round(x,5)},{round(y,5)}) = ",end=' ')
        y = y + h * func(x,y)
        print(round(y,5))
        x = x+h 
    

if __name__ == '__main__':
    h = float(input("Enter h: "))
    a = float(input("Enter initial x0 of range of x : "))
    b = float(input("Enter xn of range of x: "))
    x0 = float(input("Enter initial value of x : "))
    y0 = float(input("Enter initial value of y : "))
    eulerMethodDiffEqn(a,b,h,x0,y0)
