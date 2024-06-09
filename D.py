x = input().split("\n")
size = int(x[0])
matrix = []

for i in range(1, size + 1):
    line = x[i].split()
    row = []
    for j in range(size):
        row.append(line[j])

def helper(row):
    return all(square == 'X' for square in line)

empty_positions = [(i, j) for i in range(size) for j in range(size) if matrix[i][j] == '.']
k = len(empty_positions)
total_ways = 0
for mask in range(2**k):
    new = [list(row) for row in matrix]
    for idx, (i, j) in enumerate(empty_positions):
        if (mask >> idx) & 1:
            new[i][j] = 'X'
        else:
            new[i][j] = 'O'
        
    row_x = any(helper(new[i]) for i in range(size))
    col_x = any(helper(new[i][j] for i in range(size)) for j in range(size))
    diag1_x = helper(new[i][i] for i in range(size))
    diag2_x = helper(new[i][size-i-1] for i in range(size))
    
    if row_x or col_x or diag1_x or diag2_x:
        total_ways += 1

print(total_ways)
