# Minimum Spanning Tree
from heapq import heappush, heappop
INF = 1e9

N, M = list(map(int, input().split()))

min_heap = []
graph = [[] for i in range(N + 1)]
dist = [INF for i in range(N + 1)]
path = [-1 for i in range(N + 1)]
visited = [False for i in range(N + 1)]

def prim(src):
  global min_heap, grasph, dist, path, visited
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
  for i in range(1, N + 1):
    if path[i] == -1:
      continue
    res += dist[i]
  print(res)

for _ in range(M):
  i, j ,k = list(map(int, input().split())) 
  graph[i].append((k, j))
  graph[j].append((k, i))

prim(1)
print_dist()
