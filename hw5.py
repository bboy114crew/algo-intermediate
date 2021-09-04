# BFS not use Queue
def BFS (V,Adj,s):
  level = {s: 0}
  parent = {s : None}
  i = 1
  frontier = [s] # previous level, i 􀀀 1
  while frontier:
    next = [ ] # next level, i
    for u in frontier:
      for v in Adj [u]:
        if v not in level: # not yet seen
          level[v] = i # level[u] + 1
          parent[v] = u
          next.append(v)
    frontier = next
    i += 1

import queue

# # Breadth First Search: Shortest Reach
# q = int(input())

# def bfs_shortest_reach(q):
#   for i in range(q):
#     nm = list(map(int, input().split()))
#     n = nm[0]
#     m = nm[1]

#     visited = [False for index in range(n + 1)]
#     dist = [-1 for index in range(n + 1)]

#     adj_list = [[] for index in range(n + 1)]

#     for j in range(m):
#       e1, e2 = map(int, input().split())
#       adj_list[e1].append(e2)
#       adj_list[e2].append(e1)

#     q = queue.Queue()
#     start = int(input())
#     visited[start] = True
#     q.put(start)
#     dist[start] = 0
#     while not q.empty():
#       u = q.get()
#       for v in adj_list[u]:
#         if (not visited[v]):
#           visited[v] = True
#           q.put(v)
#           dist[v] = dist[u] + 6

#     result = ''
#     for j in range(1, len(dist)):
#       if (j != start):
#         result = result + str(dist[j]) + " "
#     print(result)

# bfs_shortest_reach(q)

# Breadth First Search: Shortest Reach
# q = int(input())

# def bfs_shortest_reach(q):
#   for i in range(q):
#     nm = list(map(int, input().split()))
#     n = nm[0]
#     m = nm[1]

#     visited = [False for index in range(n + 1)]
#     dist = [-1 for index in range(n + 1)]

#     adj_list = [[] for index in range(n + 1)]

#     for j in range(m):
#       e1, e2 = map(int, input().split())
#       adj_list[e1].append(e2)
#       adj_list[e2].append(e1)

#     q = queue.Queue()
#     start = int(input())
#     visited[start] = True
#     q.put(start)
#     dist[start] = 0
#     while not q.empty():
#       u = q.get()
#       for v in adj_list[u]:
#         if (not visited[v]):
#           visited[v] = True
#           q.put(v)
#           dist[v] = dist[u] + 6

#     result = ''
#     for j in range(1, len(dist)):
#       if (j != start):
#         result = result + str(dist[j]) + " "
#     print(result)

# bfs_shortest_reach(q)

# # Validate The Maze
# def validate_the_maze(m, n, case, matrix):
#   len_case = len(case)

#   sx, sy = 0, 0  # first maze gate
#   ex, ey = 0, 0  # second maze gate

#   max_openings = 0 # it must equal 2

#   # get two gate
#   for i in range(len_case):
#     p1, p2 = case[i]
#     if (p1 == 0 or p2 == 0 or p1 == m - 1 or p2 == n - 1):
#       max_openings += 1
#       if (max_openings > 2):
#         print("invalid")
#         return
#       else:
#         if (sx == 0 and sy == 0):
#           sx = p1
#           sy = p2
#         else:
#           ex = p1
#           ey = p2

#   if (max_openings < 2):
#     print("invalid")
#     return

#   # # visited point
#   vis = [[False for j in range(n)] for i in range(m)]
#   vis[sx][sy] = True

#   # queue for store current point
#   q = queue.Queue()
#   q.put((sx, sy))

#   while not q.empty():
#     x, y = q.get()

#     # points right arround current point
#     arrounds = []
#     arrounds.append((x + 1, y))
#     arrounds.append((x, y + 1))
#     arrounds.append((x - 1, y))
#     arrounds.append((x, y - 1))

#     for arround in arrounds:
#       a_x, a_y = arround
#       # check if point inside matrix
#       if (a_x >= 0 and a_y >= 0 and a_x < m and a_y < n):
#         # check if point not visited and is posible move
#         if ((not vis[a_x][a_y]) and matrix[a_x][a_y] == '.'):
#           vis[a_x][a_y] = True
#           q.put(arround)

#   if (vis[ex][ey]):
#     print('valid')
#   else:
#     print('invalid')

# # Input
# t = int(input())

# cases = []
# matrixs = []
# for i in range(t):
#   mn = list(map(int, input().split()))
#   m = mn[0]
#   n = mn[1]
#   case = []
#   matrix = [[] for index in range(m)]
#   for j in range(m):
#     row = input()
#     row = [x for x in row]
#     matrix[j] = row
#     for k in range(len(row)):
#       if (row[k] == '.'):
#         case.append((j, k))
#   cases.append(case)
#   matrixs.append(matrix)

#   # Run and output
#   validate_the_maze(m, n, cases[i], matrixs[i])

# # Dhoom 4
# def dhoom_4(s_key, b_secret_key, num_b_keys, b_keys):
#   MAX = 100000 + 1
#   dist = [-1] * MAX

#   q = queue.Queue()

#   q.put(s_key)
#   dist[s_key] = 0

#   while not q.empty():
#     u = q.get()
#     for key in b_keys:
#       new_key = (u * key) % 100000
#       if dist[new_key] == -1:
#         dist[new_key] = dist[u] + 1
#         q.put(new_key)

#         if (new_key == b_secret_key):
#           print(dist[b_secret_key])
#           return

#   print(dist[b_secret_key])

# # Input
# ab = list(map(int, input().split()))
# s_key = ab[0]
# b_secret_key = ab[1]

# num_b_keys = int(input())

# b_keys = list(map(int, input().split()))

# # Run and output
# dhoom_4(s_key, b_secret_key, num_b_keys, b_keys)

# # Guilty Prince
# def guilty_prince(m, n, start, matrixs, index):
#   # m is number of row
#   # n is number of column
#   sx, sy = start  # first maze gate

#   # # visited point
#   vis = [[False for j in range(n)] for i in range(m)]
#   vis[sx][sy] = True

#   # queue for store current point
#   q = queue.Queue()
#   q.put((sx, sy))
#   result = 1
#   while not q.empty():
#     x, y = q.get()

#     # points right arround current point
#     arrounds = []
#     arrounds.append((x + 1, y))
#     arrounds.append((x, y + 1))
#     arrounds.append((x - 1, y))
#     arrounds.append((x, y - 1))

#     for arround in arrounds:
#       a_x, a_y = arround
#       # check if point inside matrix
#       if (a_x >= 0 and a_y >= 0 and a_x < m and a_y < n):
#         # check if point not visited and is posible move
#         if ((not vis[a_x][a_y]) and matrix[a_x][a_y] == '.'):
#           vis[a_x][a_y] = True
#           result += 1
#           q.put(arround)
#   result = 'Case ' + str(index) + ': ' + str(result)
#   print(result)

# # Input
# t = int(input())

# matrixs = []
# starts = []

# for i in range(t):
#   mn = list(map(int, input().split()))
#   m = mn[1]
#   n = mn[0]
#   matrix = [[] for index in range(m)]
#   for j in range(m):
#     row = input()
#     row = [x for x in row]
#     matrix[j] = row
#     for k in range(len(row)):
#       if (row[k] == '@'):
#         starts.append((j, k))
#         break
#   matrixs.append(matrix)

#   # Run and output
#   guilty_prince(m, n, starts[i], matrixs[i], i + 1)

# # Kefa and Park
# def kefa_and_park(n, m, a, edges):
#   MAX = 100000 + 5
#   cat = [0] * MAX
#   visited = [False] * MAX
#   graph = [[] for _ in range(MAX)]

#   for edge in edges:
#     u, v = edge
#     graph[u - 1].append(v - 1)
#     graph[v - 1].append(u - 1)

#   restaurants = 0
#   q = queue.Queue()
#   visited[0] = True
#   q.put(0)

#   cat[0] = (1 if a[0] == 1 else 0)

#   while not q.empty():
#     u = q.get()
#     for v in graph[u]:
#       if not visited[v]:
#         visited[v] = True
#         if a[v] == 1:
#           cat[v] = cat[u] + 1
#         # Number of cat <= max
#         if cat[v] <= m:
#           # Check if v is a leaf aka vertex has no children
#           if len(graph[v]) == 1:
#             restaurants += 1
#           # Go down to the leaf of v
#           else:
#             q.put(v)
#   print(restaurants)

# # Input
# nm = list(map(int, input().split()))
# n = nm[0] # the number of vertices of the tree
# m = nm[1] # the maximum number of consecutive vertices with cats that is still ok for Kefa.

# a = list(map(int, input().split()))
# edges = []

# for i in range(n - 1):
#   edge = list(map(int, input().split()))
#   edge = (edge[0], edge[1])
#   edges.append(edge)
# # Run and output
# kefa_and_park(n, m, a, edges)

# Slick
def is_valid_point (ax, ay, n, m):
  return ax >= 0 and ay >= 0 and ax < n and ay < m

def slick(n, m, i, j, matrix, result):
  q = queue.Queue()
  q.put((i, j))

  spilled_oil = 0
  if matrix[i][j] == 1:
    spilled_oil += 1
    matrix[i][j] = 0

  while not q.empty():
    x, y = q.get()

    arrounds = []
    arrounds.append((x + 1, y))
    arrounds.append((x, y + 1))
    arrounds.append((x - 1, y))
    arrounds.append((x, y - 1))
    for arround in arrounds:
      ax, ay = arround
      if (not is_valid_point(ax, ay, n, m)):
        continue
      if matrix[ax][ay] == 1:
        q.put((ax, ay))
        spilled_oil += 1
        matrix[ax][ay] = 0

  if spilled_oil != 0:
    if spilled_oil in results:
      results[spilled_oil] += 1
    else:
      results[spilled_oil] = 1


# Input
while True:
  n, m = map(int, input().split())

  if (n == 0 and m == 0):
    break

  results = {}

  matrix = [[] for index in range(n)]

  for i in range(n):
    row = list(map(int, input().split()))
    matrix[i] = row

  for i in range(n):
    for j in range(m):
      if (matrix[i][j] != 0):
        slick(n, m, i, j, matrix, results)

  # Output
  number_of_slicks = 0
  values = results.values()
  number_of_slicks = sum(values)
  print(number_of_slicks)

  if number_of_slicks > 0:
    results = {size:num for size, num in sorted(results.items())}
    for size, num in results.items():
      print(size, num)

# # Ice Cave
# def is_valid_point (ax, ay, n, m):
#   return ax >= 0 and ay >= 0 and ax < n and ay < m

# def ice_cave(n, m, s, e, matrix):
#   q = queue.Queue()
#   q.put(s)
#   sx, sy = s
#   ex, ey = e
#   matrix[sx][sy] = 'X'

#   while not q.empty():
#     x, y = q.get()

#     # points right arround current point
#     arrounds = []
#     arrounds.append((x + 1, y))
#     arrounds.append((x, y + 1))
#     arrounds.append((x - 1, y))
#     arrounds.append((x, y - 1))

#     for arround in arrounds:
#       ax, ay = arround
#       if (ax == ex and ay == ey and matrix[ax][ay] == 'X'):
#         print('YES')
#         return
#       if (is_valid_point(ax, ay, n, m) and matrix[ax][ay] == '.'):
#         matrix[ax][ay] = 'X'
#         q.put(arround)
#   print('NO')

# # Input
# matrixs = []

# nm = list(map(int, input().split()))
# n = nm[0] # row
# m = nm[1] # column
# matrix = [[] for index in range(n)]
# for j in range(n):
#   row = input()
#   row = [x for x in row]
#   matrix[j] = row

# s_input = list(map(int, input().split()))
# s = (s_input[0] - 1, s_input[1] - 1)
# e_input = list(map(int, input().split()))
# e = (e_input[0] - 1, e_input[1] - 1)

# # Run and output
# ice_cave(n, m, s, e, matrix)

# Sheep
def is_valid_point (ax, ay, n, m):
  return ax >= 0 and ay >= 0 and ax < n and ay < m

def sheep(n, m, sx, sy, matrix):
  global survived_sheep, survived_wolf

  q = queue.Queue()
  q.put((sx, sy))

  current_sheep = (1 if matrix[sx][sy] == 'k' else 0)
  current_wolf = (1 if matrix[sx][sy] == 'v' else 0)

  connected_outside = False
  matrix[sx][sy] = '#'

  while not q.empty():
    x, y = q.get()

    if (x == 0 or x == n - 1 or y == 0 or y == m - 1):
      connected_outside = True

    # points right arround current point
    arrounds = []
    arrounds.append((x + 1, y))
    arrounds.append((x, y + 1))
    arrounds.append((x - 1, y))
    arrounds.append((x, y - 1))

    for arround in arrounds:
      ax, ay = arround
      if not is_valid_point(ax, ay, n, m):
        connected_outside = True
        continue
      if (matrix[ax][ay] != '#'):
        current_sheep += (1 if matrix[ax][ay] == 'k' else 0)
        current_wolf += (1 if matrix[ax][ay] == 'v' else 0)
        matrix[ax][ay] = '#'
        q.put(arround)

  if connected_outside:
    survived_sheep += current_sheep
    survived_wolf += current_wolf
  else:
    if current_sheep > current_wolf:
      survived_sheep += current_sheep
    else:
      survived_wolf += current_wolf

# Input
nm = list(map(int, input().split()))
n = nm[0] # row
m = nm[1] # column

matrix = [[] for index in range(n)]

for j in range(n):
  row = input()
  row = [x for x in row]
  matrix[j] = row

survived_sheep = 0
survived_wolf = 0

for i in range(n):
  for j in range(m):
    if (matrix[i][j] != '#'):
      sheep(n, m, i, j, matrix)

# Run and output
print(survived_sheep, survived_wolf)