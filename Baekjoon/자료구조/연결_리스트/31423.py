# 시간초과
import sys
input = sys.stdin.readline

from collections import deque

university = deque()

N = int(input())
for _ in range(N):
    university.append(input())

ans = 0
for _ in range(N-1):
    i, j = map(int, input().split())
    university[i-1] += university[j-1]
    university[j-1] = ''
    ans = i

print(university[i-1])

#%%
# 정답코드
import sys
# 기본 재귀 깊이 늘리기 (기본 재귀 깊이는 약 1000)
sys.setrecursionlimit(10**7) # 안늘리면 RecursionError 발생,,,
input = sys.stdin.readline

university = []
N = int(input())
for _ in range(N):
    university.append(input().rstrip())

start_node_list = [0] * (N) # 출발 노드 확인해야함*** 무작정 1로 설정해서 틀림,,,
adj = [[] for _ in range(N+1)]
for _ in range(N-1):
    i, j = map(int, input().split())
    adj[i].append(j) # 단방향
    start_node_list[j-1] += 1

start_node = start_node_list.index(0) # 출발 노드는 j에 안나온 값, 즉 tail이 아닌 숫자 (head인 숫자)

ans = []
# ans = '' # 시간초과
def dfs(s):
    global ans
    # ans += university[s-1] # 시간초과
    ans.append(university[s-1])

    for node in adj[s]:
            dfs(node)

dfs(start_node+1)
print(''.join(ans)) # 리스트 활용해서 join 하는것이 시간초과 발생하지 않음***