import heapq

class PQEntry:
  def __init__(self, value):
    self.value = value
  def __lt__(self, other):
    return self.value > other.value
  def __eq__(self, other):
    return self.value == other.value

# Monk and Multiplication
def monk_and_multiplication(n, a):
  h = []
  for i in range(n):
    heapq.heappush(h, PQEntry(a[i]))
    if (i < 2):
      print(-1)
    else:
      max_1 = heapq.heappop(h).value
      max_2 = heapq.heappop(h).value
      max_3 = heapq.heappop(h).value

      print(max_1 * max_2 * max_3)

      heapq.heappush(h, PQEntry(max_1))
      heapq.heappush(h, PQEntry(max_2))
      heapq.heappush(h, PQEntry(max_3))

# Input
n = int(input())
a = list(map(int, input().split()))

# Run and output
monk_and_multiplication(n , a)