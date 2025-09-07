def backtracking(lst):
    global result
    if len(lst) == M:
        result.append(lst)
        return
    
    for i in range(1,N+1):
        backtracking(lst + [i])


N, M = map(int, input().split())
result = []
backtracking([])

for i in range(len(result)):
    print(*result[i])
