# # Bishu and his Girlfriend
# def bishu_and_his_girlfriend(s, visited, dist, graph):
#   visited[s] = True
#   stack = []
#   stack.append(s)
#   while (len(stack) != 0):
#     u = stack.pop()
#     for v in graph[u]:
#       if not visited[v]:
#         visited[v] = True
#         dist[v] = dist[u] + 1
#         stack.append(v)

# # Input
# n = int(input())

# dist = [-1 for index in range(n + 1)]
# dist[1] = 0

# # Make adjacency list
# graph = [[] for index in range(n + 1)]
# for _ in range(n - 1):
#   u, v = list(map(int, input().split()))
#   graph[u].append(v)
#   graph[v].append(u)

# q = int(input())
# visited = [False for index in range(n + 1)]

# # Make list location where the girls live
# city_of_girl = []
# for _ in range(q):
#   city = int(input())
#   city_of_girl.append(city)

# # Run and output
# bishu_and_his_girlfriend(1, visited, dist, graph)

# min_distance = n + 1
# min_id = n
# for i in range(len(city_of_girl)):
#   if (
#     dist[city_of_girl[i]] < min_distance or
#     ((dist[city_of_girl[i]] == min_distance) and (min_id > city_of_girl[i]))):
#     min_distance = dist[city_of_girl[i]]
#     min_id = city_of_girl[i]

# print(min_id)

# Prayatna
def prayatna(s, visited, dist, graph):
  global result
  visited[s] = True
  stack = []
  stack.append(s)
  if len(graph[s]) == 0:
    result += 1
    return
  while (len(stack) != 0):
    u = stack.pop()
    for v in graph[u]:
      if not visited[v]:
        visited[v] = True
        stack.append(v)
  result += 1

# Input
t = int(input()) # number of test cases

for _ in range(t):
  n = int(input())
  e = int(input())
  dist = [-1 for index in range(n)]
  if (e == 0):
    print(n)
    continue
  # Make adjacency list
  graph = [[] for index in range(n)]
  for i in range(e):
    u, v = list(map(int, input().split()))
    graph[u].append(v)
    graph[v].append(u)

  visited = [False for index in range(n)]

  # Run and output
  result = 0
  for i in range(n):
    if not visited[i]:
      prayatna(i, visited, dist, graph)
  print(result)