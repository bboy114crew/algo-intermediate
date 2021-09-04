'''
make_set() Tạo ra tập hợp cho mỗi phần tử ban đầu
find_set(u) Tìm ra phần tử đại diện cho tập hợp ban đầu
uniset(u, v) Hợp tập hợp chứa u và tập hợp chứa v thành 1 tập hợp. Nếu đang cùng 1 tập hợp rồi thì không thực hiện
'''
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

# # Friends
# parent = []
# ranks = []
# num = []

# def make_set(n):
#   global parent, ranks, num
#   parent = [i for i in range(n + 1)]
#   ranks = [i for i in range(n + 1)]
#   num = [1 for i in range(n + 1)]

# def find_set(u):
#   global parent
#   if parent[u] != u:
#     parent[u] = find_set(parent[u])
#   return parent[u]

# def union_set(u, v):
#   global parent, ranks, num
#   up = find_set(u)
#   vp = find_set(v)

#   if up == vp:
#     return

#   if ranks[up] > ranks[vp]:
#     parent[vp] = up
#     num[up] += num[vp]
#   elif ranks[up] < ranks[vp]:
#     parent[up] = vp
#     num[vp] += num[up]
#   else:
#     parent[up] = vp
#     ranks[vp] += 1
#     num[vp] += num[up]

# T = int(input())

# for _ in range(T):
#   N, M = list(map(int, input().split()))
#   make_set(N)
#   for i in range(M):
#     A, B = list(map(int, input().split()))
#     union_set(A, B)

#   result = 0
#   for i in range(1, N + 1):
#     result = max(result, num[i])
#   print(result)

# Graph Connectivity

# parent = []
# ranks = []

# def make_set(n):
#   global parent, ranks
#   parent = [i for i in range(n)]
#   ranks = [i for i in range(n)]

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

# T = int(input())
# input()

# for _ in range(T):
#   MAX = input()
#   N = ord(MAX) - ord('A') + 1
#   ans = N
#   make_set(N)
#   while True:
#     try:
#       edge = input()
#       if edge == '':
#         break
#       x = ord(edge[0]) - ord('A')
#       y = ord(edge[1]) - ord('A')

#       if find_set(x) != find_set(y):
#         union_set(x, y)
#         ans -= 1
#     except EOFError:
#       break
#   print(ans)
#   print()

# # Forests
# def find_set(u):
#   global parent
#   if u != parent[u]:
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

# Q = int(input())
# input()

# while Q > 0:
#   P, T = map(int, input().split())
#   trees = [set() for i in range(P + 1)]
#   parent = [i for i in range(P + 1)]
#   ranks = [0 for i in range(P + 1)]

#   while True:
#     try:
#       line = input()
#       if not line:
#         break
#       person, tree = map(int, line.split())
#       trees[person].add(tree)
#     except EOFError:
#         break

#   for i in range(1, P + 1):
#     for j in range(i + 1, P + 1):
#       # If set i identical with set j => we union i vs j 
#       if trees[i] == trees[j]:
#         union_set(i, j)
#   # If i == parent[i] => it isn't union yet.
#   ans = sum(1 for i in range(1, P + 1) if i == parent[i])
#   print(ans)
#   Q -= 1

#   if Q > 0:
#     print()
