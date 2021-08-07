# import heapq

class PQEntry:
  def __init__(self, value):
    self.value = value
  def __lt__(self, other):
    return self.value > other.value
  def __eq__(self, other):
    return self.value == other.value

# # Monk and Multiplication
# def monk_and_multiplication(n, a):
#   h = []
#   for i in range(n):
#     heapq.heappush(h, PQEntry(a[i]))
#     if (i < 2):
#       print(-1)
#     else:
#       max_1 = heapq.heappop(h).value
#       max_2 = heapq.heappop(h).value
#       max_3 = heapq.heappop(h).value

#       print(max_1 * max_2 * max_3)

#       heapq.heappush(h, PQEntry(max_1))
#       heapq.heappush(h, PQEntry(max_2))
#       heapq.heappush(h, PQEntry(max_3))

# # Input
# n = int(input())
# a = list(map(int, input().split()))

# # Run and output
# monk_and_multiplication(n , a)

# # Qheap 1
# heap = []
# item_lookup = set()

# def push(v):
#   heapq.heappush(heap, v)
#   item_lookup.add(v)

# def discard(v):
#   item_lookup.discard(v)

# def print_min():
#   while heap[0] not in item_lookup:
#     heapq.heappop(heap)

#   print(heap[0])

# cmds = {
#   1: push,
#   2: discard,
#   3: print_min
# }

# n = int(input())
# for _ in range(n):
#   data = list(map(int, input().split()))
#   cmds[data[0]](*data[1:])

# # Add All
# from heapq import heappush, heappop, heapify

# while True:
#   num_numbers = int(input())

#   if num_numbers == 0:
#     break

#   numbers = list(map(int, input().split()))

#   sol = 0
#   if num_numbers >= 2:
#     heapify(numbers)
#     sol = partial_sum = heappop(numbers) + heappop(numbers)
#     for j in range(num_numbers - 2) :
#       heappush(numbers, partial_sum)
#       partial_sum = heappop(numbers) + heappop(numbers)
#       sol += partial_sum

#   print(sol)

# # Roy and Trending Topics
# from heapq import heappush, heappop

# class Topic:
#   def __init__(self, _id, _old_score, _new_score):
#     self.id = _id
#     self.old_score = _old_score
#     self.new_score = _new_score
#     self.change = self.new_score - self.old_score

#   def __lt__(self, other):
#     return self.change > other.change or (self.change == other.change and self.id > other.id)

# n = int(input())
# h = []
# for _ in range(n):
#   id, old_score, post, like, comment, share = map(int, input().split())
#   new_score = post * 50 + like * 5 + comment * 10 + share * 20
#   heappush(h, Topic(id, old_score, new_score))

# for i in range(5):
#   t = heappop(h)
#   print(t.id, t.new_score)

# # Promotion
# from heapq import heappush, heappop

# n = int(input())

# taken = [False] * 1000005

# money = 0
# h_max = []
# h_min = []
# bills = 0

# for _ in range(n):
#   promotion_in_day = list(map(int, input().split()))

#   for x in promotion_in_day[1:]:
#     bills += 1
#     heappush(h_max, (-x, bills))
#     heappush(h_min, (x, bills))

#   # Check if current max receipt was used before
#   while taken[h_max[0][1]]:
#     heappop(h_max)

#   while taken[h_min[0][1]]:
#     heappop(h_min)

#   # Mark receipts is in ther box
#   taken[h_max[0][1]] = taken[h_min[0][1]] = True
#   money += -heappop(h_max)[0] - heappop(h_min)[0]

# print(money)

# # Restaurant Rating
# from heapq import heappush, heappop
# top3 = []
# rest = []
# nreviews = 0

# n = int(input())

# for _ in range(n):
#   line = list(map(int, input().split()))
#   type = line[0]

#   if type == 1:
#     x = line[1]
#     nreviews += 1
#     if len(top3) != 0 and top3[0] < x:
#       heappush(rest, -heappop(top3))
#       heappush(top3, x)
#     else:
#       heappush(rest, -x)
    
#     if nreviews % 3 == 0:
#       heappush(top3, -heappop(rest))

#   else:
#     if len(top3) == 0:
#       print("No reviews yet")
#     else:
#       print(top3[0])

# I Can Guess the Data Structure!
# from heapq import heappush, heappop
# import queue
# s = []
# q = queue.Queue()
# h = []
 
# while True:
#   try:
#     n = int(input())
#   except EOFError:
#     break

#   s.clear()
#   q.queue.clear()
#   h = []
#   isStack = isQueue = isPQ = True
    
#   for _ in range(n):
#     type, x = map(int, input().split())
#     if type == 1:
#       s.append(x)
#       q.put(x)
#       heappush(h, -x)
#     else:
#       if len(s) == 0:
#         isStack = isQueue = isPQ = False
#       else:
#         if x != s.pop():
#           isStack = False
#         if x != q.get():
#           isQueue = False
#         if x != -heappop(h):
#           isPQ = False

#   if isStack + isQueue + isPQ == 0:
#     print("impossible")
#   elif isStack + isQueue + isPQ > 1:
#     print("not sure")
#   elif isStack:
#     print("stack")
#   elif isQueue:
#     print("queue")
#   else:
#     print("priority queue")

# The Lazy Programmer
from heapq import heappush, heappop
t = int(input())

for _ in range(t):
  time = 0
  min_money = 0

  n = int(input())

  h = []

  contracts = []

  for i in range(n):
    a, b, d = list(map(int, input().split()))
    contracts.append((d, a, b))
  contracts.sort()

  for d, a, b in contracts:
    time += b
    heappush(h, (-a, b, d))
    while time > d:
      c_a, c_b, c_d = heappop(h)
      if c_b > time - d:
        c_b -= time - d
        min_money += (time - d) / -c_a
        time = d
        heappush(h, (c_a, c_b, c_d))
      else:
        time -= c_b
        min_money += c_b / -c_a

  print('{:.2f}'.format(min_money))
      


