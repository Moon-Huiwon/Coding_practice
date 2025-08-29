for t in range(10):
    N = int(input())
    adj = [[] for _ in range(N+1)]
    for _ in range(N):
        info = list(input().split()) # 각 정점의 정보 받기
        
        node = int(info[0]) # 노드 번호
        adj[node].extend(info[1:]) # 나머지
    
    for i in range(N, 0, -1):
        if len(adj[i]) > 1: # 연산자가 있는 노드
            cal = adj[i].pop(0) # 연산자
            left = int(adj[i].pop(0)) # 왼쪽 값
            right = int(adj[i].pop(0)) # 오른쪽 값

            if cal == '+':
                num = int(adj[left][0]) + int(adj[right][0])
            elif cal == '-':
                num = int(adj[left][0]) - int(adj[right][0])
            elif cal == '/':
                num = int(adj[left][0]) / int(adj[right][0])
            else:
                num = int(adj[left][0]) * int(adj[right][0])
            
            adj[i].append(num) # 연산 결과 넣기
        
        else:
            continue
    
    print(f'#{t+1} {int(adj[1][0])}')

#%%
# deque 활용
from collections import deque

for t in range(10):
    N = int(input())
    adj = [deque() for _ in range(N+1)]
    for _ in range(N):
        info = list(input().split())
        
        node = int(info[0])
        adj[node].extend(info[1:])
    
    for i in range(N, 0, -1):
        if len(adj[i]) > 1:
            cal = adj[i].popleft()
            left = int(adj[i].popleft())
            right = int(adj[i].popleft())

            if cal == '+':
                num = int(adj[left][0]) + int(adj[right][0])
            elif cal == '-':
                num = int(adj[left][0]) - int(adj[right][0])
            elif cal == '/':
                num = int(adj[left][0]) / int(adj[right][0])
            else:
                num = int(adj[left][0]) * int(adj[right][0])
            
            adj[i].append(num)
        
        else:
            continue
    
    print(f'#{t+1} {int(adj[1][0])}')