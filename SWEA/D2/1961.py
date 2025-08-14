T = int(input())

for test_num in range(T):
    # N값 받기
    N = int(input())
    # 행렬 만들기
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 회전 결과 넣는 곳
    answer = [[] for _ in range(N)]

    # 90도/180도/270도로 돌리기 때문에 3번 for문 돌리기
    for _ in range(3):
        
        # 현재 회전 결과 넣는 곳
        tmp = [[] for _ in range(N)]
        # 열별로 아래에서 위 순서로 값 저장하기
        for i in range(N-1, -1, -1):
            for j in range(N):
                tmp[j].append(arr[i][j])

        # 회전 결과를 answer에 저장하기
        for i in range(N):
            answer[i].append(str(''.join(map(str, tmp[i]))))

        # copy를 활용하여 arr 재할당
        # 90도로 돌아가있는 상태에서 90도로 돌리면 180도 이기 때문
        # 180도 돌아가있는 상태에서 90도 돌리면 270도 이기 때문
        arr = tmp.copy()
    print(f'#{test_num+1}')
    # 한줄에 작성하기 위해 join 활용 (띄어쓰기로 구분)
    for row in answer:
        print(' '.join(map(str, row)))