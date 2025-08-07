T = int(input())

for t in range(T):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
		
		# arr에 넣을 번호 설정(초기값 1)
    answer = 1
    
    # delta 설정 (오른쪽, 아래, 왼쪽, 위)
    # 이동 순서가 있기 때문에 리스트에 넣는 순서 중요***
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
		
		# 출발점 0, 0으로 설정
    x, y = (0, 0)
    
    # 이동 경로 설정
    d_x, d_y = directions[0]
    
    # 이동 경로가 반복적으로 돌아가기 때문에 뒤에 추가 삽입
    directions.append(directions.pop(0))
		
    for _ in range(N*N):
		    # arr 위치에 숫자 입력
        arr[x][y] = answer
        
        # 숫자+1로 업데이트
        answer += 1
				
				# 다음 숫자 들어갈 곳 설정 (next_x, next_y)
        n_x, n_y = x + d_x, y + d_y
				
				# 설정된 위치가 범위 외에 있거나 이미 숫자가 들어있을 경우 방향 재설정
				# n_x, n_y 값도 재설정
        if not (0 <= n_x < N and 0 <= n_y < N and arr[n_x][n_y] == 0):
            d_x, d_y = directions[0]
            directions.append(directions.pop(0))
            n_x, n_y = x + d_x, y + d_y
        
        # 현재 위치로 업데이트
        x, y = n_x, n_y
    
    print(f'#{t+1}')
    for row in arr:
        print(' '.join(map(str, row)))

