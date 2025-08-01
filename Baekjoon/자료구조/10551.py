#%%
finger_cnt = [0] * 8
finger_string = ['1QAZ', '2WSX', '3EDC', '4RFV5TGB', '6YHN7UJM', '8IK,', '9OL.', '0P;/-[\'=]']

string = input()

for s in string:
    for i in range(len(finger_string)):
        if s in finger_string[i]:
            finger_cnt[i] += 1

for cnt in finger_cnt:
    print(cnt)
