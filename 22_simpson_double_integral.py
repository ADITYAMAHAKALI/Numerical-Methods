import math
def func(x,y):
    return math.exp(x+y)

def doubleIntegralOfFunctionViaSimpson1_3(a,b,c,d,n,m):
    integral = 0 
    h = (b-a)/(2*n) # inner increment
    k = (d-c)/(2*m) # outer increment
    x = a
    y = c 
    # upper row 
    #print("for upper row ")
    upper_row = func(x,y) # f(x0,y0)
    #print(x,y,func(x,y))
    for i in range(1,2*m):
        y+= k 
        if(i %2 == 1):
            #print(x,y,4,func(x,y))
            upper_row += 4 * func(x,y)
        else:
            #print(x,y,2,func(x,y))
            upper_row += 2* func(x,y) 
    #print(x,y+k,func(x,y+k))
    upper_row += func(x, y+k) # f(x0,x0 + M * k)
    #print(upper_row)
    #print(x,y+k,func(x,y+k))
    integral +=upper_row
    # middle part 
    middle_part = 0 
    x= a 
    for i in range(1,2*n):
        x +=h 
        y = c
        row = func(x,y)
        for j in range(1,2*m): 
            y += k
            if(j %2 == 1):
                row += 4 * func(x,y)
            else:
                row += 2* func(x,y)
        row += func(x,y+k)
        if(i%2==1):
            middle_part +=  4 * row
        else:
            middle_part +=  2 * row
        
    integral +=  middle_part
    # lower row 
    #print("for lower row ")
    lower_row = 0 
    x =  b
    y =  c 
    #print(x,y,func(x,y))
    lower_row += func(x,y)
    for i in range(1,2*m):
        y+=k 
        if(i%2==1):
            #print(x,y,4,func(x,y))
            lower_row += 4 * func(x,y)
        else:
           # print(x,y,2,func(x,y))
            lower_row += 2* func(x,y)
   # print(x,y+k,func(x,y+k))
    lower_row += func(x,y+k)
    integral += lower_row 
    #print(lower_row)
    integral *= h*k/9
    return integral 

def functionDriver():
    a = float(input("Enter inner lower limit a : "))
    b = float(input("Enter inner upper limit b : "))
    c = float(input("Enter outer lower limit c : "))
    d = float(input("Enter outer upper limit d : "))
    n = int(input("Enter number of points in inner interval 2*n, enter n>=1 : "))
    m = int(input("Enter number of points in outer interval 2*m, enter m>=1 : "))
    print(doubleIntegralOfFunctionViaSimpson1_3(a,b,c,d,n,m))

if __name__ == '__main__':
    functionDriver()