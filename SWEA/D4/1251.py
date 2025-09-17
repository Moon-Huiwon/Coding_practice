from heapq import heappush, heappop

def prim(idx):
    pq = [(0, idx)]
    MST = [0]*N
    min_price = 0

    while pq:
        price, idx = heappop(pq)

        if MST[idx]:
            continue

        MST[idx] = 1
        min_price += price
        for i in range(N):
            
            if MST[i]:
                continue

            heappush(pq, (E*((x[idx] - x[i])**2 + (y[idx] - y[i])**2),i))
    
    return min_price
    
T = int(input())
for t in range(T):
    N = int(input())
    x = list(map(int,input().split()))
    y = list(map(int,input().split()))
    E = float(input())
    ans = prim(0)
    print(f'#{t+1} {ans:.0f}')