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