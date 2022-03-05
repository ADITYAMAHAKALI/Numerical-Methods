def func(x,y):
    print(f"\t= ({y}**2 - {x}**2)/({y}**2 + {x}**2) ")
    return (y**2 - x**2)/(y**2 + x**2)

def rangeKuttaMethod(x0,y0,a,b,h):
    x = x0 
    y = y0 
    i = 0
    while (x<b):
        print(f"\n\nFor i ={i}, x={x},y={y}")

        print(f"k1 = {h} * f({x},{y})")
        k1 = h * func(x,y)
        print(f"k1 = {k1}")

        print(f"k2 = {h} * f({x+ (h/2)},{y + (k1/2)})")
        k2 = h * func(x+ (h/2) , y + (k1/2) )
        print(f"k2 = {k2}")

        print(f"k3 = {h} * f({x+ (h/2)},{y + (k2/2) })")
        k3 = h * func(x+ (h/2) , y + (k2/2) )
        print(f"k3 = {k3}")

        print(f"k4 = {h} * f({x + h},{y+k3})")
        k4 = h * func(x + h , y + k3 )
        print(f"k4 = {k4}")

        y  = y+ (1/6) * (k1 + 2 * k2 +  2* k3 + k4)
        x = x+h  
        print(f"y({x}) = {y}")
        i=i+1

if __name__ == '__main__':
    # taking all inputs x0,y0, [a,b] and h
    x0 = float(input("Enter Iniital x0 "))
    y0 = float(input("Enter Initial y0 "))
    choice = int(input("Enter 1 if you are solving a problem with range 0 otherwise "))
    if(choice == 1):
        a  = float(input("Enter starting point of interval "))
        b  = float(input("Enter end point of interval "))
        h  = float(input("Enter step difference h "))
        rangeKuttaMethod(x0,y0,a,b,h)
    else:
        a=x0
        b= float(input("Enter point of calculation "))
        h  = float(input("Enter step difference h "))
        rangeKuttaMethod(x0,y0,a,b,h)
