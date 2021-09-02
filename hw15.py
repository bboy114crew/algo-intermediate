# # Minimum Spanning Tree
# from heapq import heappush, heappop
# INF = 1e9

# N, M = list(map(int, input().split()))

# min_heap = []
# graph = [[] for i in range(N + 1)]
# dist = [INF for i in range(N + 1)]
# path = [-1 for i in range(N + 1)]
# visited = [False for i in range(N + 1)]

# def prim(src):
#   global min_heap, graph, dist, path, visited
#   dist[src] = 0
#   heappush(min_heap, (dist[src], src))
#   while len(min_heap) != 0:
#     top = heappop(min_heap)
#     u = top[1]
#     if visited[u]:
#       continue
#     visited[u] = True

#     for (w, v) in graph[u]:
#       if visited[v] == False and w < dist[v]:
#         dist[v] = w
#         path[v] = u
#         heappush(min_heap, (w, v))

# def print_dist():
#   res = 0
#   for i in range(1, N + 1):
#     if path[i] == -1:
#       continue
#     res += dist[i]
#   print(res)

# for _ in range(M):
#   i, j ,k = list(map(int, input().split())) 
#   graph[i].append((k, j))
#   graph[j].append((k, i))

# prim(1)
# print_dist()

# # Connect the Campus
# from heapq import heappush, heappop
# INF = 1e9

# def distance(A, B):
#   x, y = A
#   z, t = B
#   return ((x - z) ** 2 + (y - t) ** 2) ** 0.5

# def prim(src):
#   global min_heap, graph, dist, path, visited
#   dist[src] = 0
#   heappush(min_heap, (dist[src], src))
#   while len(min_heap) != 0:
#     top = heappop(min_heap)
#     u = top[1]
#     if visited[u]:
#       continue
#     visited[u] = True

#     for (w, v) in graph[u]:
#       if visited[v] == False and w < dist[v]:
#         dist[v] = w
#         path[v] = u
#         heappush(min_heap, (w, v))

# def print_dist():
#   res = 0
#   for i in range(1, N):
#     if path[i] == -1:
#       continue
#     res += dist[i]
#   print('{:.2f}'.format(res))

# while True:
#   try:
#     N = int(input())
#   except EOFError:
#     break
#   min_heap = []
#   graph = [[] for i in range(N)]
#   dist = [INF for i in range(N)]
#   path = [-1 for i in range(N)]
#   visited = [False for i in range(N)]
#   points = []

#   for _ in range(N):
#     x, y = list(map(int, input().split()))
#     points.append((x, y))
#   for i in range(N):
#     for j in range(i, N):
#       w = distance(points[i], points[j])
#       if i != j:
#         graph[i].append((w, j))
#         graph[j].append((w, i))

#   M = int(input())
#   for _ in range(M):
#     A, B = list(map(int, input().split()))
#     graph[A - 1].append((0, B - 1))
#     graph[B - 1].append((0, A - 1))
#   prim(0)
#   print_dist()

# # Cobbled streets
# from heapq import heappush, heappop
# INF = 1e9

# def prim(src):
#   global min_heap, graph, dist, path, visited
#   dist[src] = 0
#   heappush(min_heap, (dist[src], src))
#   while len(min_heap) != 0:
#     top = heappop(min_heap)
#     u = top[1]
#     if visited[u]:
#       continue
#     visited[u] = True

#     for (w, v) in graph[u]:
#       if visited[v] == False and w < dist[v]:
#         dist[v] = w
#         path[v] = u
#         heappush(min_heap, (w, v))

# def print_dist(p):
#   res = 0
#   for i in range(1, N + 1):
#     if path[i] == -1:
#       continue
#     res += dist[i]
#   print(res * p)

# t = int(input())
# for _ in range(t):
#   p = int(input())
#   N = int(input())
#   M = int(input())

#   min_heap = []
#   graph = [[] for i in range(N + 1)]
#   dist = [INF for i in range(N + 1)]
#   path = [-1 for i in range(N + 1)]
#   visited = [False for i in range(N + 1)]
#   for _ in range(M):
#     i, j ,k = list(map(int, input().split())) 
#     graph[i].append((k, j))
#     graph[j].append((k, i))

#   prim(1)
#   print_dist(p)

# Simulate Network
from heapq import heappush, heappop
INF = 1e9

def prim(src):
  global graph, dist, path, visited
  min_heap = []
  dist[src] = 0
  heappush(min_heap, (dist[src], src))
  while len(min_heap) != 0:
    top = heappop(min_heap)
    u = top[1]
    if visited[u]:
      continue
    visited[u] = True

    for (w, v) in graph[u]:
      if visited[v] == False and w < dist[v]:
        dist[v] = w
        heappush(min_heap, (w, v))

def print_dist():
  global sorted_dist
  res = 0
  for i in range(len(sorted_dist)):
    res += sorted_dist[i]
  print(res)

N, M = list(map(int, input().split()))
graph = [[] for i in range(N + 1)]
dist = [INF for i in range(N + 1)]
visited = [False for i in range(N + 1)]

for _ in range(M):
  A, B ,L = list(map(int, input().split())) 
  graph[A].append((L, B))
  graph[B].append((L, A))

prim(1)

Q = int(input())
C = list(map(int, input().split()))
C.sort()

final = dist[2:N + 1]
sorted_dist = []
for i in range(len(final)):
  if final[i] != INF:
    sorted_dist.append(final[i])

sorted_dist.sort(reverse=True)

for i in range(len(sorted_dist)):
  if i == Q:
    break
  if sorted_dist[i] > C[i]:
    sorted_dist[i] = C[i] 

print_dist()

# # Special Subtree
# from heapq import heappush, heappop
# INF = 1e9

# N, M = list(map(int, input().split()))

# min_heap = []
# graph = [[] for i in range(N + 1)]
# dist = [INF for i in range(N + 1)]
# path = [-1 for i in range(N + 1)]
# visited = [False for i in range(N + 1)]

# def prim(src):
#   global min_heap, graph, dist, path, visited
#   dist[src] = 0
#   heappush(min_heap, (dist[src], src))
#   while len(min_heap) != 0:
#     top = heappop(min_heap)
#     u = top[1]
#     if visited[u]:
#       continue
#     visited[u] = True

#     for (w, v) in graph[u]:
#       if visited[v] == False and w < dist[v]:
#         dist[v] = w
#         path[v] = u
#         heappush(min_heap, (w, v))

# def print_dist():
#   global dist, N
#   res = 0
#   for i in range(1, N + 1):
#     if path[i] == -1:
#       continue
#     res += dist[i]
#   print(res)

# for _ in range(M):
#   x, y ,r = list(map(int, input().split())) 
#   graph[x].append((r, y))
#   graph[y].append((r, x))

# S = int(input())
# prim(S)

# print_dist()