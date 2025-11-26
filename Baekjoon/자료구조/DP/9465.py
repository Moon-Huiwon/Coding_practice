import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(2)]

    # import copy
    # tmp = copy.deepcopy(arr)

    # tmp[0][1] += tmp[1][0]
    # tmp[1][1] += tmp[0][0]

    # tmp[0][2] += max(tmp[1][1], tmp[1][0])
    # tmp[1][2] += max(tmp[0][1], tmp[0][0])

    # tmp[0][3] += max(tmp[1][2], tmp[1][1])
    # tmp[1][3] += max(tmp[0][2], tmp[0][1])

    # tmp[0][4] += max(tmp[1][3], tmp[1][2])
    # tmp[1][4] += max(tmp[0][3], tmp[0][2])

    if n > 1:    
        arr[0][1] += arr[1][0]
        arr[1][1] += arr[0][0]

        for i in range(2, n):
            arr[0][i] += max(arr[1][i-1], arr[1][i-2])
            arr[1][i] += max(arr[0][i-1], arr[0][i-2])

    ans = 0
    for j in range(2):
        ans = max(ans, arr[j][-1])

    print(ans)