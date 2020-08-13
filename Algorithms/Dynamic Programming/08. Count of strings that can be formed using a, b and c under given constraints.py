t = int(input())

def solve(n,b,c):
    #global dp

    if b<0 or c<0:
        return 0

    if n==0:
        return 1

    if b==0 and c==0:
        return 1
        
    res = 0
    res += solve(n-1,b,c)
    res += solve(n-1,b-1,c)
    res += solve(n-1,b,c-1)

    return res



while t!=0:
    t-=1
    n = int(input())
    dp = [[0]*(n+1) for i in range(3)]
    res = solve(n,1,2)
    print(res)