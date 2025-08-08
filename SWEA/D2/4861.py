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