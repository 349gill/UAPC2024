N, Q = map(int, input().split(" "))

names = []

for i in range(N):
    names.append(input())

for j in range(Q):
    matches = []
    inital = input()
    for i in names:
        x = i.split(" ")
        F, L = x[0][0], x[1][0]

        if F + L == inital:
            matches.append(i)
    if matches == []:
        print("nobody")
    elif len(matches) == 1:
        print(matches[0])
    else:
        print("ambiguous")