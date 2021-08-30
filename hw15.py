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

# Connect the Campus
from heapq import heappush, heappop
INF = 1e9

def distance(A, B):
  x, y = A
  z, t = B
  return ((x - z) ** 2 + (y - t) ** 2) ** 0.5

def prim(src):
  global min_heap, graph, dist, path, visited
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
        path[v] = u
        heappush(min_heap, (w, v))

def print_dist():
  res = 0
  for i in range(1, N):
    if path[i] == -1:
      continue
    res += dist[i]
  print('{:.2f}'.format(res))

while True:
  try:
    N = int(input())
  except EOFError:
    break
  min_heap = []
  graph = [[] for i in range(N)]
  dist = [INF for i in range(N)]
  path = [-1 for i in range(N)]
  visited = [False for i in range(N)]
  points = []

  for _ in range(N):
    x, y = list(map(int, input().split()))
    points.append((x, y))
  for i in range(N):
    for j in range(i, N):
      w = distance(points[i], points[j])
      if i != j:
        graph[i].append((w, j))
        graph[j].append((w, i))

  M = int(input())
  for _ in range(M):
    A, B = list(map(int, input().split()))
    graph[A - 1].append((0, B - 1))
    graph[B - 1].append((0, A - 1))
  prim(0)
  print_dist()
