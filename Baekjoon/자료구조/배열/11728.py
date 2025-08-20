#%%
# merge sort 찾아보기
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

answer_list = A+B
answer_list.sort()

print(*answer_list)

# 투포인터 활용
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = []

a = 0
b = 0

# ans에 저장된 A 원소의 횟수가 len(A)와 같거나
# B의 원소의 횟수가 len(B)와 같으면 더 이상 비교 작업을 할 필요 없으므로
# ans에 순차적으로 넣기
while a != len(A) or b != len(B):
    if a == len(A):
        ans.append(B[b])
        b += 1
    elif b == len(B):
        ans.append(A[a])
        a += 1
    # 그 외의 케이스에서는 A의 원소와 B의 원소를 비교해서 작은 값을 ans에 입력
    else:
        if A[a] < B[b]:
            ans.append(A[a])
            a += 1
        else:
            ans.append(B[b])
            b += 1

print(*ans)