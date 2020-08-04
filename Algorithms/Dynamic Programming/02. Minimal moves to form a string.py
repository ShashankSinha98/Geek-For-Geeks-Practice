#   We have to find the minimum number of operations to make the string . Its clearly visible dp can be one possible approach .
#   Now we consider string till every index(1...n)
#   -dp[i] will represent minimum number of operations required to form the string from index 1...i .
#   - Now from i is odd , it can be made by appending the string to itself ?(why?)-
#   because appending the string to itself will always result in an even length string .
#   so if is odd dp[i]=dp[i-1]+1;
#   - Now if is even , check from the half of the string
#   if both halves are equal dp[i]=dp[last index of first half]+1 , else dp[i]=dp[i-1]+1 .
#   -return dp[n]



t = int(input())

def solve(st,n):

    dp = [0]*(n+1)

    for i in range(1,n+1):

        if i&1!=0: #odd
            dp[i] = dp[i-1]+1
        else:
            mid = i//2
            if st[0:mid] == st[mid:i]:
                dp[i] = dp[i//2] + 1
            else:
                dp[i] = dp[i-1] + 1

    #print(dp)
    return dp[n]




while t!=0:
    t-=1

    st = input()
    print(solve(st,len(st)))