#%%
# ***ord 활용하는 법 생각하기***
s1_alphabet = [0]*26
s2_alphabet = [0]*26

for s in input():
    s1_alphabet[ord(s) - 97] += 1

for s in input():
    s2_alphabet[ord(s) - 97] += 1

answer = 0
for i in range(26):
    answer += abs(s1_alphabet[i] - s2_alphabet[i])

print(answer)
# %%
