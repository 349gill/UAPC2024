N = int(input())
potato = gravy = lucky = 1

for i in range(N):
    line = input().split(" ")
    if line[0] == 'P':
        if potato < gravy:
            potato += int(line[1])
            if potato >= gravy:
                lucky += 1
        else:
             potato += int(line[1])
    if line[0] == 'G':
        if gravy < potato:
            old_gravy = gravy
            gravy += int(line[1])
            if gravy >= potato:
                lucky += (potato - old_gravy)
        else:
            gravy += int(line[1])
print(lucky)