import sys
sys.stdin = open('input.txt')

# 내 코드(틀림)
n = int(input())
stack = []
cnt = 0
for _ in range(n):
    x, y = map(int, input().split())
    if len(stack) == 0:
        stack.append(y)
    else:
        if y == 0:
            cnt += len(stack)
            stack = []
        else:
            if stack[-1] < y: # 같은 건물인데 다른 건물로 인식하여 cnt에 문제가 생김
                cnt += 1
            elif stack[-1] == y:
                continue
            else:
                stack.append(y)
    
print(cnt + len(stack))

# GPT 코드
n = int(input())
stack = []
cnt = 0

for _ in range(n):
    x, y = map(int, input().split())

    while stack and stack[-1] > y:
        stack.pop()
        cnt += 1

    if stack and stack[-1] == y:
        continue

    if y != 0:
        stack.append(y)

print(cnt + len(stack))

# 반례 input.txt
"""
6
1 2
2 1
3 2
4 3
5 2
6 0
"""