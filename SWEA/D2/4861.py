
# reversed, [::-1] 사용 없이
T = int(input())
for t in range(T):
    # N*N 행렬과 M길이 회문을 찾기 위한 변수 받기
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    for i in range(N):
        for j in range(N-M+1):
            # 가로에 M 길이의 회문이 있으면 출력
            row_tmp = arr[i][j:j+M]

            reversed_row_tmp = []
            for p in range(len(row_tmp)-1, -1, -1):
                reversed_row_tmp.append(row_tmp[p])

            if row_tmp == reversed_row_tmp:
                print(f"#{t + 1} {''.join(row_tmp)}")
                break

            col_tmp = []
            for p in range(M):
                col_tmp.append(arr[j+p][i])

            reversed_col_tmp = []
            for p in range(len(col_tmp)-1, -1, -1):
                reversed_col_tmp.append(col_tmp[p])

            if col_tmp == reversed_col_tmp:
                print(f"#{t + 1} {''.join(col_tmp)}")

# [::-1] 사용하여 코드 작성
T = int(input())

for t in range(T):
    # N*N 행렬과 M길이 회문을 찾기 위한 변수 받기
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    for i in range(N):
        for j in range(N-M+1):

            # 가로에 M 길이의 회문이 있으면 출력
            if arr[i][j:j+M] == arr[i][j:j+M][::-1]:
                print(f"#{t+1} {''.join(arr[i][j:j+M])}")
                break

            # 세로에 M 길이의 회문이 있으면 출력
            else:
                tmp = []
                for p in range(M):
                    tmp.append(arr[j+p][i])
                if tmp == tmp[::-1]:
                    print(f"#{t + 1} {''.join(tmp)}")
