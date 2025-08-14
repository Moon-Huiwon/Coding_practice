#%%
T = int(input())

for t in range(T):
    N = int(input())
    # 저장하는 장소
    arr = []
    # 테스트 번호 출력
    print(f'#{t+1}')

    # N번 데이터가 주어진
    for i in range(N):
        # 문자와 개수 정보 받기
        string, cnt = map(str, input().split())
        cnt = int(cnt)

        # arr이 10개가 될때 까지 저장하고
        # 10개 넘어가면 print 하고
        # 다시 초기화해서 저장하도록 설정
        for _ in range(cnt):
            if len(arr) < 10:
                arr.append(string)
            else:
                print(''.join(map(str, arr)))
                arr = []
                arr.append(string)
        # 마지막에 돌아가는 건 그냥 그대로 출력
        # 마지막은 10개 미만이어도 출력할 수 있게
        if i == N-1:
            print(''.join(map(str, arr)))

# %%
