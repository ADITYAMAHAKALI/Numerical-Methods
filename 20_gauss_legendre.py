import math

def functionAfterTransformation(t):
    # write the transformed f(t) with limit of -1 --> 1 here 
    return  1/(t+3)

def onePointGaussLegendre():
    return 2 * functionAfterTransformation(0)

def twoPointGaussLegendre():
    return functionAfterTransformation(-1/ math.sqrt(3)) + functionAfterTransformation(1/math.sqrt(3))

def threePointGaussLegendre():
    return (5 * functionAfterTransformation(- math.sqrt(3/5)) + 8 * functionAfterTransformation(0) + 5 * functionAfterTransformation(math.sqrt(3/5))) / 9

if __name__ == '__main__':
    choice = int(input('''
    Enter 1 for Gauss-legendre one point method
    Enter 2 for Gauss-legendre two point method
    Enter 3 for Gauss-legendre three point method: '''))
    if choice == 1:
        print("Integral is : ", onePointGaussLegendre())
    elif choice ==2:
        print("Integral is : ",twoPointGaussLegendre())
    elif choice ==3:
        print("Integral is : ",threePointGaussLegendre())
    else:
        print("Invalid Input!!!")
