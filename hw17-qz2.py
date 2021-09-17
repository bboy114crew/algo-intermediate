# MUH and Important Things

# N = int(input())
# h = list(map(int, input().split()))

# h_dict = dict()

# h_count = dict()

# for i in range(N):
#   h_dict[i + 1] = h[i]
# h_dict_sorted = sorted(h_dict.items(), key=lambda kv: kv[1])

# for i in range(N):
#   if h[i] not in h_count:
#     h_count[h[i]] = 1
#   else:
#     h_count[h[i]] += 1

# h_count_sorted = sorted(h_count.items(), key=lambda kv: kv[1])

# total = 0

# can_swap = []

# for (key, value) in h_count_sorted:
#   if total >= 4:
#     break
#   if value >= 2:
#     can_swap.append((key, value))
#     total += value

# def print_result_list(current_l, c_swap):
#   global max_print
#   new_list = current_l
#   c_key, c_value = c_swap
#   count_swap = 0
#   for i in range(len(current_l)):
#     current_l_key, current_l_value = current_l[i]
#     if max_print == 3:
#       break
#     if count_swap < c_value - 1 and c_key == current_l_value:
#       new_list[i], new_list[i + 1] = new_list[i + 1], new_list[i]
#       count_swap += 1
#       max_print += 1
#       print(' '.join([str(key) for (key, value) in new_list]))

# max_print = 1 

# if total < 3 or len(h_count) < 2:
#   print('NO')
# else:
#   print('YES')
#   print(' '.join([str(key) for (key, value) in h_dict_sorted]))

#   print_result_list(h_dict_sorted, can_swap[0])
#   print_result_list(h_dict_sorted, can_swap[1])

# # Fibsieve Fantabulous
# T = int(input())
# for case in range(T):
#   S = int(input())

#   i = 0

#   total = 0

#   N = 1

#   x = 0
#   y = 0

#   while True:
#     i = i + 1
#     total = total + (i + i - 1)

#     if total < S:
#       continue
#     else:
#       N = i
#       number_of_move = S - (total - (i + i - 1))
#       count = 0
#       if N % 2 == 1:
#         if number_of_move < N:
#           x = N
#           y = number_of_move
#         else:
#           y = N
#           x = N - (number_of_move - N)
#       else:
#         if number_of_move < N:
#           y = N
#           x = number_of_move
#         else:
#           x = N
#           y = N - (number_of_move - N)
#     break

#   print('Case {}: {} {}'.format(case + 1, x, y))

# Ubiquitous Religions
# parent = []
# ranks = []

# def make_set(n):
#   global parent, ranks
#   parent = [i for i in range(n + 1)]
#   ranks = [i for i in range(n + 1)]

# def find_set(u):
#   global parent
#   if parent[u] != u:
#     parent[u] = find_set(parent[u])
#   return parent[u]

# def union_set(u, v):
#   global parent, ranks
#   up = find_set(u)
#   vp = find_set(v)

#   if up == vp:
#     return

#   if ranks[up] > ranks[vp]:
#     parent[vp] = up
#   elif ranks[up] < ranks[vp]:
#     parent[up] = vp
#   else:
#     parent[up] = vp
#     ranks[vp] += 1

# case = 0

# while True:
#   N, M = list(map(int, input().split()))

#   if N == 0 and M == 0:
#     break
  
#   case += 1
#   result = N

#   make_set(N)
#   for _ in range(M):
#     i, j = list(map(int, input().split()))
#     u = find_set(i)
#     v = find_set(j)
#     if u != v:
#       result -= 1
#       union_set(i, j)

#   print('Case {}: {}'.format(case, result))

# Phone List
# class Node:
#   def __init__(self):
#     self.count_word = 0
#     self.child = dict()

# def add_word(root, s):
#   tmp = root
#   for i in range(len(s)):
#     ch = s[i]
#     if ch not in tmp.child:
#       tmp.child[ch] = Node()
#     else:
#       if tmp.child[ch].count_word >= 1 and i <= len(s) - 1:
#         return False
#     tmp = tmp.child[ch]
#   tmp.count_word += 1
#   if len(tmp.child) > 0:
#     return False
#   return True

# T = int(input())

# for case in range(T):
#   N = int(input())
#   root = Node()
#   result = True

#   phone_numbers = []
  
#   for i in range(N):
#     number = input()
#     phone_numbers.append(number)

#   for number in phone_numbers:
#     result = add_word(root, number)
#     if result == False:
#       break
  
#   final_res = 'YES' if result == True else 'NO'
#   print(final_res)

# Freckles
from heapq import heappush, heappop
INF = 1e9

def distance(A, B):
  x, y = A
  z, t = B
  return ((x - z) ** 2 + (y - t) ** 2) ** 0.5

def prim(src):
  global min_heap, graph, dist, path, visited
  dist[src] = 0
  heappush(min_heap, (dist[src], src))
  while len(min_heap) != 0:
    top = heappop(min_heap)
    u = top[1]
    if visited[u]:
      continue
    visited[u] = True

    for (w, v) in graph[u]:
      if visited[v] == False and w < dist[v]:
        dist[v] = w
        path[v] = u
        heappush(min_heap, (w, v))

def print_dist():
  res = 0
  for i in range(1, N):
    if path[i] == -1:
      continue
    res += dist[i]
  print('{:.2f}'.format(res))

T = int(input())
input()
for _ in range(T):
  N = int(input())
  min_heap = []
  graph = [[] for i in range(N)]
  dist = [INF for i in range(N)]
  path = [-1 for i in range(N)]
  visited = [False for i in range(N)]
  points = []

  for _ in range(N):
    x, y = list(map(float, input().split()))
    points.append((x, y))
  for i in range(N):
    for j in range(i, N):
      w = distance(points[i], points[j])
      if i != j:
        graph[i].append((w, j))
        graph[j].append((w, i))

  prim(0)
  print_dist()