T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    
    floor = (N % H) * 100
    
    if floor == 0:
        floor = H*100
        ho = N // H
    else:
        ho = ((N // H)+1)
    
    print(floor + ho)