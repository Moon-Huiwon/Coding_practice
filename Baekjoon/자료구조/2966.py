#%%
N = int(input())
answer_list = [char for char in input()]
adrian = ['A', 'B', 'C']
bruno = ['B','A', 'B', 'C']
goran = ['C', 'C', 'A', 'A', 'B', 'B']

name_list = ['Adrian', 'Bruno', 'Goran']

adrian_answer = []
bruno_answer = []
goran_answer = []

for i in range(N):
    adrian_answer.append(adrian[i % len(adrian)])
    bruno_answer.append(bruno[i % len(bruno)])
    goran_answer.append(goran[i % len(goran)])

scores = [0, 0, 0]
for i in range(N):
    if adrian_answer[i] == answer_list[i]:
        scores[0] += 1
    if bruno_answer[i] == answer_list[i]:
        scores[1] += 1
    if goran_answer[i] == answer_list[i]:
        scores[2] += 1

max_cnt = [score for score in scores if score == max(scores)]

print(max(scores))

if len(max_cnt) > 1:
    for i in range(3):
        if scores[i] == max(scores):
            print(name_list[i])
else:
    print(name_list[scores.index(max(scores))])
