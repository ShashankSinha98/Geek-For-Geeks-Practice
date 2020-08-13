t = int(input())

def solve(arr):
    n = len(arr)
    dp = []

    for i in range(2**n):
        s = ""
        for j in range(n):
            if(i & (1<<j))!=0:
                s+=str(arr[j])+" "

        if s not in dp:
            dp.append(s)
    
    res = []
    for i in dp:
        res.append([int(j) for j in i.split()])

    return res


while t!=0:
    t-=1
    n = int(input())
    arr = [int(i) for i in input().split()]

    arr.sort()
    res = solve(arr)
    res.sort()
    #print(res)
    ans = ""
    #print(len(res[2]))
    for i in res:
        s = "("
        for j in range(len(i)):
            if j+1==len(i):
                s+=str(i[j])
            else:
                s+=str(i[j])+" "
        s+=")"
        ans+=s

    print(ans)