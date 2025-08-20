# 정답코드
# stack에 현재 건물보다 높은 건물들을 남겨놓으면서
# 비교 대상의 수를 줄여나간다 -> 시간초과 발생을 줄일 수 있음.
import sys
input = sys.stdin.readline

N = int(input())
height = list(map(int, input().split()))

stack = []
ans = []
for i in range(N):
    building = height[i]

    # 현재 건물보다 높아야지 레이저 수신 가능
    # 현재 높이보다 높은 건물 발견하면 ans에 건물번호와 건물높이 넣기
    while stack:
        if stack[-1][1] > building:
            ans.append(stack[-1][0])
            stack.append([i+1, building])
            break
        # 현재 건물보다 낮은 건물들은 제거
        else:
            stack.pop()
    
    # stack의 길이가 0이면 레이저 수신이 가능한 건물이 없다는 것
    # 따라서 ans에 0을 넣는다.
    # 그리고, 현재 건물을 stack에 넣어 다음 건물과 비교하게 만든다.
    if len(stack) == 0:
        stack.append([i+1, building])
        ans.append(0)

print(*ans)


# 시간초과 발생
import sys
input = sys.stdin.readline

N = int(input())
height = list(map(int, input().split()))
ans = []
for i in range(N):
    if i == 0:
        ans.append(0)
    else:
        check_height = height[:i] # 슬라이싱 O(i)
        # 조건 검사 O(i)
        # 각 건물마다 계속 비교함 -> 시간초과 발생
        possible_num = [idx+1 for idx in range(len(check_height)) if check_height[idx] > height[i]]
        
        if len(possible_num) == 0:
            ans.append(0)
        else:
            ans.append(possible_num[-1])

print(*ans)

