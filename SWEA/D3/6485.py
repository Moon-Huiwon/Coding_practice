import sys
sys.stdin = open('input.txt')

#%%
T = int(input())
for t in range(T):
    N = int(input())
    bus_stop_list = [0] * 5001
    
    for _ in range(N):
        A, B = map(int, input().split())
        for num in range(A, B+1):
            bus_stop_list[num] += 1

    P = int(input())
    print(f'#{t+1}', end=" ")
    for _ in range(P):
        C = int(input())
        print(bus_stop_list[C], end=" ")
    
    # ***테스트 케이스의 경우 다른 라인으로 넘어가야 함
    print()
