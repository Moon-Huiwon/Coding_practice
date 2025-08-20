from collections import deque

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    importance = list(map(int, input().split()))
    
    idx_importance = deque()
    for i in range(len(importance)):
        idx_importance.append([i, importance[i]])
    
    cnt = 0
    
    while idx_importance:
        current_paper = idx_importance.popleft()
        if any(x[1] > current_paper[1] for x in idx_importance):
            idx_importance.append(current_paper)
        else:
            cnt += 1
            if current_paper[0] == M:
                break

    print(cnt)


