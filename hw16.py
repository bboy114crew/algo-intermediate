'''
make_set() Tạo ra tập hợp cho mỗi phần tử ban đầu
find_set(u) Tìm ra phần tử đại diện cho tập hợp ban đầu
uniset(u, v) Hợp tập hợp chứa u và tập hợp chứa v thành 1 tập hợp. Nếu đang cùng 1 tập hợp rồi thì không thực hiện
'''

# Friends
MAX = 3000
parent = []
ranks = []
num = []

def make_set(n):
  global parent, ranks, num
  parent = [i for i in range(n + 1)]
  ranks = [i for i in range(n + 1)]
  num = [1 for i in range(n + 1)]

def find_set(u):
  global parent
  if parent[u] != u:
    parent[u] = find_set(parent[u])
  return parent[u]

def union_set(u, v):
  global parent, ranks, num
  up = find_set(u)
  vp = find_set(v)

  if up == vp:
    return

  if ranks[up] > ranks[vp]:
    parent[vp] = up
    num[up] += num[vp]
  elif ranks[up] < ranks[vp]:
    parent[up] = vp
    num[vp] += num[up]
  else:
    parent[up] = vp
    ranks[vp] += 1
    num[vp] += num[up]

T = int(input())

for _ in range(T):
  N, M = list(map(int, input().split()))
  make_set(N)
  for i in range(M):
    A, B = list(map(int, input().split()))
    union_set(A, B)

  result = 0
  for i in range(1, N + 1):
    result = max(result, num[i])
  print(result)
