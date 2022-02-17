def func(x,y):
    return 1/(x+y)

def doubleIntegralOfFunctionViaTrapezoidal(a,b,c,d,n,m):
    integral = 0 
    h = (b-a)/n # inner increment
    k = (d-c)/m # outer increment
    x = a
    y = c 
    # upper row 
    print("for upper row ")
    upper_row = func(x,y) # f(x0,y0)
    print(x,y,upper_row)
    for i in range(1,m):
        y += k 
        print(x,y,func(x,y))
        upper_row += 2 * func(x,y)
    upper_row += func(x, y+k) # f(x0,x0 + M * k)
    print(x,y+k,func(x,y+k))
    integral +=upper_row
    print(integral)
    # middle part 
    middle_part = 0 
    x= a 
    for i in range(1,n):
        x +=h 
        y = c
        row = func(x,y)
        for j in range(1,m): 
            y += k
            row += 2* func(x,y)
        row += func(x,y+k)
        middle_part +=  2 * row 
    integral += middle_part
    # lower row 
    print("for lower row ")
    lower_row = 0 
    x =  a + (n * h) 
    y =  c 
    lower_row += func(x,y)
    print(x,y, lower_row)
    for i in range(1,m):
        y+=k 
        print(x,y,func(x,y))
        lower_row += 2 * func(x,y)
    lower_row += func(x,y+k)
    print(x,y+k,func(x,y+k))
    integral += lower_row 
    integral *= h*k/4
    return integral 

def functionDriver():
    a = float(input("Enter inner lower limit a : "))
    b = float(input("Enter inner upper limit b : "))
    c = float(input("Enter outer lower limit c : "))
    d = float(input("Enter outer upper limit d : "))
    n = int(input("Enter number of points in inner interval n >= 2 : "))
    m = int(input("Enter number of points in outer interval m >= 2 : "))
    print(doubleIntegralOfFunctionViaTrapezoidal(a,b,c,d,n,m))

if __name__ == '__main__':
    functionDriver()