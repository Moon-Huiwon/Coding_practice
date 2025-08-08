T = int(input())

for _ in range(T):
    # test_num과 문자열 길이 입력 받기
    case_num, case_length = map(str, input().split())
    # 영어로 구성된 문자열 받기
    numbers = list(map(str, input().split()))

    # 영어로 표시된 숫자를 index 순서대로 입력하여 리스트 생성
    eng_num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    num_dict = {}

    # enumerate를 활용하여 index와 eng_num을 연결하는 딕셔너리 생성
    for idx, eng in enumerate(eng_num):
        num_dict[eng] = idx

    # 영어로 구성된 문자열을 숫자로 변경
    change_numbers = [num_dict[num] for num in numbers]
    # 오름차순으로 변경
    change_numbers.sort()

    # 다시 영어로 변경하기 위한 dictionary 재구성 (num_dict의 key와 value를 변경하면 됨)
    # k는 key값 v는 value 값이므로 v: k로 변경
    reversed_num_dict = {v: k for k, v in num_dict.items()}

    # reversed_num_dict를 활용하여 숫자를 영어 문자로 변경
    answer = [reversed_num_dict[num] for num in change_numbers]

    print(f'{case_num}')
    print(*answer)