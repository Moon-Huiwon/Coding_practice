T = int(input())
for t in range(T):
    # 문자열 input 받기
    A, B = map(str, input().split())
    # cnt 변수 생성하여 답 도출
    cnt = 0
    # A 문자열에 B 문자열이 몇개 들어있는지 확인하여 cnt에 더해주기
    cnt += A.count(B)
    # B 문자열을 사용했으므로 B 문자열을 없애주기
    A = A.replace(B, '')
    # 남아있는 철자 수를 cnt에 더해주기 (남아있는 철자 수 만큼 타이핑해야하기 때문)
    cnt += len(A)
    print(f'#{t+1} {cnt}')
