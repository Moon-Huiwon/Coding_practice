import sys
input = sys.stdin.readline

def backtracking(start, depth, lst):

    if depth == M:
        result.append(lst)
        return

    for i in range(start, N+1):
        backtracking(i+1, depth+1, lst+[i])
        

N, M = map(int, input().split())
result = []
backtracking(1, 0, [])
for i in range(len(result)):
    print(*result[i])