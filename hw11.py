# # Possible Friends
# INF = int(1e9)

# def floyd(dist, m):
#   for k in range(m):
#     for i in range(m):
#       if dist[i][k] == INF:
#         continue
#       for j in range(m):
#         if dist[k][j] != INF and dist[i][j] > dist[i][k] + dist[k][j]:
#           dist[i][j] = dist[i][k] + dist[k][j]

# t = int(input())

# for _ in range(t):
#   graph = []
#   line = input()
#   m = len(line)
#   graph.append(line)
#   dist = [[INF for i in range(m)] for i in range(m)]
#   for i in range(1, m):
#     row = input()
#     graph.append(row)

#   for i in range(m):
#     for j in range(m):
#       if i == j:
#         dist[i][j] = 0
#       else:
#         if graph[i][j] == 'Y':
#           dist[i][j] = 1
#   floyd(dist, m)
#   id = 0
#   max_posible_friends = 0
#   for i in range(m):
#     count = 0
#     for j in range(m):
#       if i == j:
#         continue
#       if dist[i][j] == 2:
#         count += 1
#     if count > max_posible_friends:
#       max_posible_friends = count
#       id = i
#   print(id, max_posible_friends)

# Meeting Prof. Miguel ...
INF = int(1e9)
MAX = 26

def add_edge(direction, X, Y, cost, array):
  i = ord(X) - ord('A')
  j = ord(Y) - ord('A')
  array[i][j] = min(cost, array[i][j])
  if (direction == 'B'):
    array[j][i] = min(cost, array[j][i])

def floyd(dist, m):
  for k in range(m):
    for i in range(m):
      if dist[i][k] == INF:
        continue
      for j in range(m):
        if dist[k][j] != INF and dist[i][j] > dist[i][k] + dist[k][j]:
          dist[i][j] = dist[i][k] + dist[k][j]

while True:
  e = int(input())
  if e == 0:
    break

  young_cost = [[INF for i in range(MAX)] for i in range(MAX)]
  old_cost = [[INF for i in range(MAX)] for i in range(MAX)]

  for i in range(MAX):
    for j in range(MAX):
      young_cost[i][i] = 0
      old_cost[i][i] = 0

  for _ in range(e):
    age, direction, X, Y, cost = list(input().split())
    if age == 'Y':
      add_edge(direction, X, Y, int(cost), young_cost)
    else:
      add_edge(direction, X, Y, int(cost), old_cost)

  floyd(young_cost, MAX)
  floyd(old_cost, MAX)

  cost = INF - 1
  results = []

  young_s, old_s = list(input().split())

  for meet in range(MAX):
    i = ord(young_s) - ord('A')
    j = ord(old_s) - ord('A')
    current_cost = young_cost[i][meet] + old_cost[j][meet]

    if current_cost < cost:
      results = []
      results.append(chr(meet + ord('A')))
      cost = current_cost
    elif current_cost == cost:
      results.append(chr(meet + ord('A')))

  results.sort()
  if len(results) > 0:
    print(cost, *results)
  else:
    print('You will never meet.')

