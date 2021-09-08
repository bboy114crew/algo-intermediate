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
parent = []
ranks = []

def make_set(n):
  global parent, ranks
  parent = [i for i in range(n + 1)]
  ranks = [i for i in range(n + 1)]

def find_set(u):
  global parent
  if parent[u] != u:
    parent[u] = find_set(parent[u])
  return parent[u]

def union_set(u, v):
  global parent, ranks
  up = find_set(u)
  vp = find_set(v)

  if up == vp:
    return

  if ranks[up] > ranks[vp]:
    parent[vp] = up
  elif ranks[up] < ranks[vp]:
    parent[up] = vp
  else:
    parent[up] = vp
    ranks[vp] += 1

case = 0

while True:
  N, M = list(map(int, input().split()))

  if N == 0 and M == 0:
    break
  
  case += 1
  result = N

  make_set(N)
  for _ in range(M):
    i, j = list(map(int, input().split()))
    u = find_set(i)
    v = find_set(j)
    if u != v:
      result -= 1
      union_set(i, j)

  print('Case {}: {}'.format(case, result))