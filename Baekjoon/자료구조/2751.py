#%%
import sys
input = sys.stdin.readline
N = int(input())
num_list = []
for _ in range(N):
    num_list.append(int(input()))

num_list.sort()

for i in range(len(num_list)):
    print(num_list[i])

#%%
# Optimal Code (merge sort 활용)
N = int(input())
num_list = []
for _ in range(N):
    num_list.append(int(input()))

def merge_sort(num_list):
    if len(num_list) <= 1:
        return num_list

    mid = len(num_list) // 2
    L = merge_sort(num_list[:mid])
    R = merge_sort(num_list[mid:])
    mer = []

    i = 0
    j = 0

    while i < len(L) and j < len(R):
        if (L[i] > R[j]):
            mer.append(R[j])
            j += 1
        else:
            mer.append(L[i])
            i += 1
    
    if i != len(L):
        mer += L[i:]
    if j != len(R):
        mer += R[j:]
    return mer

mer = merge_sort(num_list)
for i in mer:
    print(i)


