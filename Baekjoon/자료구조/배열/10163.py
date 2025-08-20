#%%
# 서브태스크 53점
N = int(input())

matrix = [[0]*1001 for _ in range(1001)]

for num in range(N):
    x, y, width, height = map(int, input().split())
    for i in range(y, y+height):
        for j in range(x, x+width): # 이 부분에서 시간초과
            matrix[i][j] = num+1

for num in range(N):
    answer = 0
    for i in range(1001):
        answer += matrix[i].count(num+1)
    print(answer)

# %%
# 100점
N = int(input())

matrix = [[0]*1001 for _ in range(1001)]

for num in range(N):
    x, y, width, height = map(int, input().split())
    for i in range(y, y+height):
        matrix[i][x:(x+width)] = [num+1]*width # 슬라이싱 활용하여 시간 단축

for num in range(N):
    answer = 0
    for i in range(1001):
        answer += matrix[i].count(num+1)
    print(answer)
