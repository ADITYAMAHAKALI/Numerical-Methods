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
        delkf.append(Y[y+1] - Y[y])
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
            
def dfx0(h,differences):
    n = len(differences)
    x = 0 
    for i in range(0,n-1):
      sign = (-1)**i
      print(f"{sign} * {differences[i][i+1][0]} / {i+1}")
      x += sign * differences[i][i+1][0] / (i+1) 
      print(x)
    return x/h
        
        
if __name__ == '__main__':
    X,Y,n = points_input("in.txt")
    X = X.flatten()
    Y = Y.flatten()
    print("X: \n",X)
    print("Y: \n",Y)
    print("n: ",n)
    forwardDifference(Y,1)
    printTable(differences)
    # assuming constant difference
    h = X[1] - X[0]
    print("h : ",h)
    print("f'(x0) = ",dfx0(h,differences))
    