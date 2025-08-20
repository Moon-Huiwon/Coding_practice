#%%
import copy
# import sys
# sys.stdin = open('input.txt')

N, M, R = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
R_num = list(map(int, input().split()))

while R_num:
    number = R_num.pop(0)
    
    # **row값과 col 값 초기화 필수
    N = len(matrix)
    M = len(matrix[0])

    # 상하반전
    if number == 1:
        answer = []
        for i in range(N-1, -1, -1):
            answer.append(matrix[i])
        
        matrix = copy.deepcopy(answer)
        
    # 좌우반전
    elif number == 2:
        answer = []
        for i in range(N):
            answer.append(matrix[i][::-1])
        
        matrix = copy.deepcopy(answer)
    
    # 오른쪽 90도 회전
    elif number == 3:
        answer = []
        for j in range(M):
            tmp = []
            for i in range(N-1, -1, -1):
                tmp.append(matrix[i][j])
            answer.append(tmp)
        
        matrix = copy.deepcopy(answer)
    
    # 왼쪽 90도 회전
    elif number == 4:
        answer = []
        for j in range(M-1, -1, -1):
            tmp = []
            for i in range(N):
                tmp.append(matrix[i][j])
            answer.append(tmp)
        
        matrix = copy.deepcopy(answer)
    
    # 4개의 구간으로 나누고 이동 (오른쪽, 아래, 왼쪽, 위 이동)
    elif number == 5:
        answer = [[0] * M  for _ in range(N)]
        five_distance = [(0, M//2), (N//2, 0), (-N//2, 0), (0, -M//2)]
        for i in range(0, N, N//2):
            for j in range(0, M, M//2):
                
                di, dj = five_distance.pop(0)

                for p in range(N//2):
                    for q in range(M//2):
                        ni, nj = i + p + di, j + q + dj

                        answer[ni][nj] = matrix[i+p][j+q]
        
        matrix = copy.deepcopy(answer)
    
    # 4개의 구간으로 나누고 이동 (아래, 오른쪽, 위, 왼쪽 이동)
    else:
        answer = [[0] * M  for _ in range(N)]
        six_distance = [(N//2, 0), (0, -M//2), (0, M//2), (-N//2, 0)]
        for i in range(0, N, N//2):
            for j in range(0, M, M//2):
                
                di, dj = six_distance.pop(0)

                for p in range(N//2):
                    for q in range(M//2):
                        ni, nj = i + p + di, j + q + dj

                        answer[ni][nj] = matrix[i+p][j+q]
        
        matrix = copy.deepcopy(answer)

for arr in matrix:
    print(*arr)



#%%

# 테스트 케이스 (디버깅 하며 하나씩 작동 코드 작성)
"""
N = 4
M = 6
test = [[1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18], [19,20,21,22,23,24]]


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
answer = [[0] * M  for _ in range(N)]
five_distance = [(0, M//2), (N//2, 0), (-N//2, 0), (0, -M//2)]
for i in range(0, N, N//2):
    for j in range(0, M, M//2):
        
        di, dj = five_distance.pop(0)

        for p in range(N//2):
            for q in range(M//2):
                ni, nj = i + p + di, j + q + dj

                answer[ni][nj] = test[i+p][j+q]


# R_num == 6이면 아래, 오른쪽, 위, 왼쪽 이동
answer = [[0] * M  for _ in range(N)]
six_distance = [(N//2, 0), (0, -M//2), (0, M//2), (-N//2, 0)]
for i in range(0, N, N//2):
    for j in range(0, M, M//2):
        
        di, dj = six_distance.pop(0)

        for p in range(N//2):
            for q in range(M//2):
                ni, nj = i + p + di, j + q + dj

                answer[ni][nj] = test[i+p][j+q]

"""