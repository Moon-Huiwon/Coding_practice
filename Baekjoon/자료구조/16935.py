#%%
N, M, R = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
R_num = list(int, input().split())

# test
N = 4
M = 6
test = [[1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18]]


# R_num == 1이면 상하반전
answer = []
for i in range(N-1, -1, -1):
    answer.append(test[i])

# R_num == 2이면 좌우반전
answer = []
for i in range(N):
    answer.append(test[i][::-1])

# R_num == 3이면 오른쪽 90도 회전
answer = []
for j in range(M):
    tmp = []
    for i in range(N-1, -1, -1):
        # print(i, j)
        # print(test[i][j])
        tmp.append(test[i][j])
    answer.append(tmp)

# R_num == 4이면 왼쪽 90도 회전
answer = []
for j in range(M-1, -1, -1):
    tmp = []
    for i in range(N):
        tmp.append(test[i][j])
    answer.append(tmp)

# R_num == 5이면 오른쪽, 아래, 왼쪽, 위 이동
five_distance = [(0, M//2), (N//2, 0), (0, -M//2), (-N//2, 0)]
# answer = []
# for i in range(N):


# R_num == 6이면 아래, 오른쪽, 위, 왼쪽 이동

