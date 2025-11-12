import sys
input = sys.stdin.readline

N = int(input())
houses = list(map(int, input().split()))
houses.sort()
idx = []

if len(houses) % 2 == 0:
    idx.append(len(houses) // 2 - 1)
else:
    idx.append(len(houses) // 2 - 1)
    idx.append(len(houses) // 2)

ans = 0
sum_distance = float('inf')
for i in idx:
    distance = 0
    for house in houses:
        distance += abs(houses[i] - house)
    
    if distance < sum_distance:
        sum_distance = distance
        ans = houses[i]
    elif distance == sum_distance:
        ans = min(ans, houses[i])

print(ans)