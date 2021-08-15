# Possible Friends
INF = int(1e9)

def floyd(dist, m):
  for k in range(m):
    for i in range(m):
      if dist[i][k] == INF:
        continue
      for j in range(m):
        if dist[k][j] != INF and dist[i][j] > dist[i][k] + dist[k][j]:
          dist[i][j] = dist[i][k] + dist[k][j]

t = int(input())

for _ in range(t):
  graph = []
  line = input()
  m = len(line)
  graph.append(line)
  dist = [[INF for i in range(m)] for i in range(m)]
  for i in range(1, m):
    row = input()
    graph.append(row)

  for i in range(m):
    for j in range(m):
      if i == j:
        dist[i][j] = 0
      else:
        if graph[i][j] == 'Y':
          dist[i][j] = 1
  floyd(dist, m)
  id = 0
  max_posible_friends = 0
  for i in range(m):
    count = 0
    for j in range(m):
      if i == j:
        continue
      if dist[i][j] == 2:
        count += 1
    if count > max_posible_friends:
      max_posible_friends = count
      id = i
  print(id, max_posible_friends)



