N, K = map(int, input().split(" "))

count = 0
for i in range(N):
    l = []
    x = input().split(" ")
    for j in range(K):
        if x[j] in l:
            count += 1
        else:
            l.append(x[j])

print(count)