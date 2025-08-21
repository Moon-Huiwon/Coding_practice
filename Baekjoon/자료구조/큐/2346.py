N = int(input())
move_info = list(map(int, input().split()))
num_move = []
for i in range(N):
    num_move.append([i+1, move_info[i]])

balloons_num = []

i = 0
while len(num_move) > 1:
    
    i %= len(num_move)

    balloons_num.append(num_move[i][0])
    move = num_move[i][1]
    num_move.pop(i)
    if move > 0:
        i += (move - 1)
    else:
        i += move + len(num_move)

balloons_num.append(num_move[0][0])
print(*balloons_num)
