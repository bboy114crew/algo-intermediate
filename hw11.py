# # Possible Friends
# INF = int(1e9)

# def floyd(dist, m):
#   for k in range(m):
#     for i in range(m):
#       if dist[i][k] == INF:
#         continue
#       for j in range(m):
#         if dist[k][j] != INF and dist[i][j] > dist[i][k] + dist[k][j]:
#           dist[i][j] = dist[i][k] + dist[k][j]

# t = int(input())

# for _ in range(t):
#   graph = []
#   line = input()
#   m = len(line)
#   graph.append(line)
#   dist = [[INF for i in range(m)] for i in range(m)]
#   for i in range(1, m):
#     row = input()
#     graph.append(row)

#   for i in range(m):
#     for j in range(m):
#       if i == j:
#         dist[i][j] = 0
#       else:
#         if graph[i][j] == 'Y':
#           dist[i][j] = 1
#   floyd(dist, m)
#   id = 0
#   max_posible_friends = 0
#   for i in range(m):
#     count = 0
#     for j in range(m):
#       if i == j:
#         continue
#       if dist[i][j] == 2:
#         count += 1
#     if count > max_posible_friends:
#       max_posible_friends = count
#       id = i
#   print(id, max_posible_friends)

# # Meeting Prof. Miguel ...
# INF = int(1e9)
# MAX = 26

# def add_edge(direction, X, Y, cost, array):
#   i = ord(X) - ord('A')
#   j = ord(Y) - ord('A')
#   array[i][j] = min(cost, array[i][j])
#   if (direction == 'B'):
#     array[j][i] = min(cost, array[j][i])

# def floyd(dist, m):
#   for k in range(m):
#     for i in range(m):
#       if dist[i][k] == INF:
#         continue
#       for j in range(m):
#         if dist[k][j] != INF and dist[i][j] > dist[i][k] + dist[k][j]:
#           dist[i][j] = dist[i][k] + dist[k][j]

# while True:
#   e = int(input())
#   if e == 0:
#     break

#   young_cost = [[INF for i in range(MAX)] for i in range(MAX)]
#   old_cost = [[INF for i in range(MAX)] for i in range(MAX)]

#   for i in range(MAX):
#     for j in range(MAX):
#       young_cost[i][i] = 0
#       old_cost[i][i] = 0

#   for _ in range(e):
#     age, direction, X, Y, cost = list(input().split())
#     if age == 'Y':
#       add_edge(direction, X, Y, int(cost), young_cost)
#     else:
#       add_edge(direction, X, Y, int(cost), old_cost)

#   floyd(young_cost, MAX)
#   floyd(old_cost, MAX)

#   cost = INF - 1
#   results = []

#   young_s, old_s = list(input().split())

#   for meet in range(MAX):
#     i = ord(young_s) - ord('A')
#     j = ord(old_s) - ord('A')
#     current_cost = young_cost[i][meet] + old_cost[j][meet]

#     if current_cost < cost:
#       results = []
#       results.append(chr(meet + ord('A')))
#       cost = current_cost
#     elif current_cost == cost:
#       results.append(chr(meet + ord('A')))

#   results.sort()
#   if len(results) > 0:
#     print(cost, *results)
#   else:
#     print('You will never meet.')

# # Arbitrage

# # Key point [i][k] + [k][i] vs [i][i]

# def floyd(dist, m):
#   for k in range(m):
#     for i in range(m):
#       for j in range(m):
#         dist[i][j] = max(dist[i][j] , dist[i][k] * dist[k][j])

# case = 0

# while True:
#   n = int(input())

#   if n == 0:
#     break

#   case += 1
#   currencies = []

#   for _ in range(n):
#     currency = str(input())
#     currencies.append(currency)

#   dist = [[1 if i == j else 0 for j in range(n)] for i in range(n)]

#   m = int(input())

#   for _ in range(m):
#     cx, r, cy = list(input().split())
#     u, v = map(lambda x: currencies.index(x), (cx, cy))
#     dist[u][v] = float(r)
#   input()
#   floyd(dist, n)

#   arbitrage = False

#   for i in range(n):
#     if dist[i][i] > 1:
#       arbitrage = True
#       break

#   if arbitrage:
#     print('Case {}: Yes'.format(case))
#   else:
#     print('Case {}: No'.format(case))

# # Risk
# INF = int(1e9)
# n = 20

# def floyd(dist, m):
#   for k in range(m):
#     for i in range(m):
#       if dist[i][k] == INF:
#         continue
#       for j in range(m):
#         if dist[k][j] != INF and dist[i][j] > dist[i][k] + dist[k][j]:
#           dist[i][j] = dist[i][k] + dist[k][j]
# case = 0
# while True:
#   dist = [[INF for i in range(n + 1)] for _ in range(n + 1)]
#   try:
#     for i in range(1, n):
#       for j in list(map(int, input().split()))[1:]:
#         dist[i][j] = dist[j][i] = 1
#     floyd(dist, n +  1)
#     case += 1
#     print('Test Set #{}'.format(case))

#     m = int(input())
#     for _ in range(m):
#       s, e = list(map(int, input().split()))
#       print('{:2d} to {:2d}: {}'.format(s, e, dist[s][e]))
#     print()
#   except EOFError:
#     break

# # Asterix and Obelix
# INF = int(1e9)
# case = 0

# max_cost = [[None] * 85 for _ in range(85)]
# def floyd(dist, max_cost, C):
#   for _ in range(2):
#     for k in range(1, C + 1):
#       for i in range(1, C + 1):
#         for j in range(1, C + 1):
#           max_c = max(max_cost[i][k], max_cost[k][j])
#           if dist[i][j] + max_cost[i][j] > dist[i][k] + dist[k][j] + max_c:
#             dist[i][j] = dist[i][k] + dist[k][j]
#             max_cost[i][j] = max_c

# while True:
#   C, R, Q = map(int, input().split())

#   if C == 0:
#     break

#   case += 1

#   f = [0] + list(map(int, input().split()))

#   for i in range(1, C + 1):
#     for j in range(1, C + 1):
#       max_cost[i][j] = max(f[i], f[j])

#   dist = [[INF] * (C + 1) for _ in range(C + 1)]

#   for _ in range(R):
#     u, v, w = map(int, input().split())
#     dist[u][v] = dist[v][u] = w

#   floyd(dist, max_cost, C)

#   if case > 1:
#     print()

#   print('Case #{}'.format(case))

#   for _ in range(Q):
#     u, v = map(int, input().split())
#     print(-1 if dist[u][v] == INF else dist[u][v] + max_cost[u][v])

# # Thunder Mountain
# INF = int(1e9)

# def distance(a,b):
#   return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

# def floyd(dist, m):
#   for k in range(m):
#     for i in range(m):
#       for j in range(m):
#         dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

# N = int(input())

# for case in range(N):
#   n = int(input())
#   dist = [[0 if i == j else INF for j in range(n)] for i in range(n)]

#   x = [None for i in range(n)]
#   y = [None for i in range(n)]

#   for i in range(n):
#     point = list(map(int, input().split()))
#     x[i] = point[0]
#     y[i] = point[1]

#   for i in range(n):
#     for j in range(n):
#       dis = distance((x[i], y[i]), (x[j], y[j]))
#       if dis <= 10:
#         dist[i][j] = dis

#   floyd(dist, n)

#   print('Case #{}:'.format(case + 1))

#   res = 0
#   for i in range(n):
#     for j in range(n):
#       res = max(res, dist[i][j])
#   print("{:.4f}".format(res) if res != INF else 'Send Kurdy')
#   print()

# # Event Organizer
# INF = int(1e9)
# MAX = 49

# def floyd(dist, m):
#   for k in range(m):
#     for i in range(m):
#       for j in range(m):
#         if i <= k <= j:
#           dist[i][j] = max(dist[i][j], dist[i][k] + dist[k][j])

# T = int(input())

# for _ in range(T):
#   dist = [[0 for j in range(MAX)] for i in range(MAX)]
#   N = int(input())
#   for i in range(N):
#     S, E, C = list(map(int, input().split()))
#     dist[S][E] = max(dist[S][E], C)

#   floyd(dist, MAX)

#   print(dist[0][MAX - 1])

# Greg and Graph
n = int(input())
dist = [[0] * (n + 1)]

for i in range(1, n + 1):
  dist.append([0] + list(map(int, input().split())))

deleted_vertices = list(map(int, input().split()))
res = [0] * n

for index in range(n - 1, -1, -1):
  k = deleted_vertices[index]

  for i in range(1, n + 1):
    for j in range(1, n + 1):
      dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

  for u in deleted_vertices[index:]:
    for v in deleted_vertices[index:]:
      res[index] += dist[u][v]

print(*res)




