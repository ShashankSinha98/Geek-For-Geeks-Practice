t = int(input())

def solve(st,n):

    dp = [1]*(n)

    for i in range(1,n):
        best = 0
        for j in range(i):
            if st[j]<st[i]:
                best = max(best,dp[j])
        dp[i] = best+1

    #print(dp)
    return max(dp)


while t!=0:
    t-=1
    st = input()

    print(solve(st,len(st)))