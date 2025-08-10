import sys
input = sys.stdin.readline

M = int(input())
S = set()
for _ in range(M):
    data = list(map(str, input().split()))
    
    if len(data) > 1:
        method = data[0]
        num = data[1]
    else:
        method = data[0]
        
    if (method == 'add') or (method == 'toggle' and int(num) not in S) :
        S.add(int(num))
    elif (method == 'remove' and int(num) in S) or (method == 'toggle' and int(num) in S):
        S.remove(int(num))
    elif method == 'check':
        if int(num) in S:
            print(1)
        else:
            print(0)
    elif method == 'all':
        S = {i for i in range(1, 21)}
    elif method == 'empty':
        S = set()
        