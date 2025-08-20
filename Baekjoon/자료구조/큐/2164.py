import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
num_list = deque(range(1,n+1))

while len(num_list) > 1:
    num_list.popleft()
    num_list.append(num_list[0])
    num_list.popleft()

print(num_list[0])