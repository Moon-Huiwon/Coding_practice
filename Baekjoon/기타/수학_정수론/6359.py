T = int(input())
for _ in range(T):
    n = int(input())
    rooms = [1] * (n+1)
    for i in range(2,n+1):
        for j in range(1,n+1):
            if j % i == 0:
                rooms[j] *= -1
    
    print(rooms[1:].count(1))