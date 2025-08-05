# #%%
# import sys
# sys.stdin = open('input.txt')

N, M = map(int, input().split())
start_W = ['W', 'B'] * (M//2 + M % 2)
start_B = ['B', 'W'] * (M//2 + M % 2)

board = [list(input()) for _ in range(N)]
result = []
for x in range(N - 7):
    for y in range(M - 7):
        start_W_cnt = 0
        start_B_cnt = 0

        for i in range(8):
            for j in range(8):
                if (x+i) % 2 == 0:
                    if board[x+i][y+j] != start_W[j]:
                        start_W_cnt += 1
                    if board[x+i][y+j] != start_B[j]:
                        start_B_cnt += 1
                else:
                    if board[x+i][y+j] != start_B[j]:
                        start_W_cnt += 1
                    if board[x+i][y+j] != start_W[j]:
                        start_B_cnt += 1
        result.extend([start_W_cnt, start_B_cnt])
print(min(result))



# %%
