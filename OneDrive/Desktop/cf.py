for _ in range(int(input())):
    n = int(input())
    ans = [0] * n
    # fill positions 0 through n-2 with 2,3,…,n
    for i in range(n-1):
        ans[i] = i + 2
    # last position gets 1
    ans[n-1] = 1
    print(*ans)
