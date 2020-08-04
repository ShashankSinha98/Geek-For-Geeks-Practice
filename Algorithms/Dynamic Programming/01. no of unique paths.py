t = int(input())

def dp_solve(m,n):
    arr = [[0]*n for i in range(m)]
    for i in range(m):
        arr[i][0] = 1

    for i in range(n):
        arr[0][i] = 1

    for i in range(1,m):
        for j in range(1,n):
            arr[i][j] = arr[i-1][j]+arr[i][j-1]
    
    return arr[m-1][n-1]

def fact(n):
    res = 1
    while n>0:
        res*=n
        n-=1
    return res

def formula_solve(m,n):

    num = fact(m+n-2)
    den = fact(m-1)*fact(n-1)

    return num//den




while t!=0:
    t-=1
    
    m,n = [int(i) for i in input().split()] 
        
    res = formula_solve(m,n)
    print(res)

