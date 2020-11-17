t = int(input())

def longest_prefix_suffix(inp_str):

    n = len(inp_str)
    arr = [0]*n

    i = 1
    j = 0

    while i<n:

        if inp_str[i] == inp_str[j]:
            arr[i] = j+1
            i+=1
            j+=1

        else:
            if j==0:
                arr[j] = 0
                i+=1
            else:
                j = arr[j-1]

    return arr[-1]



while t!=0:
    t-=1

    inp_str = input()
    print(longest_prefix_suffix(inp_str))