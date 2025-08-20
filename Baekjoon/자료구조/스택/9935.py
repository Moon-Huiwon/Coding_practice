# 시간초과
import sys
input = sys.stdin.readline

string = input().rstrip()
remove_str = input().rstrip()

while string.count(remove_str) > 0:
    string = string.replace(remove_str, "")

if len(string) > 0:
    print(string)
else:
    print('FRULA')

#%%
# 정답 코드
import sys
input = sys.stdin.readline

string = list(input().rstrip())
remove_str = list(input().rstrip())

stack = []
for s in string:
    stack.append(s)

    if len(stack) >= len(remove_str):
        if stack[-len(remove_str):] == remove_str:
            # del 사용하는 걸 생각 안함
            # 처음에 슬라이싱으로 stack을 재할당했었음 -> 시간초과
            del stack[-len(remove_str):] 

if len(stack) > 0:
    print(''.join(stack))
else:
    print('FRULA')


    
