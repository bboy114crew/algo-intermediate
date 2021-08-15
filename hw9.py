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

INF = int(1e9)
def bell_man_ford(s, m, n, edge_list):
  dist = [INF for index in range(n + 1)]
  dist[s] = 0
  for i in range(n - 1): # n-1 thôi là đủ
    for j in range(m):
      cx, cy, ct = edge_list[j]
      if dist[cx] != INF and dist[cx] + ct < dist[cy]:
        dist[cy] = dist[cx] + ct

  # đánh dấu nhưng đỉnh bị ảnh hưởng bởi chu trình âm
  for i in range(n - 1): 
    for j in range(m):
      cx, cy, ct = edge_list[j]
      # nếu đỉnh cy còn update được dist thì đánh dấu lại
      if dist[cx] != INF and dist[cx] + ct < dist[cy]:
        dist[cy] = -INF # dist gán bằng âm vô cùng --> bị ảnh hưởng bởi chu trình âm

  return dist

while True:
  n, m, q, s = list(map(int, input().split()))
  if n == 0 and m == 0 and q == 0 and s == 0:
    break
  edge_list = []
  for _ in range(m):
    u, v, w = list(map(int, input().split()))
    edge_list.append((u, v, w))
  
  queries = []
  for _ in range(q):
    query = int(input())
    queries.append(query)

  dist = bell_man_ford(s, m, n, edge_list)
  for query in queries:
    if dist[query] == -INF:
      print('-Infinity')
    elif dist[query] == INF:
      print('Impossible')
    else:
      print(dist[query])
  print()
