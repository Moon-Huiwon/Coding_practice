#%%
# 틀린 코드
# 동일한 나이일때 입력된 순서대로 정렬을 못했음.

"""
N = int(input())

dictionary = {}

for _ in range(N):
    age, name = map(str, input().split())
    dictionary[name] = int(age)

sorted_dict = dict(sorted(dictionary.items(), key=lambda x: x[1]))

for key, value in sorted_dict.items():
    print(value, key)
"""
#%%
N = int(input())

people = []
for i in range(N):
    age, name = map(str, input().split())
    people.append((int(age), name, i))

people.sort(key=lambda x: (x[0], x[2]))

for age, name, _ in people:
    print(age, name)