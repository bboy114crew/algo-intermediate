# Bishu and his Girlfriend

def bishu_and_his_girlfriend(s):
  global vistited, dist, graph

  vistited[s] = True
  for v in graph[s]:
    if not vistited[s]:
      dist[v] = dist[s] + 1
      bishu_and_his_girlfriend(v)




# Input
n = int(input())

dist = [-1 for index in range(n)]
dist[0] = 0

min_distance = n
min_id = n - 1

graph = [[] for index in range(n)]
for _ in range(n - 1):
  u, v = list(map(int, input().split()))
  graph[u - 1].append(v - 1)
  graph[v - 1].append(u - 1)

q = int(input())
vistited = [False for index in range(n)]
city_of_girl = []

for _ in range(q):
  city = int(input())
  city_of_girl.append(city - 1)

# Run and output
bishu_and_his_girlfriend(0)

min_distance = city_of_girl[0]
min_id = 0

print(dist)

for i in range(1, len(city_of_girl)):
  if (dist[city_of_girl[i]] < min_distance or ((dist[city_of_girl[i]] == min_distance) and (min_id > i))):
    min_distance = dist[city_of_girl[i]]
    min_id = i

print(min_id + 1)