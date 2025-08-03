#%%
N, K = map(int, input().split())
students = {
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: []
}

for _ in range(N):
    s, y = map(int, input().split())
    students[y].append(s)

room_cnt = 0
for i in range(1, 7):
    woman = students[i].count(0)
    man = students[i].count(1)

    room_cnt += woman // K
    room_cnt += man // K 
    if woman % K != 0:
        room_cnt += 1
    if man % K != 0:
        room_cnt += 1

print(room_cnt)
