T = int(input())
for _ in range(T):
    string = list(input())
    for i in range(5):
        if i in [0, 4]:
            print('..#.'*len(string)+'.')
        elif i in [1, 3]:
            print('.#'*len(string)*2+'.')
        else:
            for s in string:
                print('#.'+ s + '.', end="")
            print('#')