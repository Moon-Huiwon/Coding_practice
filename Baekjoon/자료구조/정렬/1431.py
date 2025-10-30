N = int(input())

tmp = []
for _ in range(N):
    num = input()
    sum_num = 0
    for i in num:
        if i in [str(i) for i in range(10)]:
            sum_num += int(i)
    tmp.append((len(num), sum_num, num))

sorted_tmp = sorted(tmp)
for _, _, num in sorted_tmp:
    print(num)
