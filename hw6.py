# Bishu and his Girlfriend
def bishu_and_his_girlfriend(s, visited, dist, graph):
  visited[s] = True
  stack = []
  stack.append(s)
  while (len(stack) != 0):
    u = stack.pop()
    for v in graph[u]:
      if not visited[v]:
        visited[v] = True
        dist[v] = dist[u] + 1
        stack.append(v)

# Input
n = int(input())

dist = [-1 for index in range(n + 1)]
dist[1] = 0

min_distance = n + 1
min_id = n

graph = [[] for index in range(n + 1)]
for _ in range(n - 1):
  u, v = list(map(int, input().split()))
  graph[u].append(v)
  graph[v].append(u)

q = int(input())
visited = [False for index in range(n + 1)]
city_of_girl = []

for _ in range(q):
  city = int(input())
  city_of_girl.append(city)

# Run and output
bishu_and_his_girlfriend(1, visited, dist, graph)

for i in range(len(city_of_girl)):
  if (
    dist[city_of_girl[i]] < min_distance or 
    ((dist[city_of_girl[i]] == min_distance) and (min_id > city_of_girl[i]))):
    min_distance = dist[city_of_girl[i]]
    min_id = city_of_girl[i]

print(min_id)