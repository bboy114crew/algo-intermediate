class Node:
  def __init__(self):
    self.left = None
    self.right = None
    self.key = None

def create_node(key):
  new_node = Node()
  new_node.key = key
  return new_node

def insert_node(root, x):
  if root == None:
    return create_node(x)
  if x < root.key:
    root.left = insert_node(root.left, x)
  elif x > root.key:
    root.right = insert_node(root.right, x)
  return root
# # Distinct Count
# T = int(input())

# for _ in range(T):
#   N, X = list(map(int, input().split()))
#   numbers = list(map(int, input().split()))

#   # distinct = {}
#   # number_of_distinct = 0
#   # for num in numbers:
#   #   if distinct.get(num, None) != None:
#   #     distinct[num] += 1
#   #   else:
#   #     distinct[num] = 1
#   #     number_of_distinct += 1

#   distinct = set()
#   for num in numbers:
#     distinct.add(num)
#   number_of_distinct = len(distinct)
  
#   if number_of_distinct == X:
#     print('Good')
#   elif number_of_distinct < X:
#     print('Bad')
#   else:
#     print('Average')

# Isenbaev's Number
import queue
def BFS(graph, src, rank):
  Q = queue.Queue()
  rank[src] = 0
  Q.put(src)
  while not Q.empty():
    u = Q.get()
    for v in graph[u]:
      if rank[v] == 'undefined':
        rank[v] = rank[u] + 1
        Q.put(v)
  return rank

n = int(input())
S = dict()
cnt = 0
graph = []

# Lưu Tên map với số sau đó lưu vào BTS self-balance để search cho tối ưu

for i in range(n):
  line = input().split()
  v = []
  for name in line:
    if name in S:
      id = S[name]
    else:
      S[name] = cnt
      id = cnt
      graph.append([])
      cnt+= 1
    v.append(id)
  for x in v:
    for y in v:
      if x != y:
        graph[x].append(y)
rank = ['undefined' for i in range(cnt)]
if 'Isenbaev' in S:
  rank = BFS(graph, S['Isenbaev'], rank)
a = []
for name in S:
  a.append(name)
a.sort()
for name in a:
  print(name + ' ' + str(rank[S[name]]))
