T = int(input())
for t in range(T):
    N = int(input())
    
    # 숫자 리스트로 받기
    nums = list(map(int, input().split()))
		
		# 숫자 정렬할 리스트
    ans = []
    
    # ans에 입력한 값을 없애 나가는 방식 사용 (while 구문 사용)
    while nums:
		    # max값, min값 초기 설정
        max_value = 0
        min_value = float('inf')
        
        # max값과 min값 업데이트
        for num in nums:
            if max_value < num:
                max_value = num
            if min_value > num:
                min_value = num
        # 최종적으로 나온 max값과 min값을 순서대로 입력
        ans.extend([max_value, min_value])
        
        # 이 과정을 반복해야 하므로 현재 max, min 값을 제거
        nums.remove(max_value)
        nums.remove(min_value)

    # 10개만 뽑아야하므로 리스트 슬라이싱 사용
    print(f'#{t+1}', end=" ")
    print(*ans[:10])

