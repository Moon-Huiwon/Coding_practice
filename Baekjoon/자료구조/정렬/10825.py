N = int(input())

ans = []
for _ in range(N):
    name, kor, eng, math = map(str, input().split())
    
    kor = int(kor)
    eng = int(eng)
    math = int(math)

    ans.append((-kor, eng, -math, name))

ans.sort()

for _, _, _, name in ans:
    print(name)

#%%