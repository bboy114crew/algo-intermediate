# # Wormholes
# INF = int(1e9)

# def bell_man_ford(s, m, n, edge_list):
#   dist = [INF for index in range(n)]
#   dist[s] = 0
#   for i in range(1, n):
#     for j in range(m):
#       cx, cy, ct = edge_list[j]
#       if dist[cx] != INF and dist[cx] + ct < dist[cy]:
#         dist[cy] = dist[cx] + ct
#   for i in range(m):
#     cx, cy, ct = edge_list[i]
#     if dist[cx] != INF and dist[cx] + ct < dist[cy]:
#       return False
#   return True

# # Input
# c = int(input())

# for _ in range(c):
#   # n is the number of star systems a.k.a vertices
#   # m is the number of wormholes a.k.a edges
#   n, m = list(map(int, input().split()))

#   edge_list = []

#   for i in range(m):
#     x, y, t = list(map(int, input().split()))
#     edge_list.append((x, y, t))

#   # Run
#   res = bell_man_ford(0, m, n, edge_list)
#   if not res:
#     print('possible')
#   else:
#     print('not possible')

# Extended traffic
INF = int(1e9)
def bell_man_ford(s, m, n, edge_list):
  dist = [INF for index in range(n + 1)]
  dist[s] = 0
  for i in range(1, n):
    for j in range(m):
      cx, cy, ct = edge_list[j]
      if dist[cx] != INF and dist[cx] + ct < dist[cy]:
        dist[cy] = dist[cx] + ct

  for i in range(m):
    cx, cy, ct = edge_list[i]
    if dist[cx] != INF and dist[cx] + ct < dist[cy]:
      return (False, dist)
  return (True, dist)

t = int(input())

for case in range(t):
  input()
  n = int(input()) # vertices
  # n intergers denoting the busyness of the junctions
  vertices = [0]
  busyness_of_junctions = list(map(int, input().split()))
  vertices = [*vertices, *busyness_of_junctions]
  edge_list = []
  m = int(input()) # edges
  for i in range(m):
    u, v = list(map(int, input().split()))
    edge_list.append((u, v, (vertices[v] - vertices[u]) ** 3))
  q = int(input()) # number of queries
  queries = []
  for i in range(q):
    query = int(input())
    queries.append(query)
  result = bell_man_ford(1, m, n, edge_list)
  print('Case {}:'.format(case + 1))
  for query in queries:
    if result[0]:
      if result[1][query] > 2:
        if result[1][query] != INF:
          print(result[1][query])
        else:
          print('?')
      else:
        print('?')
    else:
      print('?')