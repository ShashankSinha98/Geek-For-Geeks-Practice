#   Note: The tricky part is that , question has asked for combinations not permutations
#   If only permutations were asked , we could have simply done dp[i]=dp[i-3]+dp[i-5]+dp[i-10] , as it does not care about the duplicate sets .

#   Now to avoid that,
#   1) first mark all values which can be made by moving 3 .
#   eg if n=8 . all values that can be made using only 3 coins are multiple of 3 .
#   Technically we write it as dp[i]=d[i]+dp[i-3];
#   2)Now moves using 3 are done , mark all moves by moving 5 , This gives us all combinations that can be made using only 3 and 5
#   Technically we write it as dp[i]=dp[i]+dp[i-5]
#   3)Now moves using 3 and 5 are done , mark all moves by moving 10 , This gives us all combinations that can be made using 3 , 5 and 10(note that we would never come across duplicated in such a case)
#   Technically we write it as dp[i]=dp[i]+dp[i-10]



t = int(input())

def solve(n):

    dp = [0]*(n+1)
    dp[0] = 1


    for i in range(3,n+1):
        dp[i] += dp[i-3]
    
    for i in range(5,n+1):
        dp[i] += dp[i-5]

    for i in range(10,n+1):
        dp[i] += dp[i-10]

    return dp[n]


while t!=0:
    t-=1

    n = int(input())
    print(solve(n))