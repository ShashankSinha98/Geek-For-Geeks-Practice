
def min_no(arr,n):

    if n<=2:
        return min(arr)

    l = 0
    r = n-1

    while(l<=r):
        mid = (l+r)//2

        if mid==0 and arr[mid]<arr[mid+1]:
            return arr[mid]
        elif mid==n-1 and arr[mid]<arr[mid-1]:
            return arr[mid]
        elif arr[mid]<arr[mid+1] and arr[mid]<arr[mid-1]:
            return arr[mid]
        elif arr[mid]>arr[l] and arr[mid]>arr[r]:
            l = mid+1
        elif arr[mid]<arr[l] and arr[mid]<arr[r]:
            r = mid-1
        elif arr[l]<arr[r]:
            r = mid-1
        else:
            l = mid+1
    
    return -1


t = int(input())

while t!=0:
    t-=1

    n = int(input())
    arr = [int(i) for i in input().split()]

    print(min_no(arr,n))