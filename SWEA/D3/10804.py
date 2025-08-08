T = int(input())
# 거울에 비췄을 때 바뀌는 문자 딕셔너리 저장
replace_dict = {
    'b': 'd',
    'd': 'b',
    'p': 'q',
    'q': 'p',

}
for t in range(T):
    # 문자열 받기
    str = list(input())
    # 거꾸로 재설정
    str = str[::-1]

    # **주의 replace를 활용해서 한꺼번에 바꾸면 안됨
    # 한글자씩 차례대로 replace_dict를 활용하여 문자 변경
    for i in range(len(str)):
        str[i] = replace_dict[str[i]]

    print(f'#{t+1} {"".join(str)}')
