t = int(input())

def solve(arr,n):

    if(n<=0):
        return 0
    if(n==1):
        return arr[0]
    if(n==2):
        return min(arr[0],arr[1])

    return min(arr[n-1]+solve(arr,n-1),arr[n-2]+solve(arr,n-2))

while t!=0:
    t-=1

    n = int(input())
    arr = [int(i) for i in input().split()] 

    print(solve(arr,n))