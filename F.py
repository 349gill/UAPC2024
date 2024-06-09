data = input().split()

n = int(data[0])
m = int(data[1])
C = int(data[2])

def can_blow_out(mid, n, m, C, efforts):
    per_guest = mid // n
    extra = mid % n
    total_effort = 0

    for guest in range(n):
        candles_to_blow = per_guest + (1 if guest < extra else 0)
        if candles_to_blow > m:
            return False
        
        guest_efforts = sorted(efforts[guest])
        total_effort += sum(guest_efforts[:candles_to_blow])
        if total_effort > C:
            return False

    return total_effort <= C

def max_candles(n, m, C, efforts):
    left = 0
    right = n * m
    max_blow_out = 0

    while left <= right:
        mid = (left + right) // 2
        if can_blow_out(mid, n, m, C, efforts):
            max_blow_out = mid
            left = mid + 1
        else:
            right = mid - 1

    return max_blow_out

efforts = []
index = 3
for i in range(n):
    efforts.append(list(map(int, data[index:index + m])))
    index += m

print(max_candles(n, m, C, efforts))
