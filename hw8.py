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

# The Shortest Path
from heapq import heappush, heappop

def the_shortest_path(source, destination):
  global graph
  INF = int(1e9)  
  dist = [INF for index in range(10005)]
  dist[source] = 0

  h = []
  heappush(h, (0, source))

  while len(h):
    top = heappop(h)
    w, b = top

    if b == destination:
      break

    if dist[b] < w:
      continue

    for neighbor in graph[b]:
      w_n, b_n = neighbor
      if w_n + dist[b] < dist[b_n]:
        dist[b_n] = w_n + w
        heappush(h, (dist[b_n],  b_n))
  print(dist[destination])

s = int(input()) # the number of tests <= 10

for _ in range(s):
  n = int(input()) # the number of cities <= 10000
  cities = {}
  graph = [[] for index in range(10005)]
  for i in range(n):
    NAME = str(input()) # city name
    cities[NAME] = i + 1
    p = int(input()) # the number of neighbours of city NAME
    for j in range(p):
      # nr is index of a city connected to NAME (the index of the first city is 1)]
      # cost is the transportation cost
      nr, cost = list(map(int, input().split()))
      graph[i + 1].append((cost, nr))
  r = int(input()) # the number of paths to find <= 100
  for i in range(r):
    # NAME1 is source
    # NAME2 is destination
    NAME_1, NAME_2 = list(map(str, input().split()))
    the_shortest_path(cities[NAME_1], cities[NAME_2])
  input()