#%%
# 시간초과 발생
# insert()`나 `pop(index)`를 사용하면, 그 이후 모든 원소를 한 칸씩 밀거나 당겨야 하므로 O(n) 시간이 걸림
import sys
input = sys.stdin.readline

string = list(input().strip())
M = int(input())

point = len(string)
for _ in range(M):
    input_value = list(map(str, input().split()))
    if len(input_value) > 1:
        command = input_value[0]
        s = input_value[1]
    else:
        command = input_value[0]
    
    if command == 'L' and point > 0:
        point -= 1
    elif command == 'D' and point < len(string):
        point += 1
    elif command == 'B' and point > 0:
        string.pop(point - 1) # 시간 초과 원인
        point -= 1
    elif command == 'P':
        string.insert(point, s) # 시간 초과 원인
        point += 1

print(*string)

#%%
# 커서를 기준으로 left_stack과 right_stack를 구분해서 사용
import sys
input = sys.stdin.readline
# 개행문자 제거하는 strip() 사용하기 ***
left_stack = list(input().strip())
right_stack = []
M = int(input())

for _ in range(M):
    cmd = input().split()
    if cmd[0] == 'L':
        # 커서 왼쪽에 데이터가 있으면
        if left_stack:
            # right_stack에 마지막 value를 저장하고 삭제
            right_stack.append(left_stack.pop())
    
    elif cmd[0] == 'D':
        if right_stack:
            left_stack.append(right_stack.pop())
    
    elif cmd[0] == 'B':
        if left_stack:
            left_stack.pop()
    
    elif cmd[0] == 'P':
        left_stack.append(cmd[1])

# right_stack은 reverse해야하는 점 유의
print(''.join(left_stack + right_stack[::-1]))