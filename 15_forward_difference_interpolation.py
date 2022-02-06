import math
import numpy as np 
import numpy.polynomial as poly 
'''
I have taken this superscript and substring printing functunality from gfg's following article:
    https://www.geeksforgeeks.org/how-to-print-superscript-and-subscript-in-python/
'''

def get_super(x):
    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
    super_s = "ᴬᴮᶜᴰᴱᶠᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾQᴿˢᵀᵁⱽᵂˣʸᶻᵃᵇᶜᵈᵉᶠᵍʰᶦʲᵏˡᵐⁿᵒᵖ۹ʳˢᵗᵘᵛʷˣʸᶻ⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾"
    res = x.maketrans(''.join(normal), ''.join(super_s))
    return x.translate(res)

def get_sub(x):
    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
    sub_s = "ₐ₈CDₑբGₕᵢⱼₖₗₘₙₒₚQᵣₛₜᵤᵥwₓᵧZₐ♭꜀ᑯₑբ₉ₕᵢⱼₖₗₘₙₒₚ૧ᵣₛₜᵤᵥwₓᵧ₂₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎"
    res = x.maketrans(''.join(normal), ''.join(sub_s))
    return x.translate(res)


def points_input(filename):
    X = []
    n=0
    file = open(filename,'r+')
    for line in file:
        r =[]
        n+=1
        nums = line.split(' ')
        for num in nums:
            r.append(float(num.strip()))
        X.append(r)
    A = np.array(X,dtype = np.float32)
    A = np.hsplit(A,[1,2])
    return A[0],A[1],n

differences = []

def forwardDifference(Y,k):
    n = len(Y)
    if(n<=0):
        return 
    delkf = []
    for y in range(0, n-1):
        delkf.append(round(Y[y+1] - Y[y] , 6))
    differences.append({k:delkf})
    k+=1
    forwardDifference(delkf,k)

def printTable(differences):
    n = len(differences)
    for k in range(1,n+1):
        print(f"for del_f{get_super(str(k))}\n")
        m = len(differences[k-1][k])
        for j in range(0,m):
            print(f"for del_f{get_super(str(k))}{get_sub(str(j))} = {differences[k-1][k][j]}")
            
def InterpolationPolynomial(X,px,differences,h,x):
    n = len(differences)
    for i in range(0,n-1):
        roots = []
        for j in range(0,i+1):
            roots.append(X[j])
        lx = poly.polynomial.polyfromroots(roots)
        #print(lx)
        lx *= differences[i][i+1][0]
        lx /= (math.factorial(i+1) *math.pow(h,i+1))
        print(f"value of l{i}x :{poly.polynomial.polyval(x,lx)}")
        print(lx)
        px+=lx
    return px
        
if __name__ == '__main__':
    X,Y,n = points_input("in.txt")
    X = X.flatten()
    Y = Y.flatten()
    # Y = np.cos(X) // this was for ques 11.2 exercise 2.2
    # Y *= 0.12
    print("X: \n",X)
    print("Y: \n",Y)
    print("n: ",n)
    forwardDifference(Y,1)
    printTable(differences)
    # now based on the table I need to construct the interpolation polynomial
    px =  poly.Polynomial(0.0)
    # first I will initialise the polynomial with f(x0) i.e. Y[0]
    px+=float(Y[0]) 
    print(px)
    h = X[1] - X[0]
    x = 0.12
    px = InterpolationPolynomial(X,px,differences,h,x)
    print(px)
    t = px.coef
    p = np.round(px.coef)
    print(p)
    value = poly.polynomial.polyval(x,t)
    print(value)
    