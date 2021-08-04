# Travelling Cost
from heapq import heappush, heappop
def travelling_cost(s):
  global graph, destinies, u, dist

  h = []

  heappush(h, (s, 0))

  dist[0] = 0

  while len(h):
    top = heappop(h)
    b, w = top

    for neighbor in graph[b]:
      b_n, w_n = neighbor
      if w_n + w < dist[b_n]:
        dist[b_n] = w_n + w
        heappush(h, (b_n, dist[b_n]))

n = int(input())
INF = int(1e9)

graph = [[] for index in range(100005)]
for _ in range(n):
  a, b, w = list(map(int, input().split()))
  graph[a].append((b, w))
  graph[b].append((a, w))

u = int(input())
q = int(input())

destinies = []
dist = [INF for index in range(100005)]
for _ in range(q):
  d = int(input())
  destinies.append(d)

travelling_cost(u)

for d in destinies:
  if dist[d] != INF:
    print(dist[d])
  else:
    print('NO PATH')