# # Travelling Cost
# from heapq import heappush, heappop
# def travelling_cost(s):
#   global graph, destinies, u, dist

#   h = []

#   heappush(h, (0, s))

#   dist[s] = 0

#   while len(h):
#     top = heappop(h)
#     w, b = top

#     if dist[b] < w:
#       continue

#     for neighbor in graph[b]:
#       w_n, b_n = neighbor
#       if w_n + dist[b] < dist[b_n]:
#         dist[b_n] = w_n + w
#         heappush(h, (dist[b_n],  b_n))

# n = int(input())
# INF = int(1e9)

# graph = [[] for index in range(505)]
# for _ in range(n):
#   a, b, w = list(map(int, input().split()))
#   graph[a].append((w, b))
#   graph[b].append((w, a))

# u = int(input())
# q = int(input())

# destinies = []
# dist = [INF for index in range(505)]
# for _ in range(q):
#   d = int(input())
#   destinies.append(d)

# travelling_cost(u)

# for d in destinies:
#   if dist[d] != INF:
#     print(dist[d])
#   else:
#     print('NO PATH')

# # Mice and Maze
# from heapq import heappush, heappop
# def mice_and_maze(source):
#   global e, t_max, number_of_mice_exited, graph

#   INF = int(1e9)
#   dist = [INF for index in range(10005)]
#   dist[source] = 0

#   h = []
#   heappush(h, (0, source))

#   while len(h):
#     top = heappop(h)
#     w, b = top

#     if b == e:
#       break

#     if dist[b] < w:
#       continue

#     for neighbor in graph[b]:
#       w_n, b_n = neighbor
#       if w_n + dist[b] < dist[b_n]:
#         dist[b_n] = w_n + w
#         heappush(h, (dist[b_n],  b_n))

#   if dist[e] <= t_max:
#     number_of_mice_exited += 1

# graph = [[] for index in range(10005)]

# n = int(input())
# e = int(input())
# t_max = int(input())
# m = int(input())

# for i in range(m):
#   a, b, t = list(map(int, input().split()))
#   graph[a].append((t, b))

# number_of_mice_exited = 0

# for i in range(1, n + 1):
#   mice_and_maze(i)

# print(number_of_mice_exited)

# # The Shortest Path
# from heapq import heappush, heappop

# def the_shortest_path(source, destination):
#   global graph
#   INF = int(1e9)
#   dist = [INF for index in range(10005)]
#   dist[source] = 0

#   h = []
#   heappush(h, (0, source))

#   while len(h):
#     top = heappop(h)
#     w, b = top

#     if b == destination:
#       break

#     if dist[b] < w:
#       continue

#     for neighbor in graph[b]:
#       w_n, b_n = neighbor
#       if w_n + dist[b] < dist[b_n]:
#         dist[b_n] = w_n + w
#         heappush(h, (dist[b_n],  b_n))
#   print(dist[destination])

# s = int(input()) # the number of tests <= 10

# for _ in range(s):
#   n = int(input()) # the number of cities <= 10000
#   cities = {}
#   graph = [[] for index in range(10005)]
#   for i in range(n):
#     NAME = str(input()) # city name
#     cities[NAME] = i + 1
#     p = int(input()) # the number of neighbours of city NAME
#     for j in range(p):
#       # nr is index of a city connected to NAME (the index of the first city is 1)]
#       # cost is the transportation cost
#       nr, cost = list(map(int, input().split()))
#       graph[i + 1].append((cost, nr))
#   r = int(input()) # the number of paths to find <= 100
#   for i in range(r):
#     # NAME1 is source
#     # NAME2 is destination
#     NAME_1, NAME_2 = list(map(str, input().split()))
#     the_shortest_path(cities[NAME_1], cities[NAME_2])
#   input()

# # Traffic Network
# from heapq import heappush, heappop
# INF = int(1e9)
# MAX = 10005

# def traffic_network(s, dist, graph):
#   h = [(0, s)]
#   dist[s] = 0

#   while len(h):
#     w, u = heappop(h)

#     if w > dist[u]:
#       continue

#     for weight, v in graph[u]:
#       if w + weight < dist[v]:
#         dist[v] = w + weight
#         heappush(h, (dist[v], v))

# t = int(input()) # the number of tests <= 20

# for _ in range(t):
#   n, m, k, s, t = list(map(int, input().split()))
#   graph_s = [[] for _ in range(MAX)]
#   graph_t = [[] for _ in range(MAX)]
#   dist_t = [INF for index in range(MAX)]
#   dist_s = [INF for index in range(MAX)]

#   # m is number of one-way roads
#   for i in range(m):
#     u, v, d = map(int, input().split())
#     graph_s[u].append((d, v))
#     graph_t[v].append((d, u))

#   traffic_network(s, dist_s, graph_s)
#   traffic_network(t, dist_t, graph_t)
#   res = dist_s[t]
#   # k is number of two-way roads
#   for i in range(k):
#     u, v, d = map(int, input().split())
#     res = min(res, dist_s[u] + d + dist_t[v], dist_s[v] + d + dist_t[u])

#   print(res if res != INF else -1)

# # Sending Email
# from heapq import heappush, heappop
# INF = int(1e9)
# MAX = 10005

# def sending_email(graph, source, destination, case):
#   dist = [INF for index in range(MAX)]
#   dist[source] = 0

#   h = []
#   heappush(h, (0, source))

#   while len(h):
#     top = heappop(h)
#     w, b = top

#     if b == destination:
#       break

#     if dist[b] < w:
#       continue

#     for neighbor in graph[b]:
#       w_n, b_n = neighbor
#       if w_n + dist[b] < dist[b_n]:
#         dist[b_n] = w_n + w
#         heappush(h, (dist[b_n],  b_n))

#   res = dist[destination]
#   if res != INF:
#     print('Case #{}: {}'.format(case, res))
#   else:
#     print('Case #{}: unreachable'.format(case))

# q = int(input())

# for i in range(q):
#   n, m, s, t = list(map(int, input().split()))
#   graph = [[] for _ in range(MAX)]
#   for _ in range(m):
#     u, v, d = map(int, input().split())
#     graph[u].append((d, v))
#     graph[v].append((d, u))
#   sending_email(graph, s, t, i + 1)

# # Commandos - Source: LightOJ
# from heapq import heappush, heappop
# INF = int(1e9)
# MAX = 10005

# def commandos(graph, source):
#   dist = [INF for index in range(MAX)]
#   dist[source] = 0

#   h = []
#   heappush(h, (0, source))

#   while len(h):
#     top = heappop(h)
#     w, b = top

#     if dist[b] < w:
#       continue

#     for neighbor in graph[b]:
#       w_n, b_n = neighbor
#       if w_n + dist[b] < dist[b_n]:
#         dist[b_n] = w_n + w
#         heappush(h, (dist[b_n],  b_n))
#   return dist

# t = int(input())
# for i in range(t):
#   n = int(input())
#   r = int(input())
#   graph = [[] for _ in range(MAX)]
#   for j in range(r):
#     u, v = list(map(int, input().split()))
#     graph[u].append((1, v))
#     graph[v].append((1, u))
#   s, d = list(map(int, input().split()))
#   dist_s = commandos(graph, s)
#   dist_d = commandos(graph, d)

#   res = 0

#   for j in range(n):
#     res = max(res, dist_s[j] + dist_d[j])

#   print('Case {}: {}'.format(i + 1, res))

# # Chocolate Journey
# from heapq import heappush, heappop
# INF = int(1e9)

# def chocolate_journey(graph, source, n):
#   dist = [INF for index in range(n + 1)]
#   dist[source] = 0

#   h = []
#   heappush(h, (0, source))

#   while len(h):
#     top = heappop(h)
#     w, b = top

#     if dist[b] < w:
#       continue

#     for neighbor in graph[b]:
#       w_n, b_n = neighbor
#       if w_n + dist[b] < dist[b_n]:
#         dist[b_n] = w_n + w
#         heappush(h, (dist[b_n],  b_n))
#   return dist

# n, m, k, x = list(map(int, input().split()))
# cities_have_socola = list(map(int, input().split()))

# graph = [[] for _ in range(n + 1)]
# for _ in range(m):
#   u, v, d = list(map(int, input().split()))
#   graph[u].append((d, v))
#   graph[v].append((d, u))
# a, b = list(map(int, input().split()))

# dist_a = chocolate_journey(graph, a, n)
# dist_b = chocolate_journey(graph, b, n)

# res = INF
# for city in cities_have_socola:
#   if dist_b[city] <= x:
#     res = min(res, dist_a[city] + dist_b[city])

# print(res if res != INF else -1)

# Almost Shortest Path
from heapq import heappush, heappop
INF = int(1e9)

def chocolate_journey(graph, source, dist):
  dist[source] = 0

  h = []
  heappush(h, (0, source))

  while len(h):
    top = heappop(h)
    w, b = top

    if dist[b] < w:
      continue

    for neighbor in graph[b]:
      w_n, b_n = neighbor
      if w_n + dist[b] < dist[b_n]:
        dist[b_n] = w_n + w
        heappush(h, (dist[b_n],  b_n))

while True:
  n, m = list(map(int, input().split()))

  if n == 0 and m == 0:
    break

  graph = [[] for _ in range(n)]
  graph_s = [[] for _ in range(n)]
  graph_d = [[] for _ in range(n)]

  dist = [INF] * n
  dist_s = [INF] * n
  dist_d = [INF] * n

  s, d = list(map(int, input().split()))

  for _ in range(m):
    u, v, p = list(map(int, input().split()))
    graph_s[u].append((p, v))
    graph_d[v].append((p, u))

  chocolate_journey(graph_s, s, dist_s)
  chocolate_journey(graph_d, d, dist_d)
  shortest = dist_s[d]
  for i in range(n):
    for w, v in graph_s[i]:
      # check s -> i + i -> v + v -> d is euqal shortest mean i -> v belong to shortest path
      if (dist_s[i] + w + dist_d[v] != shortest):
        graph[i].append((w, v))

  chocolate_journey(graph, s, dist)

  print(dist[d] if dist[d] != INF else -1)
