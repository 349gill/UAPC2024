data = input().split()
n = int(data[0])
m = int(data[1])
edges = []
index = 2
for i in range(m):
    u = int(data[index])
    v = int(data[index + 1])
    edges.append((u, v))
    index += 2

def find_colouring(n, m, edges):
    from collections import defaultdict, deque
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    colours = [None] * (n + 1)
    def bfs(start):
        queue = deque([start])
        colours[start] = 1
        while queue:
            node = queue.popleft()
            available = {1, 2, 3}
            for neighbour in graph[node]:
                if colours[neighbour] in available:
                    available.remove(colours[neighbour])
            for neighbour in graph[node]:
                if colours[neighbour] is None:
                    colours[neighbour] = available.pop()
                    queue.append(neighbour)
    bfs(1)
    return colours[1:]

result = find_colouring(n, m, edges)
print(" ".join(map(str, result)))
