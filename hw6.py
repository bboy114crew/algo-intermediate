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

# # Prayatna
# def prayatna(s, visited, dist, graph):
#   global result
#   visited[s] = True
#   stack = []
#   stack.append(s)
#   if len(graph[s]) == 0:
#     result += 1
#     return
#   while (len(stack) != 0):
#     u = stack.pop()
#     for v in graph[u]:
#       if not visited[v]:
#         visited[v] = True
#         stack.append(v)
#   result += 1

# # Input
# t = int(input()) # number of test cases

# for _ in range(t):
#   n = int(input())
#   e = int(input())
#   dist = [-1 for index in range(n)]
#   if (e == 0):
#     print(n)
#     continue
#   # Make adjacency list
#   graph = [[] for index in range(n)]
#   for i in range(e):
#     u, v = list(map(int, input().split()))
#     graph[u].append(v)
#     graph[v].append(u)

#   visited = [False for index in range(n)]

#   # Run and output
#   result = 0
#   for i in range(n):
#     if not visited[i]:
#       prayatna(i, visited, dist, graph)
#   print(result)

# Lakes in Berland
def is_valid_point (ax, ay, n, m):
  return ax >= 0 and ay >= 0 and ax < n and ay < m

def lakes_in_berland(n, m, i, j, matrix, results, vis):
  vis[i][j] = True
  stack = []
  stack.append((i, j))
  connected_with_ocean = False
  # Check if cell connected with the ocean
  if (i == 0 or i == n - 1 or j == 0 or j == m - 1):
      connected_with_ocean = True
  lake = 0
  cells = []
  if (matrix[i][j] == '.'):
    lake = 1
    cells.append((i, j))
  else:
    return

  while (len(stack) != 0):
    x, y = stack.pop()

    arrounds = []
    arrounds.append((x + 1, y))
    arrounds.append((x, y + 1))
    arrounds.append((x - 1, y))
    arrounds.append((x, y - 1))

    for arround in arrounds:
      ax, ay = arround
      # Check if cell in map
      if (not is_valid_point(ax, ay, n, m)):
        continue
      if matrix[ax][ay] == '.':
         # Check if cell connected with the ocean
        if (ax == 0 or ax == n - 1 or ay == 0 or ay == m - 1):
          connected_with_ocean = True
        if not vis[ax][ay]:
          vis[ax][ay] = True
          stack.append((ax, ay))
          lake += 1
          cells.append((ax, ay))
  # Store list cells and total cell of current lake
  if (lake != 0 and (not connected_with_ocean)):
    current_lake_cell = {
      'lake': lake,
      'cells': cells
    }
    # Add current lake to list lake in map
    results.append(current_lake_cell)
# Input
n, m, k = map(int, input().split())

# Initial matrix
matrix = [[] for index in range(n)]
# Result matrix
matrix_final = [[] for index in range(n)]
# Input matrix
for i in range(n):
  row = input()
  matrix[i] = [char for char in row]
  matrix_final[i] = [char for char in row]

# List of lake
results = []

vis = [[False for j in range(m)] for i in range(n)]

# Check if cell is water cell
for i in range(n):
  for j in range(m):
    if not vis[i][j]:
      lakes_in_berland(n, m, i, j, matrix, results, vis)

# Sort lake by number of cells in lake
results =  sorted(results, key=lambda k: k['lake'])

total_lake = len(results)
minimum_num_cells = 0
# Find minimum number of water cells
for result in results:
  if (total_lake > k):
    total_lake -= 1
    minimum_num_cells += result['lake']
    # Fill up water cell
    for cell in result['cells']:
      x, y = cell
      matrix_final[x][y] = '*'
  else:
    break

# Output
if k == len(results):
  print(0)
  for i in range(n):
    print("".join(str(x) for x in matrix_final[i]))
else:
  print(minimum_num_cells)
  for i in range(n):
    print("".join(str(x) for x in matrix_final[i]))

# Dudu Service Maker
