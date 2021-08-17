# Where is the Marble
import bisect

def find_marble(marbles, left, right, query):
  if left <= right:
    mid = (left + right) // 2
    if (mid == right or query > marbles[mid - 1]) and marbles[mid] == query:
      return mid
    elif marbles[mid] < query:
      return find_marble(marbles, mid + 1, right, query)
    else:
      return find_marble(marbles, left, mid - 1, query)
  return -1

case = 0
while True:
  n, q = list(map(int, input().split()))

  if n == 0 and q == 0:
    break
  case += 1
  marbles = []
  for i in range(n):
    marble = int(input())
    marbles.append(marble)
  marbles.sort()
  print('CASE# {}:'.format(case))
  for _ in range(q):
    query = int(input())
    result = find_marble(marbles, 0, n - 1, query)
    if result == -1:
      print('{} not found'.format(query))
    else:
      print('{} found at {}'.format(query, result + 1))

