# # Where is the Marble
# import bisect

# def find_marble(marbles, left, right, query):
#   if left <= right:
#     mid = left + (right - left) // 2
#     if marbles[mid] == query and (mid == left or query > marbles[mid - 1]):
#       return mid
#     elif marbles[mid] < query:
#       return find_marble(marbles, mid + 1, right, query)
#     else:
#       return find_marble(marbles, left, mid - 1, query)
#   return -1

# case = 0
# while True:
#   n, q = list(map(int, input().split()))

#   if n == 0 and q == 0:
#     break
#   case += 1
#   marbles = []
#   for i in range(n):
#     marble = int(input())
#     marbles.append(marble)
#   marbles.sort()
#   print('CASE# {}:'.format(case))
#   for _ in range(q):
#     query = int(input())
#     result = find_marble(marbles, 0, n - 1, query)
#     if result == -1:
#       print('{} not found'.format(query))
#     else:
#       print('{} found at {}'.format(query, result + 1))

# # Pizzamania
# t = int(input())

# for _ in range(t):
#   n, m = list(map(int, input().split()))
#   array = list(map(int, input().split()))
#   array.sort()

#   start = 0
#   tail = n - 1
#   count = 0

#   while tail > start:
#     sum = array[tail] + array[start]
#     if sum == m:
#       count += 1
#       tail -= 1
#       start += 1
#     elif sum > m:
#       tail -= 1
#     else:
#       start += 1
  
#   print(count)

# Eko
import math
N, M = list(map(int, input().split()))

heights_of_tree = list(map(int, input().split()))
heights_of_tree.append(0)
N += 1
heights_of_tree.sort()

t = 0
sum = 0

result = 0

for i in range(N - 1, -1, -1):
  t += 1
  sum += heights_of_tree[i]
  if sum - heights_of_tree[i] * t < M:
    continue
  elif sum - heights_of_tree[i] * t == M:
    result = (sum - M) / t  
    break
  else:
    result = (sum - heights_of_tree[i] - M) // (t - 1)
    break

print(math.floor(result))