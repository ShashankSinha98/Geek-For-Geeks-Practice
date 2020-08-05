t = int(input())

def solve(n):
    dp = [0]*(n+1)
    dp[0] = 1

    for i in range(1,n+1):
        for j in range(i,i-4,-1):
            if j>=0:
                dp[i]+=dp[j]
    #print(dp)
    return dp[n]





while t!=0:
    t-=1

    n = int(input())
    print(solve(n))
