for _ in range(10):
    T = int(input())
    # 사다리 데이터 입력
    arr = [list(map(int, input().split())) for _ in range(100)]
		
		# 사다리의 경우 행렬 0에서 시작하고, 해당 값이 1이어야 하기 때문에
		# 시작할 수 있는 index만 저장
    start_x = [idx for idx in range(100) if arr[0][idx] == 1]
		
		# 정답 확인하기 위한 변수 설정
    ans = 0
    
    # 시작할 수 있는 index에서만 출발
    for j in start_x:
    
		    # 출발 위치 설정
        cx, cy = (0, j)
        
        # 방문 여부 확인하기 위한 리스트 (지나갔는지 여부 확인)
        init_x = [[0] * 100 for _ in range(100)]
        
        # while 구문 사용하기 위한 설정
        q = []
        q.append([cx, cy])
        while q:
		        # 현재 위치 확인
            cx, cy = q.pop(0)
            
            # 현재 위치 방문했으므로 1로 업데이트 (방문했으면 1)
            init_x[cx][cy] = 1
						
						# 오른쪽으로 이동 가능한지 확인하고, 가능하면 이동
            if 0 <= cx < 100 and 0 <= cy+1 < 100 and arr[cx][cy+1] == 1 and init_x[cx][cy+1] == 0:
                cy += 1
                q.append([cx, cy]) # 이동할 수 있는 곳 q에 저장
                
            # 왼쪽으로 이동 가능한지 확인하고, 가능하면 이동
            elif 0 <= cx < 100 and 0 <= cy-1 < 100 and arr[cx][cy-1] == 1 and init_x[cx][cy-1] == 0:
                cy -= 1
                q.append([cx, cy]) # 이동할 수 있는 곳 q에 저장
            
            # 아래로 이동 가능한지 확인하고, 가능하면 이동 
            elif 0 <= cx+1 < 100 and 0 <= cy < 100 and arr[cx+1][cy] == 1 and init_x[cx+1][cy] == 0:
                cx += 1
                q.append([cx, cy]) # 이동할 수 있는 곳 q에 저장
            
            # 아래로 이동 가능한지 확인
            # 아래로 이동했을 때 값이 2이면 도착한 것이므로 break
            elif 0 <= cx+1 < 100 and 0 <= cy < 100 and arr[cx+1][cy] == 2 and init_x[cx+1][cy] == 0:
                cx += 1
                break
            
        # 마지막에 도착한 arr의 값이 2이면 해당 출발점이 정답
        if arr[cx][cy] == 2:
            ans = j
            break
    
    print(f'#{T} {ans}')
