# # Where is the Marble
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

# # Eko
# import math
# N, M = list(map(int, input().split()))

# heights_of_tree = list(map(int, input().split()))
# heights_of_tree.append(0)
# N += 1
# heights_of_tree.sort()

# t = 0
# sum = 0

# result = 0

# for i in range(N - 1, -1, -1):
#   t += 1
#   sum += heights_of_tree[i]
#   if sum - heights_of_tree[i] * t < M:
#     continue
#   elif sum - heights_of_tree[i] * t == M:
#     result = (sum - M) / t  
#     break
#   else:
#     result = (sum - heights_of_tree[i] - M) // (t - 1)
#     break

# print(math.floor(result))

# # The Playboy Chimp
# # https://onlinejudge.org/external/106/10611.pdf
# import bisect
# def bs_first(a, left, right, x):
#   if left < right:
#     mid = (left + right) // 2
#     if (mid == left or x > a[mid - 1]) and a[mid] == x:
#       return mid
#     elif x > a[mid]:
#       return bs_first(a, mid + 1, right, x)
#     else:
#       return bs_first(a, left, mid - 1, x)
#   return -1

# def bs_last(a, left, right, x):
#   if left < right:
#     mid = (left + right) // 2
#     if (mid == right or x < a[mid + 1]) and a[mid] == x:
#       return mid
#     elif x < a[mid]:
#       return bs_first(a, left, mid - 1, x)
#     else:
#       return bs_first(a, mid + 1, right, x)
#   return -1

# N = int(input())

# heights_of_chimps = list(map(int, input().split()))

# Q = int(input())

# queries = list(map(int, input().split()))

# for query in queries:
#   r1 = 'X'
#   r2 = 'X'
#   left = bisect.bisect_left(heights_of_chimps, query)
#   right = bisect.bisect_right(heights_of_chimps, query)
#   if right != N:
#     r2 = heights_of_chimps[right]

#   if left > 0:
#     r1 = heights_of_chimps[left - 1]
  
#   print('{} {}'.format(r1, r2))

# The Monkey and the Oiled Bamboo - https://onlinejudge.org/external/120/12032.pdf

T = int(input())

for t in range(T):
  
  n = int(input())
  r = list(map(int, input().split()))
  if len(r) == 1:
    print('Case {}: {}'.format(t + 1, r[0]))
    continue
  steps = []
  for j in range(len(r)):
    if j != len(r) - 1:
      steps.append(r[j + 1] - r[j])
  steps.append(r[0])
  steps.sort()
  result = steps[-1]

  for i in range(len(steps) - 1, -1, -1):
    if result == steps[i]:
      result -= 1
  
  if result > 0:
    result = steps[-1]
  elif result == 0:
    result = steps[-1] + 1
  else:
    result = steps[-1] - result
  print('Case {}: {}'.format(t + 1, result))

# Other solution:
T = int(input())
for tc in range(1, T + 1):
  print('Case %d: ' % tc, end = '')
  n = int(input())
  a = [0] + list(map(int, input().split()))
  l = 1
  r = a[-1] + 1
  res = 0
  
  while l <= r:
    mid = (l + r) // 2
    k = mid
    check = True
    
    for i in range(n + 1):
      if a[i] - a[i - 1] > k:
        check = False
        break
      else:
        if a[i] - a[i - 1] == k:
          k -= 1
    
    if check:
      res = mid
      r = mid - 1
    else:
      l = mid + 1

  print(res)
