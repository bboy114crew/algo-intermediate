# Tìm đường đi tốt nhất theo 1 tiêu chí nào đó, thì bellman có thể phát hiện chu trình mà làm cho độ "tốt" luôn tăng

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

# # Extended traffic
# INF = int(1e9)
# def bell_man_ford(s, m, n, edge_list):
#   dist = [INF for index in range(n + 1)]
#   dist[s] = 0
#   for i in range(n - 1): # n-1 thôi là đủ
#     for j in range(m):
#       cx, cy, ct = edge_list[j]
#       if dist[cx] != INF and dist[cx] + ct < dist[cy]:
#         dist[cy] = dist[cx] + ct

#   # đánh dấu nhưng đỉnh bị ảnh hưởng bởi chu trình âm
#   for i in range(n - 1): 
#     for j in range(m):
#       cx, cy, ct = edge_list[j]
#       # nếu đỉnh cy còn update được dist thì đánh dấu lại
#       if dist[cx] != INF and dist[cx] + ct < dist[cy]:
#         dist[cy] = -INF # dist gán bằng âm vô cùng --> bị ảnh hưởng bởi chu trình âm

#   return dist
 
# t = int(input())
 
# for case in range(t):
#   input()
#   n = int(input()) # vertices
#   # n intergers denoting the busyness of the junctions
#   vertices = [0]
#   busyness_of_junctions = list(map(int, input().split()))
#   vertices = [*vertices, *busyness_of_junctions]
#   edge_list = []
#   m = int(input()) # edges
#   for i in range(m):
#     u, v = list(map(int, input().split()))
#     edge_list.append((u, v, (vertices[v] - vertices[u]) ** 3))
#   q = int(input()) # number of queries
#   queries = []
#   for i in range(q):
#     query = int(input())
#     queries.append(query)
#   dist = bell_man_ford(1, m, n, edge_list)
#   print('Case {}:'.format(case + 1))
#   for query in queries:
#     if 3 <= dist[query] < INF:
#       print(dist[query])
#     else:
#       print('?')


# # XYZZY
# import queue
# INF = int(1e9)

# def hasPathBFS(s, n, edge_list):
#   visited = [False] * (n + 1)
#   q = queue.Queue()
#   q.put(s)
#   visited[s] = True

#   while not q.empty():
#     u = q.get()

#     for edge in edge_list:
#       s, t = edge
#       if s == u:
#         if not visited[t]:
#           visited[t] = True
#           q.put(t)
        
#         if t == n:
#           return True
#   return False


# def bell_man_ford(s, n, edge_list, rooms_point):
#   dist = [-INF for index in range(n + 1)]
#   dist[s] = 100
#   for i in range(n - 1):
#     for edge in edge_list:
#       cx, cy = edge
#       if dist[cx] > 0:
#         dist[cy] = max(dist[cy], dist[cx] + rooms_point[cy])
#   for edge in edge_list:
#     cx, cy = edge
#     if dist[cx] > 0 and dist[cx] + rooms_point[cy] > dist[cy] and hasPathBFS(cx, n, edge_list):
#       return True
#   return dist[n] > 0

# while True:
#   n = int(input())
#   if n == -1:
#     break
#   edge_list = []
#   adj_list = [[] for index in range(n + 1)]
#   rooms_point = [0 for index in range(n + 1)]

#   for i in range(n):
#     w, s, *a = list(map(int, input().split()))
#     current_room = i + 1
#     rooms_point[current_room] = w
#     adj_list[current_room] = a
    
#   for i in range(len(adj_list)):
#     if i != 0:
#       for j in adj_list[i]:
#         edge_list.append((i, j))
#   can_win = bell_man_ford(1, n, edge_list, rooms_point)
#   if can_win:
#     print('winnable')
#   else:
#     print('hopeless')

# 106 Miles To Chicago
'''
As they are on a mission from God,
you should help them find the safest way to Chicago.
In this problem, the safest way is considered to be the route which maximises the probability that they are not caught.
'''

'''
Nếu một công việc nào đó phải hoàn thành qua nn giai đoạn liên tiếp, trong đó:
Phương án thứ 1 có m_1
Phương án thứ 2 có m_2
…
Phương án thứ n có m_n
Khi đó sẽ có m_1 * m_2 * ... * m_n cách để hoàn thành công việc được cho.
'''
# def bell_man_ford(s, n, graph):
#   dist = [-1.0 for index in range(n + 1)]
#   dist[s] = 1.0
#   for _ in range(n - 1): # loop n-1 times
#     for edge in graph:
#       u, v, r = edge
#       dist[u] = max(dist[u], dist[v] * r)
#       dist[v] = max(dist[v], dist[u] * r)
#   return dist[n]

# while True:
#   line = list(map(int, input().split()))
#   if len(line) == 1:
#     break
#   # n is the number of intersections
#   # m is the number of streets to be considered.
#   n, m = line
#   graph = []
#   for _ in range(m):
#     a, b, p = list(map(int, input().split()))
#     graph.append((a, b, p / 100))

#   result = bell_man_ford(1, n, graph)
#   print('{:.6f} percent'.format(result * 100))

# Single source shortest path, negative weights

# INF = int(1e9)
# def bell_man_ford(s, m, n, edge_list):
#   dist = [INF for index in range(n + 1)]
#   dist[s] = 0
#   for i in range(n - 1): # n-1 thôi là đủ
#     for j in range(m):
#       cx, cy, ct = edge_list[j]
#       if dist[cx] != INF and dist[cx] + ct < dist[cy]:
#         dist[cy] = dist[cx] + ct

#   # đánh dấu nhưng đỉnh bị ảnh hưởng bởi chu trình âm
#   for i in range(n - 1): 
#     for j in range(m):
#       cx, cy, ct = edge_list[j]
#       # nếu đỉnh cy còn update được dist thì đánh dấu lại
#       if dist[cx] != INF and dist[cx] + ct < dist[cy]:
#         dist[cy] = -INF # dist gán bằng âm vô cùng --> bị ảnh hưởng bởi chu trình âm

#   return dist

# while True:
#   n, m, q, s = list(map(int, input().split()))
#   if n == 0 and m == 0 and q == 0 and s == 0:
#     break
#   edge_list = []
#   for _ in range(m):
#     u, v, w = list(map(int, input().split()))
#     edge_list.append((u, v, w))
  
#   queries = []
#   for _ in range(q):
#     query = int(input())
#     queries.append(query)

#   dist = bell_man_ford(s, m, n, edge_list)
#   for query in queries:
#     if dist[query] == -INF:
#       print('-Infinity')
#     elif dist[query] == INF:
#       print('Impossible')
#     else:
#       print(dist[query])
#   print()

# # Monk's Business Day
# INF = int(1e9)

# def bell_man_ford(s, n, edge_list):
#   dist = [INF for index in range(n + 1)]
#   dist[s] = 0
#   for i in range(n):
#     for edge in edge_list:
#       cx, cy, cw = edge
#       if dist[cx] != INF and dist[cx] + cw < dist[cy]:
#         dist[cy] = dist[cx] + cw
#         if i == n - 1:
#           return True
#   return False

# t = int(input())

# for _ in range(t):
#   n, m = list(map(int, input().split()))
#   edge_list = []
#   for i in range(m):
#     u, v, w = list(map(int, input().split()))
#     edge_list.append((u, v, -w))
  
#   result = bell_man_ford(1, n, edge_list)

#   if result:
#     print('Yes')
#   else:
#     print('No')

# Alice in Amsterdam, I mean Wonderland

INF = (2 ** 30) * 100 + 7

def bell_man_ford(s):
  dist[s][s] = 0

  for i in range(n - 1):
    for edge in graph:
      u, v, w = edge
      if dist[s][u] != INF and dist[s][u] + w < dist[s][v]:
        dist[s][v] = dist[s][u] + w

  for i in range(n - 1):
    for edge in graph:
      u, v, w = edge
      if dist[s][u] != INF and dist[s][u] + w < dist[s][v]:
        dist[s][v] = -INF

tc = 1
while True:
  n = int(input())
  if n == 0:
    break

  monuments = []
  graph = []
  dist = [[INF for i in range(n)] for i in range(n)]
  for i in range(n):
    name, *weights = input().split()
    monuments.append(name)
    for j in range(n):
      w = int(weights[j])
      if i != j and w == 0:
        continue
      if i == j and w >= 0:
        w = 0
      graph.append((i, j, w))

  for i in range(n):
    bell_man_ford(i)

  print('Case #{}:'.format(tc))
  tc += 1
  q = int(input())

  for _ in range(q):
    u, v = map(int, input().split())
    if dist[u][v] <= -INF:
      print('NEGATIVE CYCLE')
    elif dist[u][v] == INF:
      print('{}-{} {}'.format(monuments[u], monuments[v], 'NOT REACHABLE'))
    else:
      print('{}-{} {}'.format(monuments[u], monuments[v], dist[u][v]))

# # Maelstrom
# INF = int(1e9)
# def bell_man_ford(s, n, dist, graph):
#   dist[s] = 0

#   for i in range(n - 1):
#     for edge in graph:
#       u, v, w = edge
#       dist[v] = min(dist[v], dist[u] + w)

# n = int(input())
# dist = [INF for index in range(n + 1)]
# graph = []
 
# for i in range(2, n + 1):
#   line = input().split()

#   for j in range(1, i):
#     if line[j - 1] != 'x':
#       w = int(line[j - 1])
#       graph.append((i, j, w))
#       graph.append((j, i, w))
 
# bell_man_ford(1, n, dist, graph)
 
# res = 0
# for i in range(1, n + 1):
#   res = max(res, dist[i])
# print(res)