N, M = map(int, input().split())
result = []
def backtracking(n, lst):
    
    if len(lst) == M:
        result.append(lst)
        return
    
    for i in range(n,N+1):
        backtracking(i, lst + [i])

backtracking(1, [])
for i in range(len(result)):
    print(*result[i])