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

# Dhoom 4

def dhoom_4(s_key, b_secret_key, num_b_keys, b_keys):
  MAX = 100000 + 1
  dist = [-1] * MAX

  q = queue.Queue()

  q.put(s_key)
  dist[s_key] = 0

  while not q.empty():
    for key in b_keys:
      new_key = (u * key) % 100000
      if dist[new_key] == -1:
        dist[new_key] = dist[u] + 1
        q.put(new_key)

        if (new_key == b_secret_key):
          print(dist[b_secret_key])
          return

  print(dist[b_secret_key])

# Input
ab = list(map(int, input().split()))
s_key = ab[0]
b_secret_key = ab[1]

num_b_keys = int(input())

b_keys = list(map(int, input().split()))

# Run and output
dhoom_4(s_key, b_secret_key, num_b_keys, b_keys)


