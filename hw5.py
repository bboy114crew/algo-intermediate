import queue

# Breadth First Search: Shortest Reach
q = int(input())

def bfs_shortest_reach(q):
  for i in range(q):
    nm = list(map(int, input().split()))
    n = nm[0]
    m = nm[1]

    visited = [False] * (n + 1)
    dist = [-1] * (n + 1)

    adj_list = [[]] * (n + 1)

    for j in range(m):
      edge = list(map(int, input().split()))
      adj_list[edge[0]].append(edge[1])
      adj_list[edge[1]].append(edge[0])

    q = queue.Queue()
    start = int(input())
    visited[start] = True
    q.put(start)
    dist[start] = 0
    while not q.empty():
      u = q.get()
      for v in adj_list[u]:
        if (not visited[v]):
          visited[v] = True
          q.put(v)
          dist[v] = dist[u] + 6
    result = ''
    for j in range(1, len(dist)):
      if (j != start):
        result = result + str(dist[j]) + " "
    print(result)

bfs_shortest_reach(q)